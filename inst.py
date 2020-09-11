import selenium
from selenium import webdriver

class InstagramBot():
    def __init__(self):
    #     self.username = username
    #     self.password = password
        self.driver = webdriver.Firefox()

    def run(self):
        self.login()
        # https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher
        # input[@name="username"]
        # input[@name="password"]
    
    def login(self):
        print("aaa")
        driver = self.driver
        driver.get("www.google.com")


InstagramBot().run()
