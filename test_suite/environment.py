from page_model.add_new_machine_page import AddNewMachine
from page_model.new_alignment_page import NewAlignment
from page_model.select_machine_page import SelectMachine

import allure
from allure_commons.types import AttachmentType


def before_feature(context, feature):
    platformName = context.config_files.userdata.get('platform_name')

    feature.new_alignment_page = NewAlignment(context.driver)
    feature.add_new_machine_page = AddNewMachine(context.driver)
    feature.select_machine_page = SelectMachine(context.driver)


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        if hasattr(context, 'step'):
            screen_shot_name = context.step.name
        else:
            screen_shot_name = context.scenario.name
        allure.attach(context.driver.get_screenshot_as_png(), name=screen_shot_name,attachment_type=AttachmentType.PNG)
