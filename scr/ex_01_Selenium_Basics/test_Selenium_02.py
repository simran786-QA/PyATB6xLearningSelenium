###from selenium import webdriver
#import allure
#import pytest


#@allure.title("Verify that we are able to open a page by using Selenium.")
#@allure.description("We will open a page and verify that it is getting opened by using Selenium.")
#def test_first_tc():
    # Selenium 3 - Not much used now
    # driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path=driver_path)
    # driver = webdriver.Edge()
    #driver.get("https://thetestingacademy.com")
    #print(driver.title)
    #assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    # -------------------------------------------------------------
    # Author: Simran Shaikh
    # Topic: Opening a Website Using Selenium with Pytest & Allure
    # -------------------------------------------------------------

    # -------------------------------------------------------------
    # Step 1: Import Required Libraries
    # -------------------------------------------------------------

    # Selenium WebDriver is used to automate browsers
    from selenium import webdriver

    # Allure is used for advanced reporting
    import allure

    # Pytest is the testing framework used to execute test cases
    import pytest

    # -------------------------------------------------------------
    # Step 2: Add Allure Title
    # -------------------------------------------------------------

    # This title will appear in the Allure report
    @allure.title("Verify that website opens successfully using Selenium")
    # -------------------------------------------------------------
    # Step 3: Add Allure Description
    # -------------------------------------------------------------

    # Description explains what this test case is doing
    @allure.description(
        "This test opens TheTestingAcademy website "
        "and verifies the page title."
    )
    # -------------------------------------------------------------
    # Step 4: Create Test Case Function
    # -------------------------------------------------------------

    # Pytest identifies functions starting with 'test_' as test cases
    def test_first_tc():
        # ---------------------------------------------------------
        # Step 5: Launch Edge Browser
        # ---------------------------------------------------------

        # Selenium 4 automatically manages browser drivers
        driver = webdriver.Edge()

        # ---------------------------------------------------------
        # Step 6: Open Website URL
        # ---------------------------------------------------------

        # get() method is used to open a website in browser
        driver.get("https://thetestingacademy.com")

        # ---------------------------------------------------------
        # Step 7: Fetch and Print Page Title
        # ---------------------------------------------------------

        # driver.title gets the current page title
        actual_title = driver.title

        print("Website Title:", actual_title)

        # ---------------------------------------------------------
        # Step 8: Expected Title
        # ---------------------------------------------------------

        # Expected title used for validation
        expected_title = (
            "TheTestingAcademy | Learn Software Testing and Automation Testing"
        )

        print("Expected Title:", expected_title)

        # ---------------------------------------------------------
        # Step 9: Validation Using Assertion
        # ---------------------------------------------------------

        # Assertion checks whether actual and expected values match
        assert actual_title == expected_title

        # ---------------------------------------------------------
        # Step 10: Close Browser
        # ---------------------------------------------------------

        # Closes the browser after execution
        driver.quit()

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------

    # 1. Imported Selenium, Allure, and Pytest libraries
    # 2. Added reporting title and description using Allure
    # 3. Opened Edge browser using Selenium
    # 4. Opened TheTestingAcademy website
    # 5. Captured website title
    # 6. Compared actual vs expected title
    # 7. Assertion validates whether the test passes or fails
    # 8. Closed browser after test execution