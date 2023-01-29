import os
from appium import webdriver

CWD = os.getcwd()
__driver_configs = dict()


def driver_setup(host, port, appium_version, platform_name, platform_version,
                 device_name, browser_name, device_orientation, test_name, app_uri):

    __driver_configs['host'] = host
    __driver_configs['port'] = port
    __driver_configs['appium_version'] = appium_version
    __driver_configs['platform_name'] = platform_name
    __driver_configs['platform_version'] = platform_version
    __driver_configs['device_name'] = device_name
    __driver_configs['browser_name'] = browser_name
    __driver_configs['device_orientation'] = device_orientation
    __driver_configs['test_name'] = test_name
    __driver_configs['app_uri'] = app_uri

    # __driver_configs['automationName'] = "UiAutomator2"
    # __driver_configs['appPackage'] = 'com.skf.tkba.android'
    # __driver_configs['appActivity'] = 'com.skf.tkba.android.MainActivity'
    # __driver_configs['noReset'] = True
    # __driver_configs['fullReset'] = True


def start_driver(context):
    try:
        context.driver = webdriver.Remote(
            command_executor='http://%s:%s/wd/hub' % (__driver_configs.get('host'), __driver_configs.get('port')),
            desired_capabilities={
                'platformName': __driver_configs.get('platform_name'),
                'platformVersion': __driver_configs.get('platform_version'),
                'deviceName': __driver_configs.get('device_name'),
                'app': (CWD + __driver_configs.get('app_uri'))
            })

        context.platform = __driver_configs.get('platform_name')
        if context.platform == 'Android':
            from page_model.new_alignment_page import NewAlignmentPage
        elif context.platform == 'iOS':
            from page_model.new_alignment_page import NewAlignmentPage
        elif context.platform == 'Windows':
            from page_model.new_alignment_page import NewAlignmentPage
        else:
            raise RuntimeError('Unrecognized platform: {}'.format(context.platform))
        context.new_alignment_page = NewAlignmentPage(context.driver)

    except Exception as e:
        raise e

def cleanup_driver(context):
    context.driver.quit()
