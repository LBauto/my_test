#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Driver


class Dialog(Driver.Driver):

	def __init__(self):
		self.wait_element_visible(self.find_element('.ui-dialog'))
		self.dialog = self.find_element('.ui-dialog')

	def accept(self):
		self.dialog.find_element(by=self.Css, value='.ui-dialog-button button:nth-of-type(1)').click()

	def cancel(self):
		self.dialog.find_element(by=self.Css, value='.ui-dialog-button button:nth-of-type(2)').click()