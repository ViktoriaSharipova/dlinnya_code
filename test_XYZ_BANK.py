import time
import pytest
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert


@pytest.mark.usefixtures('setup')
class TestXYZBANK:
    browser = None

    @allure.feature('Тест сайта')
    @allure.story('Тест адреса персонажа')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/button[1]').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_2(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').text
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             assert element == 'Login', 'Ошибка'

    def test_3(self):
        with allure.step('Открываем ссылку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').click()
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').text
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             assert element == 'Login', 'Ошибка'

    def test_4(self):
        with allure.step('Нажимаем кнопку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открываем ссылку'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').click()
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').text
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             assert element == 'Login', 'Ошибка'

    def test_5(self):
        with allure.step('Нажимаем кнопку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открываем ссылку'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').click()
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').text
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             assert element == 'Login', 'Ошибка'

    def test_6(self):
        with allure.step('Нажимаем кнопку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открываем ссылку'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').click()
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').text
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             assert element == 'Login', 'Ошибка'

    def test_7(self):
        with allure.step('Нажимаем кнопку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открываем ссылку'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').click()
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').text
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
             assert element == 'Login', 'Ошибка'

    def test_8(self):
        with allure.step('Нажимаем кнопку'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открываем ссылку'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_9(self):
        with allure.step('Customer'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Hermoine Granger'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Dollar'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[2]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_10(self):
        with allure.step('Customer'):
             Alert(self.browser).accept
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Harry Potter'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Pound'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[3]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_11(self):
        with allure.step('Customer'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Ron Weasly'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Pound'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[3]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_12(self):
        with allure.step('Customer'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Albus Dumbledore'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Pound'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[3]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_13(self):
        with allure.step('Customer'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Neville Longbottom'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Pound'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[3]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_14(self):
        with allure.step('Customer'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Hermoine Granger'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Rupee'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[4]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def test_15(self):
        with allure.step('Customer'):
             self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]').click()
        with allure.step('Harry Potter'):
             self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').click()
        with allure.step('Currency'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]').click()
        with allure.step('Rupee'):
             self.browser.find_element(By.XPATH, '//*[@id="currency"]/option[4]').click()
        with allure.step('Process'):
             self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        with allure.step('OK'):
             Alert(self.browser).accept()
             allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

