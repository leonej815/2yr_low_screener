# if broken update yfinance
# pip install yfinance --upgrade --no-cache-dir 
from finviz import finviz
from yahoo import yahoo
import pandas as pd
from datetime import date

if __name__ == "__main__":
    # Step 1: Scrape symbols from Finviz
    symbols = finviz()
    print(f"Collected {len(symbols)} symbols from Finviz.")

    # Step 2: Filter symbols using Yahoo Finance
    filtered_symbols = yahoo(symbols)
    print(f"{len(filtered_symbols)} symbols passed the filter criteria.")

    # Step 3: Save filtered symbols to a CSV file
    today_date = date.today().strftime("%Y-%m-%d")
    df = pd.DataFrame(filtered_symbols, columns=[today_date])
    df.to_csv('symbols.csv', index=False)
    print("Filtered symbols saved to 'symbols.csv'.")