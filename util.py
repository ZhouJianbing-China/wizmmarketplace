import json
import logging.handlers
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import DIR_PATH, HOST, BROWSER


class GetDriver:
    __web_driver = None

    # Get Web Driver
    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            if BROWSER == "chrome":
                cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif BROWSER == "firefox":
                cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            else:
                cls.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

            cls.driver.get(HOST)
            cls.driver.maximize_window()
        return cls.driver


# Read json
def read_json(filename):
    file_path = DIR_PATH + os.sep + "data" + os.sep + filename
    arrs = []
    with open(file_path, "r", encoding="utf-8")as f:
        for data in json.load(f):
            arrs.append(tuple(data.values()))
        return arrs


# Log
class GetLog:

    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            cls.__log = logging.getLogger()
            cls.__log.setLevel(logging.INFO)
            filename = DIR_PATH + os.sep + "log" + os.sep + "wizmarketplace_auto.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # add format
            tf.setFormatter(fm)
            # add to logger
            cls.__log.addHandler(tf)
        # return logger
        return cls.__log


if __name__ == '__main__':

    # Expectation：[(),()]
    GetLog.get_log().info("Test logging")



