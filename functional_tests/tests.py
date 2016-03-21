from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class CommonTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_title):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_title, [row.text for row in rows])

	def test_add_task(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Pomodoro web', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_task')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'The task to do')
		inputbox.send_keys('write code')
		inputbox.send_keys(Keys.ENTER)
		list_url_a = self.browser.current_url
		self.assertRegex(list_url_a, '/list/.+')

		inputbox = self.browser.find_element_by_id('id_new_task')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'The task to do')
		inputbox.send_keys('make seminar data')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: write code')
		self.check_for_row_in_list_table('2: make seminar data')
		
		
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('write code', page_text)
		self.assertNotIn('make seminar data', page_text)

		inputbox = self.browser.find_element_by_id('id_new_task')
		inputbox.send_keys('buy milk')
		inputbox.send_keys(Keys.ENTER)

		list_url_b = self.browser.current_url
		self.assertRegex(list_url_b, '/list/.+')
		self.assertNotEqual(list_url_a, list_url_b)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('write code', page_text)
		self.assertIn('buy milk', page_text)






if __name__ == '__main__':
	unittest.main(warnings='ignore')