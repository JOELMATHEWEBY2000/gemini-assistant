import requests

from config import ALPHA_VANTAGE_API_KEY


def get_bitcoin_price():

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "BTC",
        "to_currency": "USD",
        "apikey": ALPHA_VANTAGE_API_KEY
    }

    try:

        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        if "Realtime Currency Exchange Rate" not in data:
            return f"API Error: {data}"

        exchange = data["Realtime Currency Exchange Rate"]

        price = exchange["5. Exchange Rate"]

        return f"""
Current Bitcoin Price

USD : ${float(price):,.2f}
"""

    except Exception as e:

        return f"Bitcoin API Error: {e}"