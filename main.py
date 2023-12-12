from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

username = "jmeno" # Uživatelské jméno
password = "heslo" # Heslo

date = datetime.datetime.now()

if date.month == 12 and 1 <= date.day <= 24:
    print("Datum je v rozmezí adventního kalendáře.")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path='/etc/drivers/chromedriver', options=chrome_options)

    login_url = 'https://leosight.cz/prihlaseni'
    driver.get(login_url)

    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()

    advent_url = 'https://leosight.cz/advent'
    driver.get(advent_url)

    driver.execute_script('Advent();')

    driver.quit()
else:
    print("Datum není v rozmezí adventního kalendáře.")
