import yfinance as yf
import numpy as np

def get_exchange_rate(base_currency, target_currency):
    """
    Fetches the current exchange rate for a given currency pair.

    Args:
        base_currency (str): The base currency (e.g., USD, EUR, JPY).
        target_currency (str): The target currency (e.g., USD, EUR, JPY).

    Returns:
        float: The current exchange rate.
    """
    if base_currency == target_currency:
        return 1.0
    ticker = f"{base_currency}{target_currency}=X"
    data = yf.download(ticker, period="1d")
    return data["Close"][-1]

def generate_arrays(currencies):
    """
    Generates the node_names and weights arrays based on a list of currencies.

    Args:
        currencies (list): A list of currency codes (e.g., USD, EUR, JPY).

    Returns:
        tuple: A tuple containing the node_names and weights arrays.
    """
    node_names = currencies
    weights = [[0 for _ in range(len(currencies))] for _ in range(len(currencies))]

    for i, base_currency in enumerate(currencies):
        for j, target_currency in enumerate(currencies):
            rate = get_exchange_rate(base_currency, target_currency)
            weight = np.log(rate)
            weights[i][j] = weight

    return node_names, weights

def main():
    # Define the list of currencies
    currencies = ['USD', 'EUR', 'JPY', 'GBP']

    # Generate the node_names and weights arrays
    node_names, weights = generate_arrays(currencies)

    # Print the results
    print("node_names:", node_names)
    print("weights:")
    for row in weights:
        print(row)
        
    return node_names, weights

if __name__ == "__main__":
    main()