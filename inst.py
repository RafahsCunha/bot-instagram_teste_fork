import time
import selenium

from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstagramBot():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def run(self):
        self.login()
        self.go_to_profile()
        self.loop_unfollow_and_follow()
        

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher")
        time.sleep(2)
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys("")
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("")
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def go_to_profile(self):
        driver = self.driver
        driver.get("https://www.instagram.com/larissamanoela/?hl=pt-br")
        time.sleep(1)
        

    def unfollow_and_follow(self, c):
        driver = self.driver
        unfollow = driver.find_elements_by_tag_name("button")
        time.sleep(3)
        unfollow[1].click()
        time.sleep(2)
        unfollow = driver.find_elements_by_tag_name("button")
        try:
            unfollow[5].click()
        except:
            unfollow[26].click()
        time.sleep(2)
        unfollow = driver.find_elements_by_tag_name("button")
        unfollow[0].click()
        random_time = randint(20, 60)
        print(f"Irá rodar novamente em {random_time} segundos...")
        time.sleep(random_time)

    def loop_unfollow_and_follow(self):
        driver = self.driver
        a = 10
        c = 0
        print(f"Irá rodar {a} vezes")
        while c < a:
            self.unfollow_and_follow(c)
            print(f"Rodando pela {c}ª vez")
            c = c + 1
        driver.close()


InstagramBot().run()
