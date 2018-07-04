from selenium import webdriver
import unittest

class NewVistortest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_litle_and_retrieve_it_later(self):
        # Edith checks out to-do page
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]

if __name__ == '__main__':
    unittest.main(warnings='ignore')
