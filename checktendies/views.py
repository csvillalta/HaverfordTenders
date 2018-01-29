from django.shortcuts import render
from django.http import HttpResponse
from . import scraper

def index(request):

	context = {'tendiestoday': scraper.checktendies()}
	return render(request, 'checktendies/index.html', context)