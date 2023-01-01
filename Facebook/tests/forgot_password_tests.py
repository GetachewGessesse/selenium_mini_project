import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Facebook.base_test.forgot_password_locators import *

def test_forgotPassword_invalid_email():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, forot_password_location).click()
    time.sleep(1)
    forgot_password_page = driver.title
    assert "Can't Log In" in forgot_password_page
    driver.find_element(By.ID, forgot_password_email_field).send_keys("huteh.com")
    time.sleep(3)
    driver.find_element(By.ID, forgot_password_search_button).click()
    time.sleep(3)
    error = driver.find_element(By.XPATH, forgot_password_error_message).text
    assert error == "No Search Results"
    driver.close()

def test_forgotPassword_valid_phone():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, forot_password_location).click()
    time.sleep(1)
    forgot_password_page = driver.title
    assert "Can't Log In" in forgot_password_page
    driver.find_element(By.ID, forgot_password_email_field).send_keys("+251942188980")
    time.sleep(3)
    driver.find_element(By.ID, forgot_password_search_button).click()
    time.sleep(3)
    new_window_message = driver.find_element(By.TAG_NAME, "h2").text
    print(new_window_message)
    time.sleep(3)
    assert new_window_message == "Reset Your Password"
    driver.close()


def test_forgotPassword_null_email():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, forot_password_location).click()
    time.sleep(1)
    forgot_password_page = driver.title
    assert "Can't Log In" in forgot_password_page
    driver.find_element(By.ID, forgot_password_email_field).send_keys("")
    time.sleep(3)
    driver.find_element(By.ID, forgot_password_search_button).click()
    time.sleep(3)
    error = driver.find_element(By.XPATH, forgot_password_error_message).text
    assert error == "No Search Results"
    driver.close()
