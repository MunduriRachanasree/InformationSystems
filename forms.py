from django.forms import ModelForm
from TPOv1.models import Drive
#from django.utils import timezone
#from django import forms

class DriveForm(ModelForm):
	class Meta:
		model = Drive
		fields = "__all__"

