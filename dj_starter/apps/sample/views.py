# Create your views here.
from django.views.generic import View
from django.http import HttpResponse

class SampleHomeView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello world")