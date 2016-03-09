#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
from Selenium.Controller import HeaderControl, TableListControl, Driver, DialogControl


class Page(Driver.Driver):

	@property
	def header(self):
		return HeaderControl.Header()

	@property
	def table(self):
		return TableListControl.Table()

	@property
	def dialog(self):
		return DialogControl.Dialog()

