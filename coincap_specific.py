""" This is to get the details of a specific currency"""
import requests

# South African rand
convert = "ZAR"

# Need this in order to create a dict that contains all the currencies with corresponding id
listing_url = "https://api.coinmarketcap.com/v2/listings/"
url_end = "?structure=array&convert=" + convert # We want the json data to be in an array format and convert is equal to the local currency

request = requests.get(listing_url)
results = request.json()

data = results["data"]

# Dictionaries are arrays but they store key value pairs
# Ticker symbol as key and id as value
ticker_url_pairs = {}
for currency in data:
    symbol = currency["symbol"]
    url = currency["id"]
    ticker_url_pairs[symbol] = url # Append each to dict


while True:
    choice = input("Enter the ticker symbol of a cryptocurrency: ")
    # Convert input to uppercase
    choice = choice.upper()

    # Pass type casted to our dictionary and whatever is stored there will be specified in the url
    ticker_url = "https://api.coinmarketcap.com/v2/ticker/" + str(ticker_url_pairs[choice]) + "/" + url_end

    request = requests.get(ticker_url)
    results = request.json()


    currency = results["data"][0] # At the 0th index, otherise we'd be looping through each and every index

    rank = currency["rank"]
    name = currency["name"]
    symbol = currency["symbol"]

    circulating_supply = int(currency["circulating_supply"])
    total_supply = int(currency["total_supply"])

    quotes = currency["quotes"][convert]  # Name the nest
    market_cap = quotes["market_cap"]
    hour_change = quotes["percent_change_1h"]
    day_change = quotes["percent_change_24h"]
    week_change = quotes["percent_change_7d"]

    price = quotes["price"]
    volume = quotes["volume_24h"]

    volume_string = "{:,}".format(volume)
    market_cap_string = "{:,}".format(market_cap)
    circulating_supply_string = "{:,}".format(circulating_supply)
    total_supply_string = "{:,}".format(total_supply)

    print("\n")
    print(str(rank) + ": " + name + " (" + symbol + ")")
    print("Market cap: \t\tR " + market_cap_string)
    print("Price: \t\t\tR " + str(price))
    print("24h Volume: \t\tR " + volume_string)
    print("Hour change: \t\t" + str(hour_change) + "%")
    print("Day change: \t\t" + str(day_change) + "%")
    print("Week change: \t\t" + str(week_change) + "%")
    print("Total supply: \t\t" + total_supply_string)
    print("Circulating supply: \t" + circulating_supply_string)
    print("Percentage of coins in circulation: " + str(int(circulating_supply / total_supply * 100)))

    choice = input("Again? (y/n)")

    if choice == "n":
        break
