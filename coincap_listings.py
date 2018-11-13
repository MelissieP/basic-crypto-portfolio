"""
Here we get the listing of each specific cryptocurrency which will be useful for later
"""

import json
import requests

listings_url = "https://api.coinmarketcap.com/v2/listings/"

request = requests.get(listings_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

# This loop will output: Rank: Name(Currency)
for currency in data: # Loops through data and gets each block
    rank = currency["id"]
    name = currency["name"]
    symbol = currency["symbol"]
    print(str(rank) + ":" + name + "(" + symbol + ")")

