#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'

from UCMM.Pages import Page, SignIn
from UCMM.Data import Get_excel_data
import unittest
import os
import unittest.result
from UCMM.Data import Env, User


class MyTestCase(unittest.TestCase):
	class_name = ''
	# 手机 key = telephone，密码 key password，环境地址 key = url
	user_data = User.User()
	url = Env.Env()
	page = Page.Page()
	data = Get_excel_data.GetData()

	def setUp(self):
		print 'start: test name is '+str(self._testMethodName)

	def tearDown(self):
		# 如果case失败就会保存截图, 不能真正判断case 是否失败。
		# if result.wasSuccessful() == 0:
		self.page.save_screen(self._testMethodName)
		self.page.quit()
		self.page.reset()
		# 打印运行时间

		print 'Done: test name is '+str(self._testMethodName)

	def Sign_In(self, username='default', env='default', port=''):
		return SignIn.SignIn(self.user_data[username], self.url[env], port).sign_in()

if __name__ == '__main__':
	print 'pearent'
	pass