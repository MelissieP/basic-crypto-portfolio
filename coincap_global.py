"""
Coin cap API gets updated every 5 minutes.
Here we get the global information on cryptocurrency and output it
"""
import json
import requests
from datetime import datetime


# Global API endpoint url
global_url = "https://api.coinmarketcap.com/v2/global/"

# This gets global url and puts json data into the variable
request = requests.get(global_url)

# Format json data
results = request.json()

# Puts in human readable format, json object and converts to a string, rest just formatting
# print(json.dumps(results, sort_keys=True, indent=4))

# Now we are going to create variables out of the entire JSON tree
active_currencies = results["data"]["active_cryptocurrencies"]
active_markets = results["data"]["active_markets"]
bitcoin_percentage = results["data"]["bitcoin_percentage_of_market_cap"]
last_updated = results["data"]["last_updated"]  # Last updated unix timestamp, convert to readable format
# Gets rid of zero after comma
global_cap = int(results["data"]["quotes"]["USD"]["total_market_cap"])
global_volume = int(results["data"]["quotes"]["USD"]["total_volume_24h"])

# To get the variables to be separated by a comma
active_currencies_string = "{:,}".format(active_currencies)
active_markets_string = "{:,}".format(active_markets)
global_cap_string = "{:,}".format(global_cap)
global_volume_string = "{:,}".format(global_volume)

# Create datetime for last_updated
last_updated_string = datetime.fromtimestamp(last_updated).strftime("%B %d, %Y at %I:%M%p") # Look at strftime format

print("\nThere are currently " + active_currencies_string + " active cryptocurrencies and" + active_markets_string +
      " active markets.")
print("\nThe global cap of all cryptos is " + global_cap_string + " and the 24hr global volume is " +
      global_volume_string + ".")
print("\nBitcoin\'s total percentage of global cap is " + str(bitcoin_percentage) + "%.")
print("\nThis information was last updated on " + str(last_updated_string) + ".")
