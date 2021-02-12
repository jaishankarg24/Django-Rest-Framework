from django.shortcuts import render
from movieapp.forms import MovieTableForm

# Create your views here.

def display_page(request):

	return render(request=request, template_name='movieapp/display.html')
	
def thankyou_page(request):
	return render(request=request, template_name='movieapp/thankyou.html')

def addmovie(request):

	form = MovieTableForm()
	my_dict = {'form' : form}

	if request.method=='POST':
		movie_form = MovieTableForm(request.POST)

		if movie_form.is_valid():
			movie_form.save(commit=True)

	if request.method=='POST':
		form_movie = MovieTableForm(request.POST)

		if form_movie.is_valid():
			print(f'NAME:{form_movie.cleaned_data["name"]}')
			print(f'RELEASE:{form_movie.cleaned_data["releasedate"]}')
			print(f'HERO:{form_movie.cleaned_data["hero"]}')
			print(f'HEROINE:{form_movie.cleaned_data["heroine"]}')
			print(f'DIRECTOR:{form_movie.cleaned_data["director"]}')
			print(f'BUDGET:{form_movie.cleaned_data["budget"]}')
			print(f'LANGUAGE:{form_movie.cleaned_data["language"]}')
			print(f'RATING:{form_movie.cleaned_data["rating"]}')

			return thankyou_page(request)


	return render(request=request, template_name='movieapp/addmovie.html', context=my_dict)


from movieapp.models import MoviesTable

def showmovie(request):

	form_movie = MoviesTable.objects.all()
	my_dict = {'form_movie': form_movie}


	return render(request=request, template_name='movieapp/showmovie.html', context=my_dict)
