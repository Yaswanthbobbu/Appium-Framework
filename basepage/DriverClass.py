from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'SM-A507FN'
        desired_caps['app'] = "C:/Users/dk8865/OneDrive - SKF/Desktop/Learnings/appium_bdd/Softwares/TKBA_24_Nov.apk"
        desired_caps['appPackage'] = 'com.skf.tkba.android'
        desired_caps['appActivity'] = 'com.skf.tkba.android.MainActivity'
        # desired_caps['noReset'] = True
        # desired_caps['fullReset'] = True

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver
