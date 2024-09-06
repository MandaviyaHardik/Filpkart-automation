import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for Products, Brands and More']").send_keys("cooker")
driver.find_element(By.CSS_SELECTOR,"svg[width='24']").click()
driver.find_element(By.CSS_SELECTOR,"a[title='BAJAJ 2 L, 3 L, 5 L Inner Lid Pressure Cooker']").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])

time.sleep(10)
driver.find_element(By.CSS_SELECTOR,"button[class='QqFHMw vslbG+ In9uk2']").click()
time.sleep(100)
