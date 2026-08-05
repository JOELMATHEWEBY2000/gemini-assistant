import requests


def get_bitcoin_price():

    url = "https://api.binance.com/api/v3/ticker/price"

    params = {
        "symbol": "BTCUSDT"
    }

    try:

        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        usd = float(data["price"])

        return f"""
Current Bitcoin Price

USD : ${usd:,.2f}
"""

    except Exception as e:

        return f"Bitcoin API Error: {e}"