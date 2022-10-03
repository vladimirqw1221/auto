from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



from base.base_class import Base


class Cart_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #     Locators

    chechout_button= "//button[@id='checkout']"




    # Getters

    def get_chechout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.chechout_button )))




    # Action


    def click_checkout_button(self):
        self.get_chechout_button().click()
        print("CLICK CHECKOUT BUTTON ")




    # Metods
    def production_configuration(self):
        with allure.step("Production configuration"):
            Logger.add_start_step(method="production_configuration")
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="production_configuration")







