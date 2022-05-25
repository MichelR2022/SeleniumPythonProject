from selenium import webdriver
# from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Ici ça ne fonctionne pas, car Python s'attend à voir tous les "import" au début du fichier
from Test.POMDemo.Pages.loginPage import LoginPage
from Test.POMDemo.Pages.homePage import HomePage

path = 'C:/Users/EXPERTEASE PRGI INC/PycharmProjects/Selenium/Drivers/chromedriver.exe'


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=path)
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        # self.driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        # self.driver.find_element(By.ID, 'btnLogin').click()
        # self.driver.find_element(By.ID, 'welcome').click()
        # self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test complété")

    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Python/Reports'))
