from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from courseapp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
	return render(request=request, template_name='courseapp/homepage.html')


def courses(request):
	return render(request=request, template_name='courseapp/courses.html')


@login_required
def python_course(request):
	return render(request=request, template_name='courseapp/python.html')

@login_required
def java_course(request):
	return render(request=request, template_name='courseapp/java.html')

@login_required
def testing_course(request):
	return render(request=request, template_name='courseapp/testing.html')

def logout_page(request):
	return render(request=request, template_name='courseapp/logout.html')


def signup_page(request):
	form=SignupForm()
	my_dict={'form':form}
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
		return HttpResponseRedirect('/accounts/login/')

	return render(request=request, template_name='courseapp/signup.html',context=my_dict)