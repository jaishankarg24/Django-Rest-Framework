import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project16.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker 
from random import *

def generate_fake(num):
	for i in range(num):
		fake_eno=randint(100, 200)
		fake_name=faker.name()
		fake_salary=randint(100000, 300000)
		fake_address=faker.city()
		employee_record=Employee.objects.get_or_create(eno=fake_eno,ename=fake_name,esalary=fake_salary,eaddress=fake_address)

if __name__ == '__main__':
	faker=Faker()
	num=int(input('Enter the number of employee:\t'))
	generate_fake(num)

