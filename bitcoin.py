import requests
from config import TWELVEDATA_API_KEY


def get_bitcoin_price():

    url = "https://api.twelvedata.com/price"

    params = {
        "symbol": "BTC/USD",
        "apikey": TWELVEDATA_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "price" not in data:
            return f"API Error: {data}"

        return f"""Current Bitcoin Price

USD : ${float(data['price']):,.2f}
"""

    except Exception as e:
        return f"Bitcoin API Error: {e}"