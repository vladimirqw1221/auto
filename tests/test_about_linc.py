import time

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


def test_linc_about(set_up):
    driver = webdriver.Chrome(executable_path='/Users/user/Desktop/resourse/chromedriver')

    print("Start test")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish test")
    time.sleep(5)


