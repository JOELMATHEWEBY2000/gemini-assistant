import requests


def get_bitcoin_price():

    url = "https://api.coincap.io/v2/assets/bitcoin"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        usd = float(data["data"]["priceUsd"])

        return f"""
Current Bitcoin Price

USD : ${usd:,.2f}
"""

    except Exception as e:

        return f"Bitcoin API Error: {e}"