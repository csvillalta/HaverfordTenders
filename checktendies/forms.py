from django.forms import ModelForm
from checktendies.models import PhoneModel

class PhoneForm(ModelForm):
	class Meta:
		model = PhoneModel
		fields = ['phone_number']