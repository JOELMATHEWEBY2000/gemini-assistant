import requests


def get_bitcoin_price():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd,inr"
    }

    response = requests.get(url, params=params)

    data = response.json()

    usd = data["bitcoin"]["usd"]
    inr = data["bitcoin"]["inr"]

    return f"""Current Bitcoin Price

USD : ${usd}

INR : ₹{inr}
"""