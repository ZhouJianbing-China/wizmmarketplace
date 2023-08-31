import unittest
from time import sleep

from parameterized import parameterized

from base import log
from page.page_web_login import PageWebLogin
from page.page_web_profile import PageProfile
from util import GetDriver, read_json
from config import EMAIL, PASSWORD


class TestWebLoginUpdateProfile(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.driver = GetDriver.get_web_driver()
        self.login = PageWebLogin(self.driver)
        self.profile = PageProfile(self.driver)

    @classmethod
    def tearDownClass(self) -> None:
        sleep(1)
        self.driver.quit()

    def test_01_Login_Go_To_Profile(self):
        self.login.page_web_login(EMAIL, PASSWORD)
        self.profile.page_web_profile_link()

    @parameterized.expand(read_json("profile.json"))
    def test_02_WebLoginUpdateProfile(self, case_name, first_name, last_name, phone_number, expected_result):

        try:
            self.profile.page_web_first_name(first_name)
            self.profile.page_web_last_name(last_name)
            self.profile.page_web_phone_number(phone_number)
            self.profile.page_web_save_changes_btn()
            self.assertNotRegexpMatches(self.profile.page_web_welcome_msg(), first_name, "should not support "+first_name)

        except Exception as e:
            log.error(e)
            self.profile.base_get_img()
            raise
