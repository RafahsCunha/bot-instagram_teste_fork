import time
import configparser

from loguru import logger
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#adicionando uma linha de comentário teste

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def run(self):
        self.login()
        self.go_to_profile()
        self.loop_unfollow_and_follow()

    def login(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        logger.opt(colors=True).debug("Realizando login..")
        driver = self.driver
        driver.get(
            "https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher"
        )
        time.sleep(2)
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys(config["dados"]["username"])
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(config["dados"]["password"])
        password.send_keys(Keys.RETURN)
        logger.opt(colors=True).info("Login realizado\n")
        time.sleep(4)

    def go_to_profile(self):
        driver = self.driver
        driver.get("https://www.instagram.com/larissamanoela/?hl=pt-br")
        time.sleep(1)

    def unfollow_and_follow(self, c):
        driver = self.driver
        options = driver.find_elements_by_tag_name("button")
        options[1].click()
        time.sleep(2)
        unfollow = driver.find_elements_by_tag_name("button")
        if c == 1:
            unfollow[6].click()
            time.sleep(2)
        else:
            unfollow = driver.find_elements_by_tag_name("button")
            time.sleep(2)
            unfollow[27].click()
            time.sleep(2)

        follow = driver.find_elements_by_tag_name("button")
        follow[1].click()
        random_time = randint(20, 60)
        logger.opt(colors=True).info(f"{c}ª vez finalizada com sucesso!")
        logger.opt(colors=True).info(
            f"Irá rodar novamente em {random_time} segundos...\n"
        )
        time.sleep(random_time)

    def loop_unfollow_and_follow(self):
        driver = self.driver
        a = 40
        c = 1
        logger.opt(colors=True).info(f"Irá rodar {a} vezes\n")
        while c < a:
            logger.opt(colors=True).debug(f"Rodando pela {c}ª vez")
            try:
                self.unfollow_and_follow(c)
            except Exception as err:
                logger.opt(colors=True).exception(f"Erro ao rodar pela {a}ª vez", err)
                break
            c = c + 1
        driver.close()


InstagramBot().run()
