from django.shortcuts import render
from datetime import datetime
# Create your views here.

def display_time(request):

	date = datetime.now()
	hour = int(datetime.now().hour)

	msg = 'Hi Students Good'

	if hour<12:
		msg+=' Morning'

	elif hour<16:
		msg+=' Afternoon'

	elif hour<21:
		msg+=' Evening'

	else:
		msg+=' Night'

	my_dict={'time': date, 'message': msg}

	return render(request=request, template_name='displaytimeapp/time.html', context=my_dict)