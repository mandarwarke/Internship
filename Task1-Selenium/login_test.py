import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r"D:\Task1-Selenium\chromedriver-win64\chromedriver.exe"

print("Starting script...")  

@pytest.fixture(scope="session")
def driver():
    """ Setup Chrome WebDriver (Runs once per session) """
    print("Initializing ChromeDriver...")
    service = Service(chrome_driver_path)
    
    try:
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        print("ChromeDriver started successfully!")
    except Exception as e:
        print(f"Error starting ChromeDriver: {e}")
        return None  # Return None if ChromeDriver fails
    
    yield driver
    print("Closing ChromeDriver...")
    driver.quit()

def test_login_and_navigation():
    """ Perform login and navigation in one test session """
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    print("Opening SauceDemo website...")
    driver.get("https://www.saucedemo.com/")
    
    try:
        print("Entering username...")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

        print("Entering password...")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        print("Clicking login button...")
        driver.find_element(By.ID, "login-button").click()

        print("Waiting for menu button...")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()

        print("Clicking 'All Items'...")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))).click()

        print("Checking navigation success...")
        assert "inventory" in driver.current_url
        print("Navigation successful!")

    except Exception as e:
        print("Error occurred:", e)
    
    driver.quit()  # Close the browser

# **Manually Call the Function**
if __name__ == "__main__":
    test_login_and_navigation()

print("Script execution completed.") 
