from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


from base.base_class import Base


class Payment(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #     Locators

    finish_button = "//button[@id='finish']"




    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.finish_button )))




    # Action


    def click_finish_button(self):
        self.get_finish_button().click()
        print("CLICK FINISH BUTTON")




    # Metods
    def select_product(self):
        with allure.step("Select product pay"):
            self.get_current_url()
            self.click_finish_button()







