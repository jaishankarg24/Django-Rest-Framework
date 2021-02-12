import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

# def get_resource(id=None):
# 	data={}
# 	if id is not None:
# 		data = {'id':id}
# 	response = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
# 	print(response.json())
# 	print(response.status_code)

# get_resource()

# def create_resource():
# 	new_emp = {'eno':11,'ename':'Ashwini','esalary':60000,'eaddress':'bangalore'}

# 	response = requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
# 	print(response.json())
# 	print(response.status_code)

# create_resource()

def update_resource(id):
	update_data = {'id':id,'ename':'kiran','esalary':51245}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)
update_resource(2)


# def delete_resource(id):
# 	emp_data={'id':id}
# 	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(emp_data))
# 	print(response.json())
# 	print(response.status_code)
# delete_resource(1)