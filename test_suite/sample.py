from basepage.DriverClass import Driver
import utilities.CustomLogger as cl
from basepage.BaseClass import BasePage
import time

driver1 = Driver()
log = cl.customLogger()

driver = driver1.driver_setup()
log.info('Launch app')

bp = BasePage(driver)
ele = bp.waitForElement("android.view.View",'class')
ele.click()

# add_new_machine_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
# add_new_machine_button.click()
#
# # company_dropdown = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='company name']").click()
#
# time.sleep(3)
# driver.quit()

# appium_service.stop()
