from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import login_page
from base_page import *
from login_page import Logging


def MyExecution(domain_name):
    error_menu = []

    try:
        login_page().login(domain_name)
    except:
        Logging("Cannot continue execution")
        error_menu.append("login_page")

def My_Execution(domain_name):
    login_page.login(domain_name)

My_Execution("https://aqxtrader.aquariux.com/web/login")

    