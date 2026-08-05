import requests


def get_bitcoin_price():

    url = "https://min-api.cryptocompare.com/data/price"

    params = {
        "fsym": "BTC",
        "tsyms": "USD,INR"
    }

    try:

        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        return f"""
Current Bitcoin Price

USD : ${data['USD']}

INR : ₹{data['INR']}
"""

    except Exception as e:

        return f"Bitcoin API Error: {e}"