import requests 

API_KEY = ~
BASE_URL = ~

CURRENCIES = ["CAD", "USD", "EUR", "AUD", "CNY", "GBP", "JPY", "CHF", "HKD", "SEK", "NOK", "SGD", "MXN", "PLN", "DKK", "NZD", "CZK", "HUF", "ZAR", "THB", "ILS", "RUB", "TRY"]

currencies = ",".join(CURRENCIES)

def get_exchange_rates(base):
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"]
    except Exception as E:
        print("Error retriving data: {e}")
        return None

while True:
    base = input("Enter the base currency (q to quit): ").upper()
    
    if base == "Q":
        break

    if base not in CURRENCIES:
        print(f"Invalid base currency, please try again")
        continue

    while True:
        target_currency = input("Enter the currency you want to convert to (type 'ALL' to see every conversion): ").upper()
        
        if target_currency == "ALL":
            break

        if target_currency not in CURRENCIES:
            print(f"Invalid currency type")
            continue
        
        if target_currency == base:
            print(f"Currency cannot be the same as the base currency")
            continue
        break

    data = get_exchange_rates(base)
    if not data:
        continue

    del data[base]
    if target_currency in data:
        print(f"1.00 {base} = {data[target_currency]:.2f} {target_currency}")
    elif target_currency == "ALL":
        for ticker, value in data.items():
            print(f"{ticker}: {value:.2f}")
    else:
        print(f"Could not retrive exchange rate for {target_currency}")
