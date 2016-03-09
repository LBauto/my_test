#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Page
import CreateOrderPage


class SignIn(Page.Page):

	def __init__(self, user_data, env, port):
		self.phone = user_data['telephone']
		self.password = user_data['password']
		if port != '':
			self.URL = env+':'+port
		else:
			self.URL = env

	def sign_in(self):
		# 如果再次使用driver时 需要再次打开浏览器，因为teardown已经把driver关闭
		self.max_browser()
		self.open(self.URL)
		self.find_element('#telePhone').send_keys(self.phone)
		self.find_element('#passWord').send_keys(self.password)
		self.find_element('#loginBtn').click()
		self.wait(5)
		return CreateOrderPage.CreateOrder()



