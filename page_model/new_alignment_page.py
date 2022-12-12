from basepage.BaseClass import BasePage
import utilities.CustomLogger as cl


class NewAlignmentPage(BasePage):

    def __init(self, driver):
        super.__init__(driver)
        self.driver = driver

    # locator values
    _select_machine_button = '1' #index
    _cancel_icon = '2'
    _add_new_machine_button = '3'

    def clickSelectMachine(self):
        self.clickElement(self._select_machine_button, 'index')

    def clickAddnewMachine(self):
        self.clickElement(self._select_machine_button, 'index')
        cl.allureLogs('clicked on add new machine button')


