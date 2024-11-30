"""Implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins,n,
  that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit 
  with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
  which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
Be sure to catch any exceptions, as with code like:"""

import sys
import requests

def main():
    # Check for a valid command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        # Convert the argument to a float
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Please provide a valid number of Bitcoins.")

    # Fetch the current Bitcoin price in USD
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")

    # Calculate total cost
    total_cost = bitcoins * price_per_bitcoin

    # Output the result with thousands separator and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()