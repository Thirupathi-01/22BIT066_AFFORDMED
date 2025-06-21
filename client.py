import requests
ele=input("give letter")
endpoint=f"http://127.0.0.1:8000/{ele}"

response=requests.get(endpoint)
print(response.status_code)
print(response.json())