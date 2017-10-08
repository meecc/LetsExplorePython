import requests
import json

url = "http://www.cricbuzz.com/match-push?id=16859"

resp = requests.get(url)
print(resp)
print(resp.json)
#print(resp.content)
feed = json.loads(resp.content)
print(feed['score']['over_summary'])

