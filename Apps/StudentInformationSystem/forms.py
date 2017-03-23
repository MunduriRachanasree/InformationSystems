from django.forms import ModelForm
from StudentInformationSystem.models import *

class PersonalInfoForm(ModelForm):
	class Meta:
		model = PersonalInfo
		fields = '__all__'			


class AcedamicInfoForm(ModelForm):
	class Meta:
		model = AcedamicInfo
		exclude = ('studentId',)
		
class AdditionalInfoForm(ModelForm):
	class Meta:
		model = AdditionalInfo
		exclude = ('studentId',)
					
