from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class CommonTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_add_task(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Pomodoro web', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'The task to do')
		inputbox.send_keys('write code')
		inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text=='1: write code' for row in rows), "There is no new task in table.")
		self.fail('Finish the test')

if __name__ == '__main__':
	unittest.main(warnings='ignore')