import sys
import time
import os
import logging

from app.browser import PersonaForm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PyQt5 import QtWidgets
from dotenv import load_dotenv

from app.interface import Head

def load_config(conf):
    basedir = os.path.abspath(os.getcwd())
    load_dotenv(os.path.join(basedir, 'config.txt'))
    conf['login'] = os.environ.get('login')
    conf['password'] = os.environ.get('password')

def autorizathion(driver, config):
    driver.get("https://simbase.0793.ru/")
    login = driver.find_element(By.ID, 'loginform-username')
    login.clear()
    login.send_keys(config['login'])
    password = driver.find_element(By.ID, 'loginform-password')
    password.clear()
    password.send_keys(config['password'])
    submit = driver.find_element(By.NAME, 'login-button')
    submit.click()

    while "Позвони маме" not in driver.title:
        time.sleep(1)

    driver.get("https://simbase.0793.ru/pirsdata/areg")

def start_interface(driver):
    app = QtWidgets.QApplication(sys.argv)
    window = Head(driver)
    window.setWindowTitle("Автоматизированная подача симок")
    window.setFixedSize(200, 200)
    window.show()
    sys.exit(app.exec_())

def create_app():
    logging.basicConfig(level=logging.INFO, filename="autosim_log.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    config = {}
    load_config(config)
    driver = webdriver.Chrome()
    autorizathion(driver, config)
    start_interface(driver)

