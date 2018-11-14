import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = "ZAR"
listings_url = "https://api.coinmarketcap.com/v2/listings/?convert=" + convert
url_end = "?structure=array&convert=" + convert

request = requests.get(listings_url)
results = request.json()
data = results["data"]

# Create dict for specific api call
# Dictionaries are arrays but they store key value pairs
# Ticker symbol as key and id as value
ticker_url_pairs = {}
for currency in data:
    symbol = currency["symbol"]
    url = currency["id"]
    ticker_url_pairs[symbol] = url # Append each to dict

print("\nMy Portfolio\n")

portfolio_value = 0.00 # Double
last_updated = 0 # Timestamp of when last updated

table = PrettyTable(["Asset", "Amount Owned", convert + "Value", "Price", "1h", "24h", "7d"])

with open("portfolio.txt") as input:
    for line in input:
        ticker, amount = line.split(":") # Split name and amount
        ticker = ticker.upper()

        ticker_url = "https://api.coinmarketcap.com/v2/ticker/" + str(ticker_url_pairs[ticker]) + "/" + url_end

        request = requests.get(ticker_url)
        results = request.json()

        currency = results["data"][0] # First index of data array
        rank = currency["rank"]
        name = currency["name"]
        last_updated = currency["last_updated"]
        symbol = currency["symbol"]
        quotes = currency["quotes"][convert]
        hour_change = quotes["percent_change_1h"]
        day_change = quotes["percent_change_24h"]
        week_change = quotes["percent_change_7d"]
        price = quotes["price"]

        value = float(price) * float(amount)

        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + "%" + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + "%" + Style.RESET_ALL

        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + "%" + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + "%" + Style.RESET_ALL

        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + "%" + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + "%" + Style.RESET_ALL


        portfolio_value +=  value

        value_string ="{:,}".format(round(value, 2)) # Decimal every 3rd place and round to 2 decimals

        table.add_row([name + " (" + symbol + ")",
                       amount,
                       "R" + value_string,
                       "R" + str(price),
                       str(hour_change),
                       str(day_change),
                       str(week_change)])
print(table)
portfolio_value_string = "{:,}".format(round(portfolio_value, 2))
last_updated_string = datetime.fromtimestamp(last_updated).strftime("%d %B, %Y at %I:%M%p") # day, month, year, time

print("\nTotal Portfolio Value : " + Back.GREEN + "R " + portfolio_value_string + Style.RESET_ALL)
print("\nAPI Results Last Updated on ", last_updated_string)