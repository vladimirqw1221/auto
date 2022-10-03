from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



from base.base_class import Base


class Finish(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #     Locators






    # Getters






    # Action







    # Metods
    def finish(self):
        with allure.step("Finish"):
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.get_screnshot()






