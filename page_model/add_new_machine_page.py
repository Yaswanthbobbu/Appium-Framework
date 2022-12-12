from basepage.BaseClass import BasePage


class AddNewMachinePage(BasePage):

    def __init(self, driver):
        super.__init__(driver)
        self.driver = driver

    # locator values
    _pagetitle = 'Add new machine'
    _machine_id_input =
    _machine_name_input =
    _company_dropdown =
    _belt_type_dropdown =
    _tolerance_value_dropdown =
    _add_distance_dropdown =
    _shieve_diameter_dropdown =
    _soft_foot_toggle =
    _save_button =

    def verifyPage(self):
        element = self.isDisplayed(self._pagetitle, 'text')
        assert element == True

    def enterid(self):
        self.sendText('123', self._machine_id_input, 'text')

    def clicksave(self):
        self.clickElement(self._save_button, 'text')