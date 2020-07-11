import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/jorge.rios/Downloads/chromedriver') 

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        #element = driver.find_element_by_id("passwd-id")
        #element = driver.find_element_by_name("passwd")
        #element = driver.find_element_by_xpath("//input[@id='passwd-id']")
        #element.clear()
    
    def test_forma(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        element = driver.find_element_by_id("nombre")
        element.send_keys("jair")
        element = driver.find_element_by_id("edad")
        element.send_keys("20")
        driver.find_element_by_id("submit").click()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
