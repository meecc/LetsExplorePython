import requests
import json
import codecs

reader = codecs.getreader("utf-8")
#url = "http://www.cricbuzz.com/match-push?id=19187"

url = "http://push.cricbuzz.com/match-push?id=19187"
resp = requests.get(url)
print(resp)
#print(resp.json())
print(resp.content)
feed = json.load(reader(resp.content))
print(feed['score']['over_summary'])

