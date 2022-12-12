from basepage.BaseClass import BasePage
import utilities.CustomLogger as cl


class SelectMachine(BasePage):

    def __init(self, driver):
        super.__init__(driver)
        self.driver = driver