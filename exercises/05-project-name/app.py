import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

data = response.json()

print(data["name"])