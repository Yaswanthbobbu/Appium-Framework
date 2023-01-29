from basepage.DriverClass import *
from basepage.AppiumClass import AppiumUtil as AU
from page_model.add_new_machine_page import AddNewMachinePage
from page_model.new_alignment_page import NewAlignmentPage
from page_model.select_machine_page import SelectMachinePage

import allure
from allure_commons.types import AttachmentType


def before_all(context):
    context.config.setup_logging()
    driver_setup(context.config.userdata.get("appium_host", "unknown"),
                 context.config.userdata.get("appium_port", "unknown"),
                 context.config.userdata.get("appium_version", "unknown"),
                 context.config.userdata.get("platform_name", "unknown"),
                 context.config.userdata.get("platform_version", "unknown"),
                 context.config.userdata.get("device_name", "unknown"),
                 context.config.userdata.get("browser_name", "unknown"),
                 context.config.userdata.get("device_orientation", "unknown"),
                 context.config.userdata.get("test_name", "unknown"),
                 context.config.userdata.get("app_uri", "unknown"))
    start_driver(context)

    # feature.new_alignment_page = NewAlignmentPage(context.driver)
    # feature.add_new_machine_page = AddNewMachinePage(context.driver)
    # feature.select_machine_page = SelectMachinePage(context.driver)


def after_all(context):
    pass
    #uninstall the app on cloude device
    context.driver.remove_app(context.config.userdata.get("app_uri"))


def before_feature(context, feature):
    # launch_app()
    pass


def before_scenario(context, scenario):
    # start_activity()
    # Android ONLY
    # get_current_activity()
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    cleanup_driver(context)


def before_step(context, step):
    pass


def after_step(context, step):
    if step.status == 'failed':
        if hasattr(context, 'step'):
            screen_shot_name = context.step.name
        else:
            screen_shot_name = context.scenario.name
        allure.attach(context.driver.get_screenshot_as_png(), name=screen_shot_name,attachment_type=AttachmentType.PNG)
