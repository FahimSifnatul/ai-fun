from django import forms
from .models import ImageToText

class ImageToTextForm(forms.ModelForm):
	class Meta:
		model  = ImageToText
		fields = '__all__'
		widget = {
			'image_to_text' : forms.ClearableFileInput(\
								attrs={'id':'image_to_text_image'}),
		}