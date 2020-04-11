from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie
        else:
            raise ValueError("Unrecognized type of browser - %s" % browser)
        self.wd.implicitly_wait(10)
        self.wd.maximize_window()
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()
