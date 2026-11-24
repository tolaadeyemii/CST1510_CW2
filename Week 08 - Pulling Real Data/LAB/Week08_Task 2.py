import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print("Name:", user["name"], "- Email:", user["email"])

print("Total users:", len(users))