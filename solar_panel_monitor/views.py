from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ValueInputForm
from .sheet_handler import validateAndPostSolarData
import os
# Create your views here.
# credentials need to be gathered in the main folder, here: ls_webdev_project


def getCurrentFileDir():
    return os.path.dirname(os.path.realpath(__file__))


def index(request):
    valueInputForm = ValueInputForm()

    if request.method == "POST":
        valueInputForm = ValueInputForm(request.POST)
        if valueInputForm.is_valid():
            dataReceived = valueInputForm.data
            password = "asd"
            postSuccessful = False
            with open(os.path.join(settings.BASE_DIR, "solar_panel_monitor", "credentials", 'password.txt')) as file:
                password = file.read()
            print(password)
            if password != dataReceived["password"]:
                messages.error(request, "Passwords don't match")
                return redirect("solar-meter-input")
            else:
                postSuccessful = validateAndPostSolarData(dataReceived)

            if not postSuccessful:
                messages.error(request, "Error in submitting info")
                return redirect("solar-meter-input")
            valueInputForm.clean()
            valueInputForm.save()
            messages.success(request, "Values Successfully Added/Updated")

    context = {
        "ValueInputForm": valueInputForm
    }

    return render(request, 'solar_panel_monitor/index.html', context)
