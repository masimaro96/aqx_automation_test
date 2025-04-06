import json
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from framework import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import driver, data

def input_order_details():
    # Input volume
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["size"]))).send_keys("0.01")
    print("-> Input volume")
    # Input stop loss
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["stop_loss"]))).send_keys("1.1000")
    print("-> Input stop loss")
    # Input take profit
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["take_profit"]))).send_keys("1.2000")
    print("-> Input take profit")

def buy_sell_market_order(type_detail):
    # Click Buy Market
    button_trade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"])))
    # Check if the button is disabled
    if button_trade.get_attribute("disabled"):
        print("Market order button is disabled")
    else:
        print("Market order button is enabled")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["submit"]))).click()
        print(f"-> Click '{type_detail}' Market button")

        try:
            # Validate the order placed details
            positions_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody[contains(@data-testid, 'asset-open-list')]")))
            if type_detail in positions_table.text:
               print(f"-> Market order '{type_detail}' has been placed and is displayed in the list of open positions.!")
            else:
               print(f"-> The order '{type_detail}' is not visible in the Positions table!")
        except:
             print("-> Can't find Positions Table!")


def select_random_order_type():
    order_type = random.choice(["Limit", "Stop"])
    
    # Open dropdown menu to select order type
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["order_trade"]["drop_down_order"]))).click()

    # Select order type randomly
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@data-testid='{order_type}']"))).click()

    print(f"Order type selected: {order_type}")
    return order_type

def expiry_random():
    expiry = random.choice(["Good Till Cancelled", "Good Till Day"])
    
    # Open dropdown menu to select order type
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["drop_down_expiry"]))).click()

    # Select order type randomly
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@data-testid='{expiry}']"))).click()

    print(f"Expiry selected: {expiry}")
    return expiry

def order_page_buy(): 
    # Buy Market Order
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["all_symbols"]))).click()
    input_order_details()
    buy_sell_market_order("Buy")
    

def order_page_sell():
    # Sell Market Order
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["trade"]["sell_order"]))).click()
    print("-> Sell Market Order")
    input_order_details()
    buy_sell_market_order("Sell")  


def order_page_type_random():
    # Buy Limit Order
    order_type = select_random_order_type()

    if order_type == "Limit":
        print("-> Buy Limit Order")
        input_order_details()
        expiry_random()
        buy_sell_market_order("Limit")    
    else:
        print("-> Buy Stop Order")
        input_order_details()
        expiry_random()
        buy_sell_market_order("Stop")
    
