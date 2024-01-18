import pytest
import time
from selenium import webdriver

@pytest.fixture
def driver_carnival():
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()
    # Get the Carnival web page
    driver.get('https://www.carnival.com/')
    # Maximize web page
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver

    # Quit the driver and close every associated window after each test
    driver.quit()


@pytest.fixture
def driver_carnival_cruise():
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()
    # Get the Carnival web page
    driver.get('https://www.carnival.com/cruise-search?pageNumber=1&numadults=2&dest=BH&durdays=6,7,8,9&pagesize=8&sort=fromprice&showBest=true&async=true&currency=USD&locality=1')
    # Maximize web page
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver

    # Quit the driver and close every associated window after each test
    driver.quit()