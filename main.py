from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("https://mycutebaby.in/contest/participant/6322b11ec1b02?utm_source=wsapp_share&utm_campaign=September_2022&utm_medium=shared&utm_term=wsapp_shared_6322b11ec1b02&utm_content=participant")
driver.find_element(By.XPATH, "//input[@id='v']").send_keys("Yash")
driver.find_element(By.ID, "vote_btn").click()
