from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

json_file = os.path.join(os.path.dirname(__file__), "config.json")
with open(json_file) as json_data_file:
    data = json.load(json_data_file)

USERNAME = "2092006504"
PASSWORD = "#7!M#P!84o9b"

def login(domain_name):
    driver.get(domain_name)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["account_demo"]))).click()
    print("- Open browser and login with demo account")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["username"]))).send_keys(USERNAME)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["password"]))).send_keys(PASSWORD)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["login_btn"]))).click()
    print("-> Input user ID, password and click button Login")
