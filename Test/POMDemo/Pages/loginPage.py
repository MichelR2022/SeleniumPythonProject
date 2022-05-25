from selenium.webdriver.common.by import By
from Test.POMDemo.Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        # self.password_textbox_id = 'txtPassword'
        self.login_button_id = 'btnLogin'

    def enter_username(self, username):
        self.driver.find_element(By.ID, Locators.username_textbox_id).clear()
        # self.driver.find_element(By.ID, 'txtUsername').clear()
        self.driver.find_element(By.ID, 'txtUsername').send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()
