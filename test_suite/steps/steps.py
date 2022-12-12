from behave import *
import re
from datetime import *
import requests
use_step_matcher("re")


def instantiate_page(context, page):
    page_dict = dict()
    page_dict['NEW ALIGNMENT'] = context.feature.add_new_machine_page
    page_dict['ADD NEW MACHINE'] = context.feature.login_page
    page_dict['SELECT MACHINE'] = context.feature.search_and_selection_page

    context.feature.page = page_dict[page]


@given('user has just launched the "(.*)" application')
def step_impl(context, app):
    if app == 'SKF-TKBA':
        context.feature.page.wait_for_loading()
    else:
        pass


@step('he lands on "(.*)" page')
def step_impl(context, page):
    instantiate_page(context, page)


@step('he goes to "(.*)"')
def step_impl(context, page):
    context.execute_steps('''When he lands on "{}"'''.format(page))
    context.feature.page.navigate_to_page(page)

@step('he clicks on "(.*)" button')
def step_impl(context, btn_name):
    pass
