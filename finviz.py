from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to scrape symbols from Finviz
def finviz():
    """
    Scrapes stock symbols from the Finviz screener using Selenium. 
    Filters for stocks based on specific criteria defined in the Finviz screener URL.

    Returns:
        list: A list of stock symbols scraped from Finviz.

    Raises:
        Exception: If there are issues with the Selenium WebDriver or page scraping.
    """
    finviz_url = 'https://finviz.com/screener.ashx?v=111&f=cap_largeover%2Csh_avgvol_o2000%2Csh_curvol_o5000%2Cta_highlow52w_a0to10h&ft=4&o=-volume'
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options)
    driver.get(finviz_url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.screener-pages')))
    page_button_els = driver.find_elements(By.CSS_SELECTOR, '.screener-pages')
    if len(page_button_els) < 2:
        last_page_number = 1
    else:
        last_page_number = int(page_button_els[-2].text)

    # Generate URLs for all pages
    urls = [f"{finviz_url}&r={i}" for i in range(1, last_page_number * 20 + 1, 20)]
    symbols = []

    for url in urls:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#screener-table .tab-link')))
        symbol_els = driver.find_elements(By.CSS_SELECTOR, '#screener-table .tab-link')
        symbols.extend(el.text.lower() for el in symbol_els)

    driver.quit()
    return symbols