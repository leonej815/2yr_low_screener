import yfinance as yf

# Function to filter symbols using Yahoo Finance
def yahoo(symbols):
    """
    Filters stock symbols based on their latest price, two-year low, 
    and the percentage difference between the two, using Yahoo Finance data.

    Args:
        symbols (list): A list of stock symbols to filter.

    Returns:
        list: A list of stock symbols that meet the filtering criteria.

    Filtering Criteria:
        - The percentage difference between the last price and the two-year low is less than 7.5%.

    Raises:
        Exception: If there are issues fetching data from Yahoo Finance.
    """
    return_symbols = []
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            last_price = get_last_price(ticker)
            if last_price is None:
                continue
            two_year_low = get_two_year_low(ticker)
            pct_diff = get_pct_diff(last_price, two_year_low)
            if pct_diff < 7.5:
                return_symbols.append(symbol)
        except Exception as e:
            print(f"Error processing symbol {symbol}: {e}")
    return return_symbols

# Utility function to calculate percentage difference
def get_pct_diff(num1, num2):
    """
    Calculates the percentage difference between two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The percentage difference between the two numbers.
    """
    return abs(num1 - num2) / ((num1 + num2) / 2) * 100

# Utility function to get two-year low
def get_two_year_low(ticker):
    """
    Retrieves the two-year low for a stock using its historical data.

    Args:
        ticker (yfinance.Ticker): The Yahoo Finance Ticker object for the stock.

    Returns:
        float: The two-year low of the stock's price.
    """
    df = ticker.history(period='2y', interval='3mo')
    return df['Low'].min()

# Utility function to get last closing price
def get_last_price(ticker):
    """
    Retrieves the last closing price for a stock.

    Args:
        ticker (yfinance.Ticker): The Yahoo Finance Ticker object for the stock.

    Returns:
        float: The last closing price of the stock.
        None: If no historical data is available.
    """
    df = ticker.history(period='1d', interval='1d')
    if len(df) < 1:
        return None
    else:
        return df['Close'].iloc[0]