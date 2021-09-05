import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def process_file(filename):
    filename = os.path.expanduser(filename)
    if not os.path.exists(filename):
        raise Exception("未在{}找到密码文件，请写入你的密码文件！".format(filename))
    accounts = {}
    for line in open(filename):
        if line != '\n':
            account, psd = line.strip().split(',')
            accounts[account] = psd
    return accounts


class Account:
    def __init__(self, filename):
        self.filename = filename
        self.accounts = process_file(filename)

    def items(self):
        return self.accounts.items()

    def __delitem__(self, key):
        """
        example:
            del my_account["1611082722"]
        """
        del self.accounts[key]

    def __repr__(self):
        result = ""
        for k, v in self.accounts.items():
            result += k + ',' + v + '\n'
        return result

    def save(self):
        """
        unused
        """
        with open(self.filename, 'w') as f:
            f.write(self.__repr__())


class Login:
    def __init__(self, filename, arg="--headless"):
        self.RETRY = 0
        self.opt = FirefoxOptions()
        self.opt.add_argument(arg)
        self.browser = None
        self.accounts = Account(filename)

    def try_all(self):
        self.browser = webdriver.Firefox(options=self.opt)
        for account, psd in self.accounts.items():
            if not self.login(account, psd):
                logging.error("Account {} is not logged successfully".format(account, psd))
            else:
                break
        self.browser.quit()

    def login(self, account, psd):
        try:
            self.browser.get(r"http://10.22.63.253/0.htm")
            username = self.browser.find_element_by_xpath('//input[@type="text"]')
            password = self.browser.find_element_by_xpath('//input[@type="password"]')

            username.clear()
            username.send_keys(account)
            password.clear()
            password.send_keys(psd)

            commit = self.browser.find_element_by_id("submit")
            commit.click()
            time.sleep(2)
            if "Drcom" not in self.browser.title:
                commit = self.browser.find_element_by_id("submit")
                commit.click()
                time.sleep(2)
                return False
            else:
                print('Online now. Account used: ', account)
                self.browser.quit()
                self.RETRY = 0
                return True
        except Exception as e:
            logging.error("ERROR OCCURRED:{}".format(e))
            # self.browser = webdriver.Firefox(options=self.opt, executable_path=_get_geckodriver_path())
            # time.sleep(2)
            # self.RETRY += 1
            # if self.RETRY < 10:
            #     return self.login(account, psd)
            # else:
            #     return False


if __name__ == '__main__':
    loginer = Login('~/.local/fly-online/password.txt', "")
    loginer.try_all()
