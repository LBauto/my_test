#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import Driver


class Header(Driver.Driver):

	urls = {
		u'运单列表全部': '/index.php/Order/olist',
		u'中转运单': '/index.php/Order/transOrderList/',
		u'装车清单': '/index.php/Driver/noworderlist?car_record_id=',
		u'回单总表': '/index.php/Finance/receiptList.html#?',
		u'现付核销': '/index.php/Finance/payBillingSettleList',
		}

	def __init__(self):
		pass

	# 跳转到运单列表页
	def navigate_create_order_page(self):
		self.find_element('#createOrderINL').click()
		self.wait(3)
		from Selenium.Pages import CreateOrderPage
		return CreateOrderPage.CreateOrder()

	# 跳转到挑单夹
	def navigate_pick_order_page(self):
		self.find_element('#pick_order').click()
		self.wait(3)
		from Selenium.Pages import PickOrderPage
		return PickOrderPage.PickOrderPage()

	# 通过URL跳转到相应页面，但是不能返回页面类
	def navigate(self, page_title):
		self.open(str(self.my_driver.current_url).split('/')[2]+self.urls[page_title])

	def navigate_order_list_page(self):
		self.find_element('.menu.pull-left li:first-child a').click()
		WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element_by_class_name('crumb').is_displayed())

	def navigate_trans_order_list_page(self):
		self.my_driver.find_element_by_css_selector('.menu.pull-left > li:nth-of-type(2) > a').click()
		WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element_by_id('transferOrderBtn').is_displayed())
		from Selenium.Pages import OrderListPage
		return OrderListPage.OrderListPage()


	def navigate_car_page(self, page_name):
		menu = self.find_element(u'车辆', self.Link_Text)
		webdriver.ActionChains(self.my_driver).move_to_element(menu).perform()
		WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element_by_link_text(page_name).is_displayed())
		self.find_element(page_name, self.Link_Text).click()
		WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element_by_class_name('tab_list_nowOrder').is_displayed())

		# 不能导航公司信息
	def navigate_other_page(self, head_title, child_title='', page_title=''):
		menu = self.find_element(head_title, self.Link_Text)
		if child_title != '':
			webdriver.ActionChains(self.my_driver).move_to_element(menu).perform()
			WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element_by_link_text(child_title).is_displayed())
			child = self.find_element(child_title, self.Link_Text)
			if page_title != '':
				webdriver.ActionChains(self.my_driver).move_to_element(child).perform()
				WebDriverWait(self.my_driver, 3).until(lambda d: d.find_element_by_link_text(page_title).is_displayed())
				self.find_element(page_title, self.Link_Text).click()
			else:
				child.click()
		else:
			menu.click()