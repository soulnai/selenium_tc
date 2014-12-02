# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


login = "test_login_mail@gmail.com"
password = "test_pass"
mail_from = "testmail@test.test"


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        #self.driver.quit()
        pass

    def test_input_field(self):
        self.driver.get("http://gmail.com")
        username_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Email"]')))
        username_field.send_keys(login)
        password_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Passwd"]')))
        password_field.send_keys(password)
        self.driver.find_element_by_xpath("//input[@id='PersistentCookie']").click()
        self.driver.find_element_by_xpath('//input[@id="signIn"]').click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gbqfq"]'))).send_keys(mail_from)
        mail_exist = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='gsan_a']"))).is_displayed()
        if mail_exist:
            mail_create_button = self.driver.find_element_by_xpath("//div[contains(text(),'НАПИСАТЬ')]")
            mail_create_button.click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@name='to']"))).send_keys(login)
            self.driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Sup!")
            self.driver.find_element_by_xpath("//div[contains(text(),'Отправить')]").click()


if __name__ == '__main__':
    unittest.main()