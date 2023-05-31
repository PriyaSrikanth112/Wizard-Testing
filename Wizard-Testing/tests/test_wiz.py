import unittest


from selenium.webdriver.support import expected_conditions as EC

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@ddt
# inherit TestCase Class and create a new test class
class PythonOrgSearch(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method

    @data(('0', 'standard_user', 'secret_sauce'), ('1', 'locked_out_user', 'secret_sauce'), ('2', 'standard_user', 'secret_sauce'))
    @unpack
    def test_search_in_python_org(self,count, username, password):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("https://www.saucedemo.com/")

        driver.find_element("xpath", '//*[@id="user-name"]').send_keys(username)
        driver.find_element("xpath", '//*[@id="password"]').send_keys(password)
        driver.find_element("xpath", '//*[@id="login-button"]').click()

        if count == '0':
            # Scenario 1
            self.assertIn("Swag Labs", driver.title)

        elif count == '1':
            # Scenario 2
            a = driver.find_element("xpath", '//*[@id="login_button_container"]/div/form/div[3]/h3').text
            self.assertIn('Sorry, this user has been banned.',a)
        elif count == '2':
            # Scenario 3
            select = Select(driver.find_element("xpath", '//*[@id="header_container"]/div[2]/div/span/select'))
            select.select_by_index(2)

            driver.find_element("xpath", '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="shopping_cart_container"]/a'))).click()

            driver.find_element("xpath", '//*[@id="checkout"]').click()

            driver.find_element("xpath", '//*[@id="first-name"]').send_keys('John')

            driver.find_element("xpath", '//*[@id="last-name"]').send_keys('Doe')
            driver.find_element("xpath", '//*[@id="postal-code"]').send_keys('123')
            driver.find_element("xpath", '//*[@id="continue"]').click()
            a = driver.find_element("xpath", '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text

            self.assertIn('$8.63', a)
            driver.find_element("xpath", '//*[@id="finish"]').click()
            a = driver.find_element("xpath", '//*[@id="checkout_complete_container"]/h2').text
            self.assertIn('Thank you', a)

    # cleanup method
    def tearDown(self):
        self.driver.close()


# execution the script
if __name__ == "__main__":
    unittest.main()

