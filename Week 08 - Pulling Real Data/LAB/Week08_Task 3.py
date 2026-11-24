import requests
my_params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

print("Number of posts:", len(posts))
for post in posts:
    print(post["title"])