
"""
Now we want to access the ticker endpoint, where we can only access 100 results at a time
(Check the parameters on the website)
We'll be using it in an array format so that we can loop through the data with ease

Ticker data is LIVE price data so essentially we'll be looking at the current value of these currencies
"""

import json
import requests

while True:

    ticker_url = "https://api.coinmarketcap.com/v2/ticker/?structure=array"  # This is to get the data as an array

    # Ask the user if they want to enter any of their own parameters
    limit = 100
    start = 1
    sort = "rank"
    convert = "ZAR"

    choice = input("Do you want to enter any custom parameters? (y/n): ")

    if choice == "y":
        limit = input("What is the custom limit?: ")
        start = input("What is the custom start number?: ")
        sort = input("What do you want to sort by?: ")
        convert = input("What is your local currency?: ")

    ticker_url += "&limit=" + str(limit) + "&sort=" + sort + "&start=" + str(start) + "&convert="


    request = requests.get(ticker_url)
    results = request.json()

    print(json.dumps(results, sort_keys=True, indent=4))

    # Store all these values
    data = results["data"]

    for currency in data:
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
        print("Percentage of coins in circulation: " + str(int(circulating_supply/total_supply * 100)))

    choice = input("Again? (y/n)")

    if choice == "n":
        break
