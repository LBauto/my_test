#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import MyTestCase
from UCMM.Pages import SignIn, OrderListPage, PayBillingSettleListPage, CreateOrderPage
import time
from UCMM.Controller import Report
import unittest


class TestCase(MyTestCase.MyTestCase):

	# 创建运单
	def test_create_order(self):
		set_model = {u'途经': u'二皮', u'托运人': u'auto托运人15'}
		order_model = self.data.get_order_models(rows=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], set_model=set_model)
		# order_model = self.data.get_order_models(i_range=[1, 2], set_model=set_model)

		create_order = self.Sign_In('longbin', 'beta', '4028')
		for model in order_model:
			if order_model.index(model) != 0:
				create_order = create_order.header.navigate_create_order_page()
			order_info_page = create_order.fill_order(model).save_order()
			print order_info_page.order_number() + ': ' + model[u'付款方式']
			# m = order_info_page.get_order_info()
			#self.assertEqual(order_info_page.order_number(), model[u'运单号'])
			# 到达运单
			# order_info_page.arrived_to_city()
			# # 签收运单
			# order_info_page.sign_receive(pay_lack=45.98, pay_lack_msg='auto msg')

	# 示例：获取order list表中数据
	def test_get_order_list_data(self):
		header = SignIn.SignIn(self.user_data['longbin'], self.url['beta'], '2000').sign_in().header
		header.navigate_order_list_page()
		time.sleep(1)
		order_list_page = OrderListPage.OrderListPage(u'全部')
		# 获取一行的数据，生成字典， key为表头例如 运单号 开单日期 等
		table = order_list_page.table
		selected_row = table.row(2)
		'''
		print u'获得第二行运单号的值'
		print table.table_data[2][table.table_header.index(u'运单号')]
		print u'获得第二行第二列的值'
		print table.table_data[2][table.table_header.index(u'运单号')]
		'''
		print u'列出选择的一行内所有的值'
		for i in selected_row.keys():
			print i + selected_row[i]
		print u'列出运单号一列所有的值'
		# 通过列名获取一列数据
		column_data = table.get_column_value(u'运单号')
		for i in column_data:
			print i

	def test_get_pay_billingSettle_List(self):
		header = SignIn.SignIn(self.user_data['longbin'], self.url['beta'], '2000').sign_in().header
		header.navigate(u'现付核销')
		table = PayBillingSettleListPage.PayBillingSettleListPage().search().table
		selected_row = table.row(2)
		print u'列出选择的一行内所有的值'
		for i in selected_row.keys():
			print i + selected_row[i]
		print u'列出运单号一列所有的值'
		# 通过列名获取一列数据
		column_data = table.get_column_value(u'运单号')
		for i in column_data:
			print i
if __name__ == 'TestCaseOrderList' or __name__ == '__main__':

	test = unittest.makeSuite(TestCase)
	Report.Report(testunit=test, file_name='TestCaseOrderList')





