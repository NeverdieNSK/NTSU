from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import secret

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver. get('https://dispace.edu.nstu.ru')
driver.implicitly_wait(5)
btn = driver.find_element_by_css_selector ('div.input-field>a')
btn.click()
driver.implicitly_wait(10)
login = driver.find_element_by_name('callback_0')
driver.implicitly_wait(10)
login.send_keys(secret.login)
driver.implicitly_wait(10)
password = driver.find_element_by_name('callback_1')
password.send_keys(secret.password)
driver.implicitly_wait(10)
button = driver.find_element_by_name('callback_2')
button.click()
driver.implicitly_wait(10)
