# Author: Simran Shaikh
# Topic: Selenium Test – Open Web Page & Verify Title

from selenium import webdriver
import allure
import pytest

# Test Case: Verify page opens successfully using Selenium
@allure.title("Verify that we are able to open a page by using Selenium.")
@allure.description("We will open a page and verify that it is getting opened by using Selenium.")
def test_first_tc():
    driver = webdriver.Edge()  # Step 1: Launch Edge browser
    driver.get("https://thetestingacademy.com")  #Step 2: Open the target URL
    print(driver.title) # Step 3: Fetch and print page title
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"
    # Step 4: Validate page title using assertion
    driver.quit() #Step 5: Close the browser
