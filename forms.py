from django.forms import ModelForm
from StudentInformationSystem.models import PersonalInfo

class PersonInfoForm(ModelForm):
	class Meta:
		model = PersonalInfo
		fields = '__all__'
