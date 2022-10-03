import time
import allure



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_button import Finish
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.pay_ment import Payment

# @pytest.mark.run(order=3)
@allure.description("test by product 1")
def test_by_product_1(set_up,set_group):
    driver = webdriver.Chrome(executable_path='/Users/user/Desktop/resourse/chromedriver')

    print("Start test1")

    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_products_1()
    cp = Cart_page(driver)
    cp.click_checkout_button()
    cip = Client_info_page(driver)
    cip.input_information()
    p = Payment(driver)
    p.click_finish_button()
    f = Finish(driver)
    f.finish()

    time.sleep(5)
@pytest.mark.run(order=1)
def test_by_product_2(set_up,set_group):
    driver = webdriver.Chrome(executable_path='/Users/user/Desktop/resourse/chromedriver')

    print("Start test2")

    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_products_2()
    cp = Cart_page(driver)
    cp.click_checkout_button()


    # time.sleep(5)

# @pytest.mark.run(order=2)
def test_by_product_3(set_up,set_group):
    driver = webdriver.Chrome(executable_path='/Users/user/Desktop/resourse/chromedriver')

    print("Start test3")

    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_products_3()
    cp = Cart_page(driver)
    cp.click_checkout_button()


    time.sleep(5)