from time import sleep

from selenium.common import NoSuchElementException

import page
from base.base import Base
from base import log


class PageWebLogin(Base):
    def page_web_login_link(self):
        self.base_click(page.login_link)

    def page_web_email(self, value):
        self.base_input(page.web_login_email, value)

    def page_web_pwd(self, value):
        self.base_input(page.web_login_pwd, value)

    def page_web_login_btn(self):
        self.base_click(page.web_login_btn)

    def page_web_dst_alert_close_btn(self):
        self.base_click(page.dst_change_close)

    def page_web_login(self, email="jianbing.zhou@asc-dev.com.cn", pwd="test1234"):

        try:
            self.page_web_dst_alert_close_btn()
        except Exception as e:
            log.info("There isn't DST alert.")

        self.page_web_login_link()
        self.page_web_email(email)
        self.page_web_pwd(pwd)
        self.page_web_login_btn()

        try:
            self.page_web_dst_alert_close_btn()
        except NoSuchElementException as e:
            log.info("There isn't DST alert.")

