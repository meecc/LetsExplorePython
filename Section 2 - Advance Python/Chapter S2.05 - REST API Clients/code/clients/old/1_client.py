import requests

try:
    response = requests.get("http://127.0.0.1:5000/cities")
    print(response)
except Exception as e:
    print(e)
