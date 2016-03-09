#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import MyTestCase
import time
import requests
from UCMM.Pages import CarRecordPage, SelectOrderDialog, ReceiptTotalPage
from UCMM.Data import Get_excel_data


class TestCase(MyTestCase.MyTestCase):

	def test_car_record_export(self):
		header = self.Sign_In().header()
		# header.navigate_car_page(u'车辆配载')
		# 打开批次 91508 进入装车清单
		header.navigate(self.url['beta']+header.urls[u'装车清单'], '91508')
		CarRecordPage.CarRecordPage().export()

		time.sleep(14)
		r = requests.get(self.url['beta']+header.urls[u'装车清单']+'91508', 'expCarOrder')
		print r.headers
		time.sleep(4)
		pass

	# 测试挑单核销窗口
	# 进入回单总表->回单接收， 然后点击接收，将order.xlsx里的order number 输入 搜索框 然后点击添加
	def test_order_select_dialog(self):
		header = self.Sign_In('longbin', 'beta', '2000').header()
		header.navigate(self.url['beta']+header.urls[u'回单总表'], '')
		receipt_total = ReceiptTotalPage.ReceiptTotalPage()
		receipt_total.navigate_receipt(u'回单接收')
		time.sleep(4)
		select_order_dialog = receipt_total.open_select_order_dialog()
		order_numbers = Get_excel_data.GetData('order.xlsx').get_column(0)
		select_order_dialog.add_order(order_numbers)

