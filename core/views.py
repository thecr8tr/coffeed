from django.shortcuts import render
from django.views.generic import TemplateView

class SplashView(TemplateView):
	"""docstring for SplashView"TemplateView"""
	template_name = 'index.html'
	