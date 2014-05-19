from django import forms

from .models import Cerveja

class CervejaForm(forms.ModelForm):
	class Meta:
		model = Cerveja
			
	
		