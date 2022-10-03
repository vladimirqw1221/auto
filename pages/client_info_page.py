from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



from base.base_class import Base


class Client_info_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #     Locators

    fist_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    poatsl_code ="//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"




    # Getters

    def get_fist_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.fist_name )))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.last_name )))

    def get_poatsl_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.poatsl_code )))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self. continue_button)))

    # Action

    def input_fist_name(self , fist_name):
        self.get_fist_name().send_keys(fist_name)
        print("INPUT NAME  ")

    def input_last_name(self , last_name):
        self.get_last_name().send_keys(last_name)
        print("INPUT LASTNAME")

    def input_poatsl_code(self, poatsl_code):
        self.get_poatsl_code().send_keys(poatsl_code)
        print("INPUT POSTAL COSE")


    def click_continue_button(self):
        self.get_continue_button().click()
        print("CLICK COUNTINE BUTTON")


    # Metods
    def input_information(self):
        with allure.step("Input information"):
            self.get_current_url()
            self.input_fist_name("Vlad")
            self.input_last_name("Shedy")
            self.input_poatsl_code("8394798")
            self.click_continue_button()







