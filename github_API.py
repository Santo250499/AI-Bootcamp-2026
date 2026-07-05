import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data["login"])
print(data["followers"])
print(data["public_repos"])
print(data["location"])