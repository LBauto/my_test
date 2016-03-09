#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
from selenium import webdriver
import Page
import CarRecordPage
from Selenium.Controller import TableListControl


class CarManagePage(Page.Page):

	def __init__(self):
		self.table = TableListControl.Table()

	# 通过批次号选择发车批次 导航到批次详情页
	def select_car_record(self, car_record):
		self.find_element(car_record, self.Link_Text).click()
		# 等待装车清单元素出现
		self.wait('.curr')
		return CarRecordPage.CarRecordPage()
