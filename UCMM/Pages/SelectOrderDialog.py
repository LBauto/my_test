#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Page


class SelectOrderDialog(Page.Page):

	def add_order(self, order_number):
		for n in order_number:
			input_element = self.find_element('#addOrderIpt')
			input_element.send_keys(n)
			self.find_element('#addToListBtn').click()
			input_element.clear()

	def get_header(self):
		headers = self.find_elements('#dialog #eidtTablelist tr:nth-of-type(1) th')
		headers_text = []
		for header in headers:
			headers_text.append(header.text)

	def get_orders_row(self):
		return self.find_elements('#eidtTablelist tbody tr')

	def remove_order(self, row_index):
		self.find_elements('.J-remove-item')[row_index].click()

	def remove_order_by_order_number(self, order_number):
		rows = self.get_orders_row()
		# To do .....
		pass