from django.shortcuts import render

from studentdetailapp.models import Student

# Create your views here.
def display_homepage(request):
	return render(request=request, template_name='studentdetailapp/homepage.html')


def display_studentdetails(request):

	student_data= Student.objects.all()
	print(student_data)
	print(type(student_data))

	my_dict={'student_data':student_data}
	return render(request=request, template_name='studentdetailapp/display.html', context=my_dict)

