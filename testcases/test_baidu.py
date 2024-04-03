import os

from keywords.library import Libray
from selenium.webdriver.common.by import By
from time import sleep
import pytest


class TestBaidu(object):

    @pytest.mark.parametrize("data",["数据驱动","POM","关键字驱动"])
    def test01(self, data):
        libray = Libray()
        libray.open_brower("chrome")
        libray.load_url("https://www.baidu.com")
        sleep(2)
        libray.input((By.ID, "kw"), data)
        sleep(2)
        libray.click((By.ID, "su"))
        sleep(2)

