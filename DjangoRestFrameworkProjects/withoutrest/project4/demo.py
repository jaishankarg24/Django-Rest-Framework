import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='apijsoncbv/'
response=requests.delete(BASE_URL+END_POINT)
print(response)
print(response.text)
print(type(response))

