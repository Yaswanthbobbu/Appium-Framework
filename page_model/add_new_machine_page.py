from basepage.BaseClass import BasePage
from locators.add_new_machine_locators import *


class AddNewMachinePage(BasePage):

    def __init(self, driver):
        super.__init__(driver)
        self.driver = driver

    def verifyPage(self):
        element = self.isDisplayed(self._pagetitle, 'text')
        assert element == True

    def enterid(self):
        self.sendText('123', self._machine_id_input, 'text')

    def clicksave(self):
        self.clickElement(self._save_button, 'text')