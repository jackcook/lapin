import requests

while True:
    try:
        requests.get("http://localhost:8080")
    except:
        pass