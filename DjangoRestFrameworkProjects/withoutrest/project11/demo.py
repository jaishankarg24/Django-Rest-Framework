import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='apidata/'

# def get_resource(id):

# 	response=requests.get(BASE_URL+END_POINT+id+'/')
# 	print(response)
# 	print(type(response))
# 	print(response.status_code)
# 	print(response.json())
# 	print(type(response.json()))

# id=input('Enter the id:\t')
# get_resource(id)

#Error handling in Partner application(python Application)
def get_resource(id):

	response=requests.get(BASE_URL+END_POINT+id+'/')
	# if response.status_code in range(200,300):
	if response.status_code == requests.codes.ok:
		print(response.status_code)
		print(response.json())
	else:
		print('The required source is not available')
	
id=input('Enter the id:\t')
get_resource(id)