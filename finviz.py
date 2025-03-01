from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def finviz():
    finviz_url = 'https://finviz.com/screener.ashx?v=111&f=cap_largeover%2Csh_avgvol_o2000%2Csh_curvol_o5000%2Cta_highlow52w_a0to10h&ft=4&o=-volume'
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options) 
    driver.get(finviz_url)
    time.sleep(3)

    page_button_els = select(driver, '.screener-pages')
    last_page_number = int(page_button_els[-2].text)
    url_rep_of_page_numbers = []
    for i in range(1, (last_page_number)*20+1, 20):
        url_rep_of_page_numbers.append(i)
    urls = []
    for number in url_rep_of_page_numbers:
        urls.append(finviz_url+f'&r={number}')
    symbols = []
    for url in urls:
        driver.get(url)
        time.sleep(3)
        symbol_els = select(driver, '#screener-table .tab-link')
        for el in symbol_els:
            symbols.append(el.text.lower())
    return symbols

def select(driver, cssSelector):
    return driver.find_elements(By.CSS_SELECTOR, cssSelector)