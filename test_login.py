from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

USERNAME = "hiteshidhandare_voN01l"
ACCESS_KEY = "n1ea2xSgYUhPHocGi8Nx"

options = Options()
options.set_capability("browserName", "Edge")
options.set_capability("browserVersion", "latest")
options.set_capability("os", "Windows")
options.set_capability("osVersion", "10")
options.set_capability("name", "Swag Labs Login Test")

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    options=options
)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(5)

print("Test completed on BrowserStack")

driver.quit()
