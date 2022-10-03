import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Current urt"""


    def get_current_url(self):
        get_url = self.driver.current_url
        print("Curent url" + get_url)



    """Methoat assert worlad"""

    def assert_world(self, world, result):
        value_world = world.text
        assert value_world == result
        print("Good claue world")

    """Methoat screnchot"""

    def get_screnshot(self):
        now_date = datetime.datetime.utcnow().strftime("%y. %m.%d.%H.%M.%S")
        new_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('/Users/user/Desktop/final_project/screen/' + new_screenshot)

    """Methoat Assert url """
    def assert_url(self, resault):
        get_url = self.driver.current_url
        assert get_url == resault
        print("Get value url")


