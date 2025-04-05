import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from framework import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import driver, data

def order_page_buy(): 
    # Buy Market Order
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["all_symbols"]))).click()
    # Input volumn
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["size"]))).send_keys("0.01")
    print("-> Input volume")
    # Input stop loss
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["stop_loss"]))).send_keys("1.1000")
    print("-> Input stop loss")
    # Input take profit     
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["take_profit"]))).send_keys("1.2000")
    print("-> Input take profit")
    # Click Buy Market
    button_trade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"])))
    # Check if the button is disabled
    if button_trade.get_attribute("disabled"):
        print("Market order button is disabled")
    else:
        print("Market order button is enabled")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"]))).click()
        print("-> Click Buy Market button")

        try:
            # Validate the order placed details
            positions_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody[contains(@data-testid, 'asset-open-list')]")))
            if "Buy" in positions_table.text:
               print("-> Market order 'Buy' has been placed and is displayed in the list of open positions.!")
            else:
               print("-> The order 'Buy' is not visible in the Positions table!")
        except:
             print("-> Can't find Positions Table!")

def order_page_sell():
    # Sell Market Order
    # Input volumn
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["size"]))).send_keys("0.01")
    print("-> Input volume")
    # Input stop loss
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["stop_loss"]))).send_keys("1.1000")
    print("-> Input stop loss")
    # Input take profit
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["take_profit"]))).send_keys("1.2000")
    print("-> Input take profit")
    # Click Sell Market
    # Check if the button is disabled
    button_trade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"])))
    if button_trade.get_attribute("disabled"):
        print("Market order button is disabled")
    else:
        print("Market order button is enabled")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"]))).click()
        print("-> Click Sell Market button")
        try:
            # Validate the order placed details
            positions_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody[contains(@data-testid, 'asset-open-list')]")))
            if "Sell" in positions_table.text:
                print("-> Market order 'Sell' has been placed and is displayed in the list of open positions.!")
            else:
                print("-> The order 'Sell' is not visible in the Positions table!")
        except:
            print("-> Can't find Positions Table!")     