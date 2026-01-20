from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['MOZ_HEADLESS_WIDTH'] = '1920'
os.environ['MOZ_HEADLESS_HEIGHT'] = '1080'
TOKEN = os.getenv("TOKEN")
def start_selenium_driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--no-sandbox")

    driver = webdriver.Firefox(options=firefox_options)
    print("Driver iniciado em modo headless.")
    return driver

def interact_with_page(driver):
    driver.get("https://totp.danhersam.com/")
    
    # Preencher o primeiro campo
    first_field = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.field:nth-child(2) > div:nth-child(2) > input:nth-child(1)"))
    )
    first_field.clear()
    first_field.send_keys(TOKEN)
    time.sleep(5)

    # Alterar o terceiro campo para 60
    third_field = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.field:nth-child(4) > div:nth-child(2) > input:nth-child(1)"))
    )
    third_field.clear()
    third_field.send_keys("60")
    time.sleep(2)

def get_token(driver):
    token = driver.find_element(By.CSS_SELECTOR, "#token").text
    print("Código gerado:", token)
    return token

def close_driver(driver):
    driver.quit()
    print("Driver fechado.")
