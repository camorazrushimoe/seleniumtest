import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_check_quizpleas(self):
        driver = self.driver
        # driver.get("https://mozgva.com/?city_id=1#sign_in")
        # driver.get("https://mozgva.com/franchise/dashboard")
        input = driver.find_element_by_xpath("//*[@id=\"user_email\"]")
        input.send_keys("*")
        input2 = driver.find_element_by_xpath("//*[@id=\"user_password\"]")
        input2.send_keys("*")
        submit = driver.find_element_by_xpath("//*[@id=\"sign_in_user\"]/input[4]")
        submit.click()
        driver.get("https://mozgva.com/franchise/dashboard")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
