from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import login_page, trade_page
from framework import *


def My_Execution(domain_name):
    login_page.login(domain_name)
    trade_page.order_page_buy()
    trade_page.order_page_sell()
    trade_page.order_page_type_random()

My_Execution("https://aqxtrader.aquariux.com/web")

    