import pytest
from selenium import webdriver
import time
import yaml

"""def selenium_test():
    driver = webdriver.Chrome()
    driver.get("http://192.168.11.25:8069/web")
    driver.find_element_by_id('login').send_keys("admin")
    driver.find_element_by_id('password').send_keys('admin')
    driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/button").click()
    
    time.sleep(4)


selenium_test()"""

'''def demo_method(a, b, x):
    if a > 1 and b == 0:
        x = x / a
    elif a == 2 or x > 1:
        x = x + 1
    return x


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("这是set up")

    def tearDown(self) -> None:
        print("这是tear down")

    def test_demoMethod(self):
        func = demo_method(2, 0, 2)
        self.assertEqual(1, func)

    def test_a(self):
        func = demo_method(0, 0, 5)
        self.assertEqual(func != 7, True)'''


class TestData:

    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        assert a * b > a + b
