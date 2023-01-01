import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from Facebook.base_test.login_locators import *
from Facebook.base_test.registration_locators import *

def test_register_all_valid_data():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, create_new_account_btn).click()
    time.sleep(2)
    driver.find_element(By.NAME, first_name_field).send_keys("jdsh")
    time.sleep(1)
    driver.find_element(By.NAME, last_name_field).send_keys("ayusbcgvb")
    time.sleep(1)
    driver.find_element(By.NAME, registration_email_field).send_keys("getachewayehu77@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, re_enter_email_field).send_keys("getachewayehu77@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, registration_password_field).send_keys("azuta@1234")
    time.sleep(1)
    # day = selecting day dropdown
    month = Select(driver.find_element(By.ID, birthday_option_day))
    # select by visible text
    month.select_by_visible_text('14')
    time.sleep(1)
    # day = selecting month dropdown
    month = Select(driver.find_element(By.ID, birthday_option_month))
    # select by visible text
    month.select_by_visible_text('Feb')
    time.sleep(1)
    # day = selecting year dropdown
    month = Select(driver.find_element(By.ID, birthday_option_year))
    # select by visible text
    month.select_by_visible_text('2000')
    time.sleep(1)
    driver.find_element(By.XPATH, gender_male_radio_btn).click()
    time.sleep(1)

    driver.find_element(By.NAME, sign_up_btn).click()
    time.sleep(120)

    next_window_message = driver.find_element(By.XPATH, confirmation_message )
    assert next_window_message.is_displayed()

def test_register_all_null_data():
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        driver.find_element(By.XPATH, create_new_account_btn).click()
        time.sleep(10)
        driver.find_element(By.NAME, sign_up_btn).click()
        time.sleep(10)

        error_warning_sign = driver.find_element(By.XPATH, error_icon)
        assert error_warning_sign.is_enabled()


def test_all_mandatory_field():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, create_new_account_btn).click()
    time.sleep(2)
    driver.find_element(By.NAME, first_name_field).send_keys("azu")
    time.sleep(1)
    driver.find_element(By.NAME, last_name_field).send_keys("ayehu")
    time.sleep(1)
    driver.find_element(By.NAME, registration_email_field).send_keys("getachewayehu77@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, re_enter_email_field).send_keys("getachewayehu77@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, registration_password_field).send_keys("azuta@1234")
    time.sleep(1)
    # day = selecting day dropdown
    month = Select(driver.find_element(By.ID, birthday_option_day))
    # select by visible text
    month.select_by_visible_text('14')
    time.sleep(1)
    # day = selecting month dropdown
    month = Select(driver.find_element(By.ID, birthday_option_month))
    # select by visible text
    month.select_by_visible_text('Feb')
    time.sleep(1)
    # day = selecting year dropdown
    month = Select(driver.find_element(By.ID, birthday_option_year))
    # select by visible text
    month.select_by_visible_text('2000')
    time.sleep(1)
    driver.find_element(By.XPATH, gender_male_radio_btn).click()
    time.sleep(1)

    driver.find_element(By.NAME, sign_up_btn).click()
    time.sleep(120)

    next_window_message = driver.find_element(By.XPATH, confirmation_message )
    assert next_window_message.is_displayed()

def test_register_invalid_email():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, create_new_account_btn).click()
    time.sleep(10)
    driver.find_element(By.NAME, first_name_field).send_keys("azu")
    time.sleep(1)
    driver.find_element(By.NAME, last_name_field).send_keys("ayehu")
    time.sleep(1)
    driver.find_element(By.NAME, registration_email_field).send_keys("getachewayehu77.com")
    driver.find_element(By.NAME, registration_password_field).send_keys("azuta@1234")
    time.sleep(1)
    # day = selecting day dropdown
    month = Select(driver.find_element(By.ID, birthday_option_day))
    # select by visible text
    month.select_by_visible_text('14')
    time.sleep(1)
    # day = selecting month dropdown
    month = Select(driver.find_element(By.ID, birthday_option_month))
    # select by visible text
    month.select_by_visible_text('Feb')
    time.sleep(1)
    # day = selecting year dropdown
    month = Select(driver.find_element(By.ID, birthday_option_year))
    # select by visible text
    month.select_by_visible_text('2000')
    time.sleep(1)
    driver.find_element(By.XPATH, gender_male_radio_btn).click()
    time.sleep(1)

    driver.find_element(By.NAME, sign_up_btn).click()
    time.sleep(10)
    error_message =  driver.find_element(By.CLASS_NAME, "_5633 _5634 _53ij")
    print(error_message)
    assert error_message.is_displayed()


def test_different_reEnter_email_from_original_email():
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        driver.find_element(By.XPATH, create_new_account_btn).click()
        time.sleep(10)
        driver.find_element(By.NAME, first_name_field).send_keys("azu")
        time.sleep(2)
        driver.find_element(By.NAME, last_name_field).send_keys("ayehu")
        time.sleep(1)
        driver.find_element(By.NAME, registration_email_field).send_keys("hgwqeyw@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, re_enter_email_field).send_keys("azariaayehu@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, registration_password_field).send_keys("azuta@1234")
        time.sleep(1)
        # day = selecting day dropdown
        month = Select(driver.find_element(By.ID, birthday_option_day))
        # select by visible text
        month.select_by_visible_text('14')
        time.sleep(1)
        # day = selecting month dropdown
        month = Select(driver.find_element(By.ID, birthday_option_month))
        # select by visible text
        month.select_by_visible_text('Feb')
        time.sleep(1)
        # day = selecting year dropdown
        month = Select(driver.find_element(By.ID, birthday_option_year))
        # select by visible text
        month.select_by_visible_text('2000')
        time.sleep(1)
        driver.find_element(By.XPATH, gender_male_radio_btn).click()
        time.sleep(1)

        driver.find_element(By.NAME, sign_up_btn).click()
        time.sleep(10)

        error_message = driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]")
        assert error_message.is_displayed()


def test_invalid_password_lessThan_six_characters():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, create_new_account_btn).click()
    time.sleep(10)
    driver.find_element(By.NAME, first_name_field).send_keys("azu")
    time.sleep(2)
    driver.find_element(By.NAME, last_name_field).send_keys("ayehu")
    time.sleep(1)
    driver.find_element(By.NAME, registration_email_field).send_keys("azariaayehu@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, re_enter_email_field).send_keys("azariaayehu@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, registration_password_field).send_keys("azu4")
    time.sleep(1)
    # day = selecting day dropdown
    month = Select(driver.find_element(By.ID, birthday_option_day))
    # select by visible text
    month.select_by_visible_text('14')
    time.sleep(1)
    # day = selecting month dropdown
    month = Select(driver.find_element(By.ID, birthday_option_month))
    # select by visible text
    month.select_by_visible_text('Feb')
    time.sleep(1)
    # day = selecting year dropdown
    month = Select(driver.find_element(By.ID, birthday_option_year))
    # select by visible text
    month.select_by_visible_text('2000')
    time.sleep(1)
    driver.find_element(By.XPATH, gender_male_radio_btn).click()
    time.sleep(1)

    driver.find_element(By.NAME, sign_up_btn).click()
    time.sleep(10)

    error_message = driver.find_element(By.ID,"reg_error_inner").text
    print(error_message)
    assert error_message == "Your password must be at least 6 characters long. Please try another."


def test_invalid_password_more_than_20_characters():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, create_new_account_btn).click()
    time.sleep(10)
    driver.find_element(By.NAME, first_name_field).send_keys("azu")
    time.sleep(2)
    driver.find_element(By.NAME, last_name_field).send_keys("ayehu")
    time.sleep(1)
    driver.find_element(By.NAME, registration_email_field).send_keys("azariaayehu@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, re_enter_email_field).send_keys("azariaayehu@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, registration_password_field).send_keys("azu4,sjchdsjvgdvdhvdfj,vhfdjbhfbvjfdvbhfhbfjJHVDFJVLDFHLHVGSAJDSKADGKFCGEDFVEYWFYFEGCHSA NZX")
    time.sleep(1)
    # day = selecting day dropdown
    month = Select(driver.find_element(By.ID, birthday_option_day))
    # select by visible text
    month.select_by_visible_text('14')
    time.sleep(1)
    # day = selecting month dropdown
    month = Select(driver.find_element(By.ID, birthday_option_month))
    # select by visible text
    month.select_by_visible_text('Feb')
    time.sleep(1)
    # day = selecting year dropdown
    month = Select(driver.find_element(By.ID, birthday_option_year))
    # select by visible text
    month.select_by_visible_text('2000')
    time.sleep(1)
    driver.find_element(By.XPATH, gender_male_radio_btn).click()
    time.sleep(1)

    driver.find_element(By.NAME, sign_up_btn).click()
    time.sleep(60)

    error_message = driver.find_element(By.ID, "reg_error_inner").text
    print(error_message)
    assert error_message == "Your password must be at least 6 characters long. Please try another."


