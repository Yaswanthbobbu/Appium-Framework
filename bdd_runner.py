from behave import __main__ as behave
from config_files.config import TAGS
import subprocess
import shutil
import os

cwd = os.getcwd()
results_dir = cwd + '//results'
if os.path.exists(results_dir):
    shutil.rmtree(results_dir)
behave.main('-f allure -o results ' + TAGS)
# subprocess.Popen('utilities\\allure\\bin\\allure serve results', shell=True, stdout=subprocess.PIPE,
#                  stderr=subprocess.PIPE)
