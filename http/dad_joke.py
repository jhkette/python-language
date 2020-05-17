import pyfiglet
import termcolor
import requests
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="magenta")
print(header)

url1 = "https://icanhazdadjoke.com/search"

topic = input('Please type in a joke topic: ')

url2 = "https://icanhazdadjoke.com/search"

res1 = requests.get(
    url2,
    headers ={"Accept": "application/json"},
    params ={"term": topic}
)

data = res1.json()

if len(data) > 1:
    print(f'There are {len(data)} jokes about {topic}')
    j = choice(data['results'])['joke']
    print(f'here is a random joke about - {topic} : {j}')
elif len(data) == 1:
    print(data['results']['joke'])
else: 
    print('There are no jokes about that topic')


