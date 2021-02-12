
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication1(BaseAuthentication):
	def authenticate(self,request):
		username=request.GET.get('username')
		if username is None:
			return None 

		try:
			user=User.objects.get(username=username)
		except User.DoesNotExist:
			raise AuthenticationFailed('Your Credentials Invalid, Please provide the valid Credentials to access the end point')
		return (user,None)

class CustomAuthentication2(BaseAuthentication):
	def authenticate(self,request):
		username=request.GET.get('username')
		key=request.GET.get('key')
		if username is None or key is None:
			return None 
		s1=len(key)==7
		s2=key[0]==username[-1].lower()
		s3=key[2]=='Z'
		s4=key[4]==username[0]

		try:
			user=User.objects.get(username=username)
		except User.DoesNotExist:
			raise AuthenticationFailed('Username is Invalid, Please provide the valid Credentials to access the end point')
		
		if s1 and s2 and s3 and s4:
			return (user,None)

		raise AuthenticationFailed('Please provide the Valid Key to access the end point')
