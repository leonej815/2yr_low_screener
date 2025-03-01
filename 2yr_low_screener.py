# if broken update yfinance
# pip install yfinance --upgrade --no-cache-dir 
from finviz import finviz
from yahoo import yahoo
import pandas as pd
from datetime import date

symbols = finviz()
filtered_symbols = yahoo(symbols)
df = pd.DataFrame(filtered_symbols, columns=[date.today()])
df.to_csv('symbols.csv', index=False)