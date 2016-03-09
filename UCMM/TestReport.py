__author__ = 'lonwu'

import unittest
from UCMM.Controller import Report
import HTMLTestRunner
global i
i = 1


class MyTestCase(unittest.TestCase):
	def test_something(self):
		global i
		i+=1
		print i
		self.assertEqual(True, True)

	def test_quick(self):
		i_list = [1,3,6,34,23,12,5,8,19,9,0,10,11,15]
		print i_list


if __name__ == '__main__':
	print 'run main'
	u = unittest.TestSuite()
	u.addTest(MyTestCase('test_something'))
	u.addTest(MyTestCase('test_quick'))
	# test = unittest.makeSuite(MyTestCase)

	Report.Report(u, 'nicai').report_html()

	# filename = "D:/test9.html"
	# fp = file(filename, 'wb')
	#
	# runner = HTMLTestRunner.HTMLTestRunner(
	# 	stream=fp,
	# 	title='longbin',
	# 	description='Run cases in '+'longbin'+',for results please refer to below table')
	# runner.run(u)
	# exit(0)

