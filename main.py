from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

options.use_chromium = True
options.add_argument("--user-data-dir=C:/selenium_profile")
options.add_argument("--profile-directory=Profile 1")

options.add_argument("--headless")

service = Service(executable_path= 'C:\\Users\\___\\Desktop\\Напоминалка\\chromedriver\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service,options=options)

driver.get(url="https://web.telegram.org/a/#___")
sleep(1)
driver.find_element("xpath",'//*[@id="editable-message-text"]').send_keys("Напоминалка про дз")
driver.find_element("xpath",'//*[@id="editable-message-text"]').send_keys(Keys.RETURN)

sleep(15)
driver.close()
driver.quit()
