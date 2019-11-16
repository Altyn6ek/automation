from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'D:\python for testers\Python for testers\учебное '
                                                        r'приложение\geckodriver.exe')
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get("https://www.softaculous.com/demos/PHP_Address_Book")

    def destroy(self):
        self.driver.quit()
