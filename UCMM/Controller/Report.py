#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import unittest
import HTMLTestRunner
import os
import datetime


class Report(object):

	def __init__(self, testunit, file_name):
		self.unit = testunit
		self.name = file_name

	def report_html(self):
		path = os.getcwd()+'\\Results\\'
		if not os.path.exists(path):
			os.makedirs(path)
		filename = path+self.name+'_'+datetime.datetime.now().strftime('_%H_%M_%S')+'.html'
		# filename = "D:/test3.html"
		fp = file(filename, 'wb')

		runner = HTMLTestRunner.HTMLTestRunner(
			stream=fp,
			title=self.name,
			description='Run cases in '+self.name+',for results please refer to below table')
		runner.run(self.unit)

		fp.close()

	def send_report(self):

		pass

if __name__ == '__main__':
	unittest.main()
