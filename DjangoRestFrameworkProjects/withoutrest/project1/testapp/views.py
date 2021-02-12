from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def student_data(request):
	data={'eno':4, 'ename':'jaishankar g', 'eage':23, 'eaddress':'shimoga'}
	response= '<h1>HTML RESPONSE <br> Student Number : {} <br> Student Name : {} <br> Student Age : {} <br> Student Address : {} <br></h1>'.format(data['eno'], data['ename'], data['eage'], data['eaddress'])
	return HttpResponse(response)