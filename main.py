from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

date = datetime.datetime.now()

username = "jmeno"
password = "heslo"

if date.month == 12 and 1 <= date.day <= 24:
    print("Datum je v rozmezí adventního kalendáře.")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path='/etc/drivers/chromedriver', options=chrome_options)

    driver.get('https://leosight.cz/')

    driver.find_element_by_id('login-username').send_keys(username)
    driver.find_element_by_id('login-password').send_keys(password)
    driver.find_element_by_id('up-login').click()

    advent_url = 'https://leosight.cz/advent'
    driver.get(advent_url)

    driver.execute_script('Advent();')

    driver.quit()
else:
    print("Datum není v rozmezí adventního kalendáře.")