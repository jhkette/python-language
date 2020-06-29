import requests

url = 'https://www.strava.com/api/v3/athlete'




res1 = requests.get(
    url,
    headers ={"Accept": "application/json",
    "Authorization" : "Bearer b41ff52e6456c9c3663e10185a528d9a1f5dbe1e"}
)

x = res1.json()

print(x)