# Stock Symbol Screener

This project is a stock symbol screener that scrapes stock data from [Finviz](https://finviz.com/) and filters the results based on specific criteria using historical price data from [Yahoo Finance](https://finance.yahoo.com/). The filtered symbols are saved to a CSV file for further analysis.

## Features

- **Scrape Stock Symbols**: Retrieves stock symbols from Finviz that meet predefined criteria.
- **Filter Symbols**: Uses Yahoo Finance to filter symbols based on:
  - The latest price.
  - The two-year low.
  - A percentage difference threshold.
- **Save Results**: Outputs the filtered stock symbols to a CSV file with a timestamped column.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.7 or higher
- [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://chromedriver.chromium.org/)
- Required Python libraries (see below)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/stock-symbol-screener.git
   cd stock-symbol-screener
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: If `yfinance` is broken, you can update it using:
   ```bash
   pip install yfinance --upgrade --no-cache-dir
   ```

3. Ensure that ChromeDriver is installed and added to your system's PATH.

## Usage

1. Run the script:
   ```bash
   python fetch_stock_symbols.py
   ```

2. The script will:
   - Scrape stock symbols from Finviz.
   - Filter the symbols using Yahoo Finance.
   - Save the filtered symbols to a CSV file named `symbols.csv` in the current directory.

   Example of the CSV file structure:
   ```
   2025-05-10
   symbol1
   symbol2
   ...
   ```

## How It Works

1. **Finviz Scraping**:
   - The `finviz()` function uses Selenium to scrape stock symbols from Finviz.
   - It iterates through all pages of results and collects symbols.

2. **Yahoo Finance Filtering**:
   - The `yahoo()` function filters symbols based on:
     - The last closing price.
     - The two-year low.
     - A percentage difference threshold (< 7.5%).
   - Historical price data is fetched using the `yfinance` library.

3. **Save to CSV**:
   - The filtered symbols are saved to `symbols.csv` with the current date as the column header.

## Notes

- **Selenium**: Ensure your ChromeDriver version matches your Google Chrome browser version.
- **Rate Limits**: Yahoo Finance may enforce rate limits on API calls. Use batching or introduce delays if you encounter issues.
- **Error Handling**: The script includes basic error handling for missing data or network issues.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.