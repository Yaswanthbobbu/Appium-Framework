# to be improved

This repository contains tests (feature files) for "SKF-TKBA" application

The test are written in Python language and requires an active installation of Python 3.8.

Once Python 3.8 is installed, it is recommended to create a Python vitual environment to run the tests.

To setup an virtual environment:

`virtualenv --python=$HOME/python/path ./target/venv`


####### Tags
Test classification tags are not yet implemented. So no changes needed for now.
Following tags are in place:
1. @bug: to disable a test (feature or scenario) with a broken behavior for which a bug is reported.
2. skip: to disable a test (feature or scenario) for any other reason
3. wip: to disable a test(feature or scenario) that is under implementation 

To run all the tests (without the above tags), use the following command from root directory:
`behave`
To run a particular feature file:
`behave path/to/the/feature/file/or/directory`

allure :
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

allure serve “logs_path”