import requests 

API_KEY = "fca_live_1dzVIZIaxZ5lPEWmv0b4V6E82Xjnrp860DU9bDS4"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["CAD", "USD", "EUR", "AUD", "CNY", "GBP", "JPY", "CHF", "HKD", "SEK", "NOK", "SGD", "MXN", "PLN", "DKK", "NZD", "CZK", "HUF", "ZAR", "THB", "ILS", "RUB", "TRY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None

while True:
    base = input("Enter the base currency (q to quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

    #return the currency the user wants and an option to list them all out.
    #Upload to GitHub when finished and add a readme.