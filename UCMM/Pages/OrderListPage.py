#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class OrderListPage(Page.Page):

	def __init__(self, filter_name):
		self.find_element(filter_name, self.Link_Text).click()

	@property
	def order_list_table(self):
		return self.table

	def navigate_order_tab(self, link_text):
		self.find_element(link_text, self.Link_Text).click()
		WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element(By.CLASS_NAME, 'curr').text == link_text)
