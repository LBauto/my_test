#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Page


class PayBillingSettleListPage(Page.Page):

	def __init__(self):
		pass

	# 如果is_middle 等于1 点击页面中间的查询按钮 查询数据，否则点击筛选中的查询
	def search(self, is_middle=1):
		if is_middle == 1:
			self.find_element('.fn-tips-bk button').click()
		else:
			self.find_element('.filter-panel .form-btn button').click()
		self.wait(5)
		return self
