import yfinance as yf
symbols = ['f']
def yahoo(symbols):
    return_symbols = []
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        last_price = get_last_price(ticker)
        if last_price == None:
            continue
        two_year_low = get_two_year_low(ticker)
        pct_diff = get_pct_diff(last_price, two_year_low)
        if pct_diff < 7.5:
            return_symbols.append(symbol)
    return return_symbols

def get_pct_diff(num1, num2):
    return abs(num1-num2) / ((num1+num2)/2) * 100

def get_two_year_low(ticker):
    df = ticker.history(period='2y', interval='3mo')
    return df['Low'].min()

def get_last_price(ticker):
    df = ticker.history(period='1d', interval='1d')
    if len(df) < 1:
        return None
    else:
        return df['Close'][0]
