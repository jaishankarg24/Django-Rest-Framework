import requests
import json
import time
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resource(id=None):
	data={}
	if id is not None:
		data = {'id':id}
	response = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)

get_resource()

time.sleep(5)

def create_resource():
	new_emp = {'eno':22,'ename':'Monica','esalary':80000,'eaddress':'bangalore'}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
	print(response.json())
	print(response.status_code)

create_resource()

time.sleep(5)

def update_resource(id):
	update_data = {'id':id,'ename':'venky','esalary':40000}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)
update_resource(2)

time.sleep(5)

def delete_resource(id):
	emp_data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(emp_data))
	print(response.json())
	print(response.status_code)
delete_resource(3)