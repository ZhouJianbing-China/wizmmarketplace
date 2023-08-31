import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


from base import log
from config import DIR_PATH, SLEEP_TIME


class Base:

    def __init__(self, driver):
        log.info("Initialing，driver object：{}".format(driver))
        self.driver = driver

    def base_find(self, loc, timeout=10, poll=0.8):
        log.info("Finding element：{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until( lambda x: x.find_element(*loc))

    def base_click(self, loc):
        log.info("Clicking element：{}".format(loc))
        self.base_find(loc).click()

    def base_input(self, loc, value):
        time.sleep(SLEEP_TIME)
        el = self.base_find(loc)
        el.clear()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
        log.info("Input into：{} content：{}".format(loc, value))
        el.send_keys(value)

    def base_get_text(self, loc):
        log.info("Getting element text：{}".format(loc))
        return self.base_find(loc).text

    def base_get_input_value(self, loc):
        log.info("Getting element value：{}".format(loc))
        return self.base_find(loc).get_attributes('value')

    def base_get_img(self):
        log.info("Calling screen capture method")
        img_path = DIR_PATH + os.sep + "img" + os.sep + "{}.png".format(time.strftime("%Y%m%d%H%M%S"))
        self.driver.get_screenshot_as_file(img_path)

    def base_switch_frame(self, loc):
        log.info("Calling switch frame method，switch to：{}".format(loc))
        el = self.base_find(loc)
        self.driver.switch_to.frame(el)

    def base_default_frame(self):
        self.driver.switch_to.default_content()
