from selenium.webdriver.common.by import By

import config

# DST Change popup
dst_change_close = By.XPATH, "//img[@alt='close icon']"
"""
   Those are for login page   
"""
# login link
login_link = By.XPATH, "//a[@href='/login']"
# email
web_login_email = By.XPATH, "//input[@type='email']"
# password
web_login_pwd = By.XPATH, "//input[@type='password']"
# Sign in button
web_login_btn = By.XPATH, "//span[text()='Log In']/.."

"""
    Those are for profile page
"""
web_profile_link = By.XPATH, "//a[@href='/user/profile']"
web_profile_welcome_msg = By.XPATH, "//p[contains(text(),'Welcome back, ')]"
web_profile_first_name = By.NAME, "firstName"
web_profile_last_name = By.NAME, "lastname"
web_profile_mobile = By.NAME, "mobile"
web_profile_save_changes = By.XPATH, "//span[text()='SAVE CHANGES']/.."

"""
    Those are for search box
"""
web_search_box = By.XPATH, "//input[@type='text' and @placeholder='What are you looking for?']"

