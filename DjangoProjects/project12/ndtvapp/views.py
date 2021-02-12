from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request=request, template_name='ndtvapp/index.html')


def display_movies_information(request):
	main_msg = 'Latest Movie Information'

	msg1 = 'RRR shooting is in progess!!!'
	msg2 = 'Robert by Dboss will be released by the end of this Year'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request=request, template_name='ndtvapp/movies.html',context=my_dict)


def display_sports_information(request):
	main_msg = 'Latest Sports Information'

	msg1 = 'IPL will be held in Dubai'
	msg2 = 'Dhoni got retired!!'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request=request, template_name='ndtvapp/sports.html',context=my_dict)


def display_politics_information(request):
	main_msg = 'Latest Politics Information'

	msg1 = 'Modi will become PM for next election also!!!'
	msg2 = 'Rahul Gandhi is the best bachelor in India'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request=request, template_name='ndtvapp/politics.html',context=my_dict)