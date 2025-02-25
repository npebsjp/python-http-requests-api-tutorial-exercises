import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")


data = response.json()


print(data[2]["images"][2])