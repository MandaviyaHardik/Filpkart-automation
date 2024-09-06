import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH,"//div[@class='H6-NpN _3N4_BX']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='New to Flipkart? Create an account']").click()
driver.find_element(By.CSS_SELECTOR,"input[class='r4vIwl BV+Dqf']").send_keys("9426736080")
driver.find_element(By.CSS_SELECTOR,"button[class='QqFHMw twnTnD _7Pd1Fp']").click()

#Enter OTP manually
time.sleep(20)

driver.find_element(By.CSS_SELECTOR,"button[class='QqFHMw twnTnD _7Pd1Fp']").click()  #click on sign in

time.sleep(20)
driver.quit()


