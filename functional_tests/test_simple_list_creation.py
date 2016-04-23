from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.server_url)
        self.assertIn('Pomodoro web', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('작업 목록 시작', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '작업 아이템 입력')
        inputbox.send_keys('write code')
        inputbox.send_keys(Keys.ENTER)
        list_url_a = self.browser.current_url
        self.assertRegex(list_url_a, '/lists/.+')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '작업 아이템 입력')
        inputbox.send_keys('make seminar data')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: write code')
        self.check_for_row_in_list_table('2: make seminar data')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('write code', page_text)
        self.assertNotIn('make seminar data', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)

        list_url_b = self.browser.current_url
        self.assertRegex(list_url_b, '/lists/.+')
        self.assertNotEqual(list_url_a, list_url_b)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('write code', page_text)
        self.assertIn('buy milk', page_text)
