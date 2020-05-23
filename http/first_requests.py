import requests
url = "http://www.google.co.uk"
response = requests.get(url)
# print(response.status_code)

url1 = "https://icanhazdadjoke.com"

res = requests.get(url1, headers ={"Accept": "text/plain"})


url2 = "https://icanhazdadjoke.com/search"
res1 = requests.get(
    url2, 
    headers ={"Accept": "application/json"},
    params={"term": "dog", "limit": "1"}
)
data = res1.json()
print(data)

