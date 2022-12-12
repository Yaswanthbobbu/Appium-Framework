from appium.webdriver.appium_service import AppiumService


class AppiumUtil:

    def __init__(self):
        self.appium_service = AppiumService()

    def connect(self):
        self.appium_service.start(args=['--base-path', '/wd/hub'])

    def disconnect(self):
        self.appium_service.stop()
