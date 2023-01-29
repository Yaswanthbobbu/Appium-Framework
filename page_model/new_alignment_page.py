from basepage.BaseClass import BasePage
from locators.new_alignment_locators import *
import utilities.CustomLogger as cl


class NewAlignmentPage(BasePage):

    def __init(self, driver):
        super.__init__(driver)
        self.driver = driver

    def clickSelectMachine(self):
        self.clickElement(select_machine_button, 'index')

    def clickAddnewMachine(self):
        self.clickElement(select_machine_button, 'index')
        cl.allureLogs('clicked on add new machine button')
