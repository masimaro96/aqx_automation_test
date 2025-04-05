from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from base_page import *
import json
import os

json_file = os.path.join(os.path.dirname(__file__), "config.json")

with open(json_file) as json_data_file:
        data = json.load(json_data_file)

def order_page(side="buy",size=None, stop_loss=None, take_profit=None): 
    if side == "buy":
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["buy_order"]))).click()
    else:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["sell_order"]))).click()
    if size:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["size"]))).send_keys(size)
    if stop_loss:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["stop_loss"]))).send_keys(stop_loss)
    if take_profit:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["take_profit"]))).send_keys(take_profit)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"]))).click()

        