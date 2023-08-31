from selenium.webdriver.common.by import By

import page
import time
from base.base import Base
from util import read_json


class PageProfile(Base):

    def page_web_first_name(self, value):
        self.base_input(page.web_profile_first_name, value)

    def page_web_last_name(self, value):
        self.base_input(page.web_profile_last_name, value)

    def page_web_phone_number(self, value):
        self.base_input(page.web_profile_mobile, value)

    def page_web_welcome_msg(self):
        return self.base_get_text(page.web_profile_welcome_msg)

    def page_web_save_changes_btn(self):
        self.base_click(page.web_profile_save_changes)

    def page_web_profile_link(self):
        self.base_click(page.web_profile_link)
