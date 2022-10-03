from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


from base.base_class import Base


class Main_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #     Locators

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    linc_about = "//a[@id='about_sidebar_link']"



    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.select_product_1 )))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.select_product_2 )))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.select_product_3 )))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.cart )))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.menu )))

    def get_linc_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.linc_about )))



    # Action


    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("SELECT PRODUCT 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("SELECT PRODUCT 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("SELECT PRODUCT 3")

    def click_cart(self):
        self.get_cart().click()
        print("CLICK CART")

    def click_menu(self):
        self.get_menu().click()
        print("CLICK menu")

    def click_about_linc(self):
        self.get_linc_about().click()
        print("CLICK linc about")




    # Metods
    def select_products_1(self):
        with allure.step("Select products 1"):
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()


    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about_linc()
        self.assert_url('https://saucelabs.com/')






