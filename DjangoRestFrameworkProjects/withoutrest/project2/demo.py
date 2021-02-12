import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='apijson/'
response = requests.get(BASE_URL + END_POINT)
print(response)
print(response.text)
print(type(response))

dict_response=response.json()
print(dict_response)
print(type(dict_response))

print('Student Number: ' , dict_response['eno'])
print('Student Name: ' , dict_response['ename'])
print('Student Age: ' , dict_response['eage'])
print('Student Address: ', dict_response['eaddress'])