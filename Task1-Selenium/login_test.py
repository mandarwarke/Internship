import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
chrome_driver_path = "D:\\Task1-Selenium\\chromedriver-win64\\chromedriver.exe"

@pytest.fixture(scope="session")
def driver():
    """ Setup Chrome WebDriver (Runs once per session) """
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver  # Provide the driver to the test function
    driver.quit()  # Close browser at the end of the test session

def test_login_and_navigation(driver):
    """ Perform login and navigation in one test session """
    
    # Open website
    driver.get("https://www.saucedemo.com/")
    print("Opened SauceDemo")

    # Perform login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Logged in")

    # Wait for menu button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
    print("Opened menu")

    # Click on 'All Items' link
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))).click()
    print("Navigated to inventory page")

    # Verify navigation
    assert "inventory" in driver.current_url
    print("Navigation successful!")
