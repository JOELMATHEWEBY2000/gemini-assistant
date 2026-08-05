import requests


def get_bitcoin_price():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd,inr"
    }

    try:

        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        print(data)      # Check Render logs

        if "bitcoin" not in data:
            return f"CoinGecko API Error: {data}"

        usd = data["bitcoin"].get("usd", "N/A")
        inr = data["bitcoin"].get("inr", "N/A")

        return f"""
Current Bitcoin Price

USD : ${usd}

INR : ₹{inr}
"""

    except requests.exceptions.RequestException as e:

        return f"Network Error: {e}"

    except Exception as e:

        return f"Error: {e}"