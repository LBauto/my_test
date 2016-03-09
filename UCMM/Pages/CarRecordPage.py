#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Page


class CarRecordPage(Page.Page):

	def export(self):
		self.find_element('.J_orderExport').click()
		# chrome 弹出一个alert 360急速弹出alert后还弹出选择下载路径的弹窗
		self.accept_alert()
		pass