import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Facebook.base_test.login_locators import *

def test_login_valid_pass_and_user():
    driver = webdriver.Edge()
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("0559477424")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("david16#")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(20)
    home_url = driver.current_url
    assert home_url == homepage_url

def test_login_valid_email_or_username_and_invalid_password():
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("0559477424")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("hdfgre")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(10)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Invalid username or password"

def test_login_invalid_email_or_username_and_invalid_password():
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("05594774")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("hdfgre")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(20)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Invalid username or password"


def test_login_invalid_email_or_username_and_valid_password():
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("05594uwde")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("david16#")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(20)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Invalid username or password"



def test_login_null_email_or_username_and_null_password():
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(20)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Invalid username or password"


def test_login_null_email_or_username_and_valid_password():
    driver = webdriver.Chrome
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("david16#")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(20)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Invalid username or password"


def test_login_valid_email_or_username_and_null_password():
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element(By.ID, email_field_id)
    username.clear()
    username.send_keys("0559477424")
    password = driver.find_element(By.ID, password_field_id)
    password.clear()
    password.send_keys("")
    driver.find_element(By.NAME, login_button_name).click()
    time.sleep(20)
    error = driver.find_element(By.XPATH, error_message).text
    assert error == "Invalid username or password"
