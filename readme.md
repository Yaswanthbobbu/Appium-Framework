

allure :
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

allure serve “logs_path”