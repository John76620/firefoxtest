# Generated by Selenium IDE
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class syscoinBot():
    def quit(self):
        self.driver.quit()
  
    def mine(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.driver.get("https://faucet.syscoin.org/")
        print("Connecté !")
        self.driver.find_element(By.ID, "address").click()
        self.driver.find_element(By.ID, "address").send_keys("sys1qg892etwe6ankkq7lqfj5ftgd36td8h05jjr7pa")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def already_mined(self):
        if self.driver.current_url != "https://faucet.syscoin.org/mine":
            print("IP déjà utilisée !")
            self.quit()
        else:
            while (self.driver.current_url == "https://faucet.syscoin.org/mine"):
                pass
            print("Minage réussi !")
            self.driver.implicitly_wait(3)
            self.quit()
