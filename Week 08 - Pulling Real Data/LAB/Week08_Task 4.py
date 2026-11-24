import requests
urls = ["https://httpbin.org/status/404", "https://httpbin.org/status/500"]

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Success!")
    except requests.exceptions.HTTPError:
        print("Sorry the request failed with status code:", response.status_code)