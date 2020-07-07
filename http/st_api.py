import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': '33093',
    'client_secret': 'd8ff435df2baf1545f911bd67cb0c00055a9c9a7',
    'refresh_token': 'cfbd75799937ffc01bc199a3058e43d26456e829',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
print(res.json())
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))



header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

print(my_dataset)