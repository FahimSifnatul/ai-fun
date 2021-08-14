from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from pathlib import Path
from secrets import token_hex

# customs forms
from .forms import ImageToTextForm, RootsOfPolynomialEqForm, TextToWordcloud

# custom models
from .models import ImageToText

# output generator function
from .output_generators import convert_image_to_text, find_roots_of_polynomial_eq, convert_text_to_cloud

# Create your views here.
class Home(APIView):
	def get(self, request, *args, **kwargs):
		context = {
			'form_image_to_text' : ImageToTextForm(),
			'form_roots_of_polynomial_eq' : RootsOfPolynomialEqForm(),
			'form_text_to_wordcloud' : TextToWordcloud(),
		}
		return render(request, 'index.html', context)


	def post(self, request, *args, **kwargs):
		BASE_DIR = Path(__file__).resolve().parent.parent
		context = {}
		context['form_image_to_text'] = ImageToTextForm()
		context['form_roots_of_polynomial_eq'] = RootsOfPolynomialEqForm()
		context['form_text_to_wordcloud'] = TextToWordcloud()

		if 'image_to_text' in request.FILES:
			image_name = token_hex(8) + '.jpg'
			request.FILES['image_to_text'].name = image_name
			image_to_text_form = ImageToTextForm(request.POST, request.FILES)
			image_to_text_form.save()

			image_path = BASE_DIR / 'media' / image_name
			text = convert_image_to_text(str(image_path))
			text = text.replace('\n', '\\n')
			
			# To remove image as output is generated already
			image_path.unlink()

			context['image_to_text'] = 'true'
			context['image_to_text_text'] = text

		elif 'roots_of_polynomial_eq' in request.POST:
			eq = request.POST['roots_of_polynomial_eq']

			context['roots_of_polynomial_eq'] = 'true'
			context['roots'] = find_roots_of_polynomial_eq(eq)

		elif 'text_to_wordcloud' in request.POST:
			text = request.POST['text_to_wordcloud']

			context['text_to_wordcloud'] = 'true'
			context['wordcloud'] = convert_text_to_cloud(text)

		elif 'delete_media_image' in request.POST:
			image = BASE_DIR / 'media' / request.POST['delete_media_image']
			image.unlink()

		return render(request, 'index.html', context)