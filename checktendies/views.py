from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import scraper
from .forms import PhoneForm

def index(request):
	if request.method == 'POST':
		form = PhoneForm(request.POST)
		if form.is_valid():
			submitted_phone = True
			form.save()
			return HttpResponseRedirect(request.get_full_path())
	else:
		form = PhoneForm()

	context = {'tendiestoday': scraper.checktendies(),'phone_form': form}
	return render(request, 'checktendies/index.html', context)