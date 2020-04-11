import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app


def open_home_page(app):
    app.wd.get("https://mail.google.com/mail/u/0/#inbox")


def send_letter(app, recipient, subject, message):
    app.wd.find_element_by_xpath("//div[@gh='cm']").click()
    app.wd.find_element_by_xpath("//textarea[@name='to']").send_keys(recipient)
    if app.wd.find_element_by_xpath("/html/body/div[37]").get_attribute('aria-expanded') == 'true':
        app.wd.find_element_by_xpath("//input[@name='q']").click()
    app.wd.find_element_by_xpath("//input[@name='subjectbox']").send_keys(subject)
    app.wd.find_element_by_xpath("//div[@role='textbox']").send_keys(message)
    app.wd.find_element_by_xpath("//div[contains(text(),'Отправить')][@role='button']").click()


def check_sent_letters_count(app):
    app.wd.get("https://mail.google.com/mail/u/0/#sent")
    WebDriverWait(app.wd, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Входящие')]")))
    new_num_sent = (WebDriverWait(app.wd, 5).until(
        EC.visibility_of_element_located((By.XPATH, "(//span[@class='ts'])[5]")))).text
    return int(new_num_sent)


def login(app, email, password):
    app.wd.find_element_by_xpath("//*[@id='identifierId']").send_keys(email)
    app.wd.find_element_by_xpath("//*[@id='identifierNext']").click()
    WebDriverWait(app.wd, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(password)
    app.wd.find_element_by_xpath("//*[@id='passwordNext']").click()
    WebDriverWait(app.wd, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Входящие')]")))


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])
