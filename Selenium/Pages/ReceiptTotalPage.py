#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Page
import time
import SelectOrderDialog


class ReceiptTotalPage(Page.Page):

	def navigate_receipt(self, title_name):
		self.find_element(title_name, self.Link_Text).click()

	def open_select_order_dialog(self):
		self.find_element('#receipt_receive').click()
		time.sleep(2)
		return SelectOrderDialog.SelectOrderDialog()