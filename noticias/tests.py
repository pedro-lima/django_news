"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
    def teste_browser(self):
        browser = webdriver.Firefox() # Get local session of firefox
        browser.get("http://www.yahoo.com") # Load page
        assert "Yahoo!" in browser.title
        elem = browser.find_element_by_name("p") # Find the query box
        elem.send_keys("seleniumhq" + Keys.RETURN)
        time.sleep(0.2) # Let the page load, will be added to the API
        try:
            browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
        except NoSuchElementException:           
            self.fail("can't find seleniumhq")
        browser.close()
        
class ViewTest(TestCase):
    pass

class ModelTest(TestCase):
    pass    
