import urllib2
import json
json_data = urllib2.urlopen("https://api.coinbase.com/v2/prices/spot?currency=USD").read()
data = json.loads(json_data)
print data["data"]["amount"]
