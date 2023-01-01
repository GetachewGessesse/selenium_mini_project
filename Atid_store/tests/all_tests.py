import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Atid_store.base_test.locators import *
def test_store_add_product_toCart():
    driver = webdriver.Chrome()
    driver.get(atid_URL)
    time.sleep(3)
    new_URL = driver.current_url
    assert new_URL == "https://atid.store/"
    driver.find_element(By.XPATH, store_link_text).click()
    time.sleep(3)
    page_title = driver.title
    print(page_title)
    assert page_title == "Products – ATID Demo Store"
    driver.find_element(By.XPATH, store_product).click()
    time.sleep(3)
    driver.find_element(By.XPATH, add_to_cart_button).click()
    time.sleep(5)
    driver.find_element(By.XPATH,  view_cart).click()
    time.sleep(5)
    cart_URL = driver.current_url
    assert cart_URL == "https://atid.store/cart-2/"
    pro_Name = driver.find_element(By.XPATH, braclet_location).text
    assert pro_Name == 'Anchor Bracelet'
    driver.close()
#
# test_store_add_product_toCart()




def test_men_add_product_toCart():
    driver = webdriver.Chrome()
    driver.get(atid_URL)
    time.sleep(3)
    driver.find_element(By.XPATH, men_link_text).click()
    time.sleep(3)
    page_title = driver.title
    print(page_title)
    assert page_title == "Men – ATID Demo Store"
    driver.find_element(By.XPATH, men_product).click()
    time.sleep(3)
    driver.find_element(By.XPATH, add_to_cart_button).click()
    time.sleep(3)
    driver.find_element(By.XPATH, view_cart).click()
    time.sleep(3)
    cart_URL = driver.current_url
    assert cart_URL == "https://atid.store/cart-2/"
    pro_name = driver.find_element(By.XPATH, blue_shoes_location).text
    assert pro_name == 'ATID Blue Shoes'
    driver.close()

# test_men_add_product_toCart()




def test_women_add_product_toCart():
    driver = webdriver.Chrome()
    driver.get(atid_URL)
    time.sleep(3)
    new_URL = driver.current_url
    assert new_URL == "https://atid.store/"
    driver.find_element(By.XPATH, women_link_text).click()
    time.sleep(3)
    page_title = driver.title
    print(page_title)
    assert page_title == "Women – ATID Demo Store"
    driver.find_element(By.XPATH, women_product).click()
    time.sleep(3)
    driver.find_element(By.XPATH, add_to_cart_button).click()
    time.sleep(3)
    driver.find_element(By.XPATH,  view_cart).click()
    time.sleep(3)
    cart_URL = driver.current_url
    assert cart_URL == "https://atid.store/cart-2/"
    prod_name = driver.find_element(By.XPATH, basic_Gray_Jeans_location).text
    assert prod_name == 'Basic Gray Jeans'
    driver.close()

# test_women_add_product_toCart()




def test_accessories_add_product_toCart():
    driver = webdriver.Chrome()
    driver.get(atid_URL)
    time.sleep(3)
    new_URL =driver.current_url
    assert new_URL == "https://atid.store/"
    driver.find_element(By.XPATH, accessories_text_link).click()
    time.sleep(3)
    page_title = driver.title
    print(page_title)
    assert page_title == "Accessories – ATID Demo Store"
    # assert page_title == "Accessories"
    driver.find_element(By.XPATH, accessories_product).click()
    time.sleep(3)
    selected_product_URL = driver.current_url
    assert selected_product_URL == "https://atid.store/product/black-over-the-shoulder-handbag/"
    driver.find_element(By.XPATH, add_to_cart_button).click()
    time.sleep(3)
    driver.find_element(By.XPATH, view_cart).click()
    time.sleep(3)
    cart_URL = driver.current_url
    assert cart_URL == "https://atid.store/cart-2/"
    prod_name = driver.find_element(By.XPATH, handbug_locator).text
    assert prod_name == 'Black Over-the-shoulder Handbag'
    driver.close()

# test_accessories_add_product_toCart()




def test_send_key_to_coupon_field():
    driver = webdriver.Chrome()
    driver.get(atid_URL)
    time.sleep(3)
    new_URL =driver.current_url
    assert new_URL == "https://atid.store/"
    driver.find_element(By.XPATH, accessories_text_link).click()
    time.sleep(3)
    page_title = driver.title
    print(page_title)
    assert page_title == "Accessories – ATID Demo Store"
    # assert page_title == "Accessories"
    driver.find_element(By.XPATH, accessories_product).click()
    time.sleep(3)
    selected_product_URL = driver.current_url
    assert selected_product_URL == "https://atid.store/product/black-over-the-shoulder-handbag/"
    driver.find_element(By.XPATH, add_to_cart_button).click()
    time.sleep(3)
    driver.find_element(By.XPATH, view_cart).click()
    time.sleep(3)
    cart_URL = driver.current_url
    assert cart_URL == "https://atid.store/cart-2/"
    prod_name = driver.find_element(By.XPATH, handbug_locator).text
    assert prod_name == 'Black Over-the-shoulder Handbag'
    coupon = driver.find_element(By.NAME, "coupon_code")
    coupon.clear()
    coupon.send_keys("ygqswqdye")
    coupon.send_keys(Keys.RETURN)
    time.sleep(4)
    error_message = driver.find_element(By.XPATH, error_message_location).text
    assert error_message == 'Coupon "ygqswqdye" does not exist!'
    driver.close()
    
# test_accessories_add_product_toCart()