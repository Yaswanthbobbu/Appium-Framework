import inspect
import logging
import allure


def customLogger():
    logName = inspect.stack()[1][3]
    logger = logging.getLogger(logName)
    logger.setLevel(logging.DEBUG)

    # fileHandler = logging.FileHandler("{0}.log".format(logName), mode='a')  multiple files
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')
    fileHandler = logging.FileHandler("../reports/code.log", mode='a')
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
