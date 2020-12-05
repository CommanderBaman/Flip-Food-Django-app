import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import requests
import os
from django.conf import settings

def getWeatherDescription(counter=0):
    # using openweather API
    apiKey = "e528ad4ae8df933c255a21b308cbffeb"
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    cityName = "Chandigarh"
    completeURL = baseURL + "appid=" + apiKey + "&q=" + cityName

    # getting weather data as json file
    weatherResponse = requests.get(completeURL)
    weatherData = weatherResponse.json()

    try:
        # returning weather description
        weatherDescription = weatherData["weather"][0]["description"]
        return weatherDescription

    except:
        # API is not connected properly
        # giving 3 tries
        if counter >= 3:
            return None
        else:
            getWeatherDescription(counter + 1)


def getCurrentFileDir():
    return os.path.dirname(os.path.realpath(__file__))


def getSheet():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    # handling so that I run only one command from my console
    try:
        directoryOfCredentials = os.path.join(
            settings.BASE_DIR, "solar_panel_monitor", "credentials", "credentials.json")
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            directoryOfCredentials, scope)
    except:
        print("running except")
        credentialsDir = getCurrentFileDir() + "\\credentials\\credentials.json"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentialsDir, scope)

    # print( credentials)
    client = gspread.authorize(credentials)

    # getting the sheet
    sheet = client.open('Solar Panel Generation - Home').sheet1

    return sheet


def addDataToSheet(sheet, data, numRow):
    try:
        sheet.insert_row(data, numRow)
        return True
    except:
        return False


def updateDataInSheet(sheet, data, numRow):
    try:
        for index, dataValue in enumerate(data):
            sheet.update_cell(numRow, index+1, dataValue)
        return True
    except:
        return False


def getNumRowsFilled(sheet):
    str_list = list(filter(None, sheet.col_values(1)))
    return len(str_list)


def getLastRecordedValues(sheet, secondLast=False):
    numRows = getNumRowsFilled(sheet)
    if secondLast:
        numRows -= 1
    return sheet.row_values(numRows)


def getTimeFromObj(dateObj, onlyDate=False):
    dateFromObj = str(dateObj.strftime("%a, %d %B, %Y"))
    timeFromObj = str(dateObj.strftime("%X"))

    if onlyDate:
        return dateFromObj
    return timeFromObj, dateFromObj


def getLastRecordedDate(sheet):
    return getLastRecordedValues(sheet)[0]


def toUpdate(sheet, dateObj):
    # decide whether to update the value or not - if date is same from last cell, then updates the value
    return getTimeFromObj(dateObj, onlyDate=True) == getLastRecordedDate(sheet)


def prepareData(sheet, unitsOnCompanyMeter, unitsOnActualMeter, unitsConsumedTotal, dateObj):
    data = []
    timeNow, dateToday = getTimeFromObj(dateObj)
    data.append(dateToday)
    data.append(timeNow)

    if toUpdate(sheet, dateObj):
        lastRecordedValues = getLastRecordedValues(sheet, secondLast=True)
    else:
        lastRecordedValues = getLastRecordedValues(sheet)

    data.append(unitsOnCompanyMeter)
    unitsGeneratedCompany = unitsOnCompanyMeter - float(lastRecordedValues[2])
    data.append(unitsGeneratedCompany)

    data.append(getWeatherDescription())

    data.append(unitsOnActualMeter)
    unitsGeneratedActual = unitsOnActualMeter - float(lastRecordedValues[5])
    data.append(unitsGeneratedActual)

    try:
      data.append(unitsGeneratedCompany / unitsGeneratedActual)
    except:
      data.append(0)

    data.append(unitsConsumedTotal)
    unitsConsumedToday = unitsConsumedTotal - float(lastRecordedValues[8])
    data.append(unitsConsumedToday)

    return data


def postSolarValue(sheet, unitsOnCompanyMeter, unitsOnActualMeter, unitsConsumedTotal, dateObj):
    data = prepareData(sheet, unitsOnCompanyMeter,
                       unitsOnActualMeter, unitsConsumedTotal, dateObj)
    numRowsFilled = getNumRowsFilled(sheet)

    if toUpdate(sheet, dateObj):
        return updateDataInSheet(sheet, data, numRowsFilled)
    return addDataToSheet(sheet, data, numRowsFilled + 1)


def validateAndPostSolarData(data):
    sheet = getSheet()
    return postSolarValue(sheet, float(data['solar_meter_company']), float(data['solar_meter_actual']), float(data['consumption']), datetime.now())
