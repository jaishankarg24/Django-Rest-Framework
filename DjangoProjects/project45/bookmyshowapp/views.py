from django.shortcuts import render,redirect
from bookmyshowapp.models import Movie
from bookmyshowapp.forms import MovieForm

# Create your views here.

def homepage(request):
	return render(request=request, template_name='bookmyshowapp/homepage.html')
	
def retrieve_data(request):
	movie=Movie.objects.all()
	my_dict={'movie':movie}
	return render(request=request, template_name='bookmyshowapp/display.html',context=my_dict)

def create_data(request):
	form=MovieForm()
	my_dict={'form':form}
	if request.method=='POST':
		form=MovieForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/display/')	

	return render(request=request, template_name='bookmyshowapp/create.html',context=my_dict)

def delete_view(request,id):
	movie=Movie.objects.get(id=id)
	movie.delete()
	return redirect('/display/')	

def update_view(request,id):
	movie=Movie.objects.get(id=id)
	my_dict={'movie':movie}
	if request.method=='POST':
		form=MovieForm(request.POST, instance=movie)
		if form.is_valid():
			form.save()
		return redirect('/display/')
	return render(request=request, template_name='bookmyshowapp/update.html',context=my_dict)


