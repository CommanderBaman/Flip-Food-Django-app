from django.forms import ModelForm
from .models import DailyValue

class ValueInputForm(ModelForm):
	class Meta:
		model = DailyValue
		fields = ["solar_meter_company", "solar_meter_actual", "consumption"]

