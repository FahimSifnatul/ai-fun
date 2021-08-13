from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from pathlib import Path
from secrets import token_hex

# customs forms
from .forms import ImageToTextForm, RootsOfPolynomialEqForm

# custom models
from .models import ImageToText

# output generator function
from .output_generators import convert_image_to_text, find_roots_of_polynomial_eq

# Create your views here.
class Home(APIView):
	def get(self, request, *args, **kwargs):
		context = {
			'form_image_to_text' : ImageToTextForm(),
			'form_roots_of_polynomial_eq' : RootsOfPolynomialEqForm(),
		}
		return render(request, 'index.html', context)


	def post(self, request, *args, **kwargs):

		if 'image_to_text' in request.FILES:
			image_name = token_hex(8) + '.jpg'
			request.FILES['image_to_text'].name = image_name
			image_to_text_form = ImageToTextForm(request.POST, request.FILES)
			image_to_text_form.save()

			image_path = Path(__file__).resolve().parent.parent / 'media' / image_name
			text = convert_image_to_text(str(image_path))
			text = text.replace('\n', '\\n')
			
			# To remove image as output is generated already
			image_path.unlink()

			context = {}
			context['image_to_text'] = 'true'
			context['image_to_text_text'] = text

			context['form_image_to_text'] = ImageToTextForm()
			context['form_roots_of_polynomial_eq'] = RootsOfPolynomialEqForm()

			return render(request, 'index.html', context)


		elif 'roots_of_polynomial_eq' in request.POST:
			eq = request.POST['roots_of_polynomial_eq']

			context = {}
			context['roots_of_polynomial_eq'] = 'true'
			context['roots'] = find_roots_of_polynomial_eq(eq)

			context['form_image_to_text'] = ImageToTextForm()
			context['form_roots_of_polynomial_eq'] = RootsOfPolynomialEqForm()

			return render(request, 'index.html', context)