from django.shortcuts import render

# Create your views here.

def home_page(request):
	return render(request=request, template_name='templateinheritanceapp/homepage.html')

def movies_page(request):
	return render(request=request, template_name='templateinheritanceapp/moviespage.html')

def events_page(request):
	return render(request=request, template_name='templateinheritanceapp/eventspage.html')

def sports_page(request):
	return render(request=request, template_name='templateinheritanceapp/sportspage.html')