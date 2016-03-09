#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
from selenium.webdriver.support.ui import Select
from Selenium.Model import Order_Model
import Page
import OrderInfoPage
from selenium.common.exceptions import NoSuchElementException
import time


class CreateOrder(Page.Page):

	_model = Order_Model.OrderModel().model

	def __init__(self):
		time.sleep(1)
		self.wait_element_visible(self.find_element('co_path', by=self.Name))
		try:
			self._model[u'开单时间'] = self.find_element('.form-datetime')
			self._model[u'发站'] = self.find_element('startCity', self.Name)
			self._model[u'到站'] = self.find_element('toCity', self.Name)
			self._model[u'途经'] = Select(self.find_element('toCityId', self.Name))
			self._model[u'运单号'] = self.find_element('OrderNum', self.Name)
			self._model[u'委托单号'] = self.find_element('customer_num', self.Name)
			self._model[u'托运人'] = self.find_element('ConsignorName', self.Name)
			self._model[u'托运人联系电话'] = self.find_element('ConsignorPhone', self.Name)
			self._model[u'托运人联系地址'] = self.find_element('ConsignorAddress', self.Name)
			# 货物
			self._model[u'货物名称'] = self.find_elements('.GoodsName')
			self._model[u'件数'] = self.find_elements('.J_numbers')
			self._model[u'包装'] = self.find_elements('.J_packet')
			self._model[u'重量'] = self.find_elements('.J_weight')
			self._model[u'体积'] = self.find_elements('.J_volume')
			self._model[u'单价'] = self.find_elements('.J_unit_price')
			self._model[u'单价单位'] = self.find_elements('.J_unit_price_unit')
			# 收货方 联系电话 联系地址
			self._model[u'收货人'] = self.find_element('ConsigneeName', self.Name)
			self._model[u'收货人联系电话'] = self.find_element('ConsigneePhone', self.Name)
			self._model[u'收货人联系地址'] = self.find_element('ConsigneeAddress', self.Name)
			self._model[u'运费'] = self.find_element('.table-new input[name=freight_price]')
			self._model[u'送货费'] = self.find_element('.table-new input[name=budget_delivery_price]')
			self._model[u'声明价值'] = self.find_element('goods_value', self.Name)
			self._model[u'代收货款'] = self.find_element('.table-new input[name=delivery]')
			self._model[u'装卸费'] = self.find_element('budget_handling_price', self.Name)
			self._model[u'保险费'] = self.find_element('.focus_active input[name=insurance]')
			self._model[u'货款手续费'] = self.find_element('.focus_active input[name=co_delivery_fee]')
			self._model[u'上楼费'] = self.find_element('budget_upstairs_price', self.Name)
			self._model[u'其他费'] = self.find_element('budget_misc_price', self.Name)
			self._model[u'提货费'] = self.find_element('budget_pick_goods_price', self.Name)
			self._model[u'垫付费'] = self.find_element('.table-new input[name=pay_advance]')
			# 付款方式 现返 欠返
			self._model[u'付款方式'] = Select(self.find_element('PaymentMode', self.Name))
			self._model[u'现付'] = self.find_element('pay_billing', self.Name)
			self._model[u'到付'] = self.find_element('pay_arrival', self.Name)
			self._model[u'欠付'] = self.find_element('pay_owed', self.Name)
			self._model[u'回付'] = self.find_element('pay_receipt', self.Name)
			self._model[u'月结'] = self.find_element('pay_monthly', self.Name)
			self._model[u'货到打卡'] = self.find_element('pay_credit', self.Name)
			self._model[u'贷款扣'] = self.find_element('pay_co_delivery', self.Name)
			self._model[u'现返'] = self.find_element('cashReturn', self.Name)
			self._model[u'欠返'] = self.find_element('discount', self.Name)

			# 送货方式， 回单
			self._model[u'送货方式'] = Select(self.find_element('ConsigneeMode', self.Name))
			self._model[u'回单'] = self.find_element('receiptNum', self.Name)
			# 备注
			self._model[u'备注'] = self.find_element('Remark', self.Name)
			# 发站实际支出
			self._model[u'发站提货费'] = self.find_element('local_pick_goods_price', self.Name)
			self._model[u'发站装卸费'] = self.find_element('local_handling_price', self.Name)
			self._model[u'发站其他费'] = self.find_element('local_misc_price', self.Name)
			self._model[u'预算送货费'] = self.find_element('remote_budget_delivery_price', self.Name)
			self._model[u'预算转交费'] = self.find_element('budget_tro_trans_price', self.Name)
		except NoSuchElementException, e:
			print u'没有发现元素'+str(e)

	def fill_order(self, order_model):
		model = order_model
		# 开单时间  目前还不能创建今天以外的日期，需要点击日历控件，单赋值不能改变日期
		if model[u'开单时间'] != '':
			self._model[u'开单时间'].send_keys(model[u'开单时间'])
		# 发站
		self._model[u'发站'].clear()
		self._model[u'发站'].send_keys(model[u'发站'])
		# 到站
		self._model[u'到站'].send_keys(model[u'到站'])
		# 运单号
		if model[u'运单号'] != '':
			self._model[u'运单号'].clear()
			self._model[u'运单号'].send_keys(model[u'运单号'])
		else:
			order_model[u'运单号'] = self._model[u'运单号'].get_attribute('value')
			pass
		# 委托单号
		if model[u'委托单号'] != '':
			self._model[u'委托单号'].send_keys(model[u'委托单号'])
		# 托运人 联系电话 联系地址
		self._model[u'托运人'].send_keys(model[u'托运人'])
		self._model[u'托运人联系电话'].send_keys(model[u'托运人联系电话'])
		self._model[u'托运人联系地址'].send_keys(model[u'托运人联系地址'])
		# 收货方 联系电话 联系地址
		self._model[u'收货人'].send_keys(model[u'收货人'])
		self._model[u'收货人联系电话'].send_keys(model[u'收货人联系电话'])
		self._model[u'收货人联系地址'].send_keys(model[u'收货人联系地址'])
		# 货物
		p = ''
		tamp1 = model[u'货物名称'].split('/')
		tamp2 = model[u'件数'].split('/')
		tamp3 = model[u'包装'].split('/')
		tamp4 = model[u'重量'].split('/')
		tamp5 = model[u'体积'].split('/')
		tamp6 = model[u'单价'].split('/')
		tamp7 = model[u'单价单位'].split('/')
		for i in range(0, 3):
			if tamp1[i]:
				self._model[u'货物名称'][i].send_keys(tamp1[i])
			if tamp2[i]:
				self._model[u'件数'][i].send_keys(tamp2[i])
			if tamp3[i]:
				self._model[u'包装'][i].send_keys(tamp3[i])
			if tamp4[i]:
				self._model[u'重量'][i].send_keys(tamp4[i])
			if tamp5[i]:
				self._model[u'体积'][i].send_keys(tamp5[i])
			if tamp6[i]:
				self._model[u'单价'][i].send_keys(tamp6[i])
			if tamp7[i] == '':
				p += Select(self._model[u'单价单位'][i]).first_selected_option.text.split('/')[1] + '/'
			else:
				p += tamp7[i] + '/'
			price_unit = tamp7[i]
			if price_unit != '':
				# self.select_drop_down(self._model[u'单价单位'][i], '/'+price_unit)
				Select(self._model[u'单价单位'][i]).select_by_visible_text('/'+price_unit)
		model[u'单价单位'] = p[:-1]
		# 运费 送货费。。。
		if model[u'运费'] != '':
			self._model[u'运费'].clear()
			self._model[u'运费'].send_keys(model[u'运费'])
		if model[u'送货费'] != '':
			self._model[u'送货费'].send_keys(model[u'送货费'])
		if model[u'声明价值'] != '':
			self._model[u'声明价值'].send_keys(model[u'声明价值'])
		if model[u'代收货款'] != '':
			self._model[u'代收货款'].send_keys(model[u'代收货款'])
		if model[u'装卸费'] != '':
			self._model[u'装卸费'].send_keys(model[u'装卸费'])
		if model[u'保险费'] != '':
			self._model[u'保险费'].clear()
			self._model[u'保险费'].send_keys(model[u'保险费'])
		if model[u'货款手续费'] != '':
			self._model[u'货款手续费'].clear()
			self._model[u'货款手续费'].send_keys(model[u'货款手续费'])
		if model[u'上楼费'] != '':
			self._model[u'上楼费'].send_keys(model[u'上楼费'])
		if model[u'其他费'] != '':
			self._model[u'其他费'].send_keys(model[u'其他费'])
		if model[u'提货费'] != '':
			self._model[u'提货费'].send_keys(model[u'提货费'])
		if model[u'垫付费'] != '':
			self._model[u'垫付费'].send_keys(model[u'垫付费'])

		# 付款方式 现返 欠返
		self._model[u'付款方式'].select_by_visible_text(model[u'付款方式'])
		if model[u'现付'] != '':
			self._model[u'现付'].clear()
			self._model[u'现付'].send_keys(model[u'现付'])
		if model[u'到付'] != '':
			self._model[u'到付'].clear()
			self._model[u'到付'].send_keys(model[u'到付'])
		if model[u'欠付'] != '':
			self._model[u'欠付'].clear()
			self._model[u'欠付'].send_keys(model[u'欠付'])
		if model[u'回付'] != '':
			self._model[u'回付'].clear()
			self._model[u'回付'].send_keys(model[u'回付'])
		if model[u'月结'] != '':
			self._model[u'月结'].clear()
			self._model[u'月结'].send_keys(model[u'月结'])
		if model[u'货到打卡'] != '':
			self._model[u'货到打卡'].clear()
			self._model[u'货到打卡'].send_keys(model[u'货到打卡'])
		if model[u'贷款扣'] != '':
			self._model[u'贷款扣'].clear()
			self._model[u'贷款扣'].send_keys(model[u'贷款扣'])
		if model[u'现返'] != '':
			self._model[u'现返'].send_keys(model[u'现返'])
		if model[u'欠返'] != '':
			self._model[u'欠返'].send_keys(model[u'欠返'])

		# 送货方式， 回单
		self._model[u'送货方式'].select_by_visible_text(model[u'送货方式'])
		self._model[u'回单'].clear()
		self._model[u'回单'].send_keys(model[u'回单'])
		# 备注
		self._model[u'备注'].send_keys(model[u'备注'])

		# 发站实际支出
		if model[u'发站提货费'] != '':
			self._model[u'发站提货费'].send_keys(model[u'发站提货费'])
		if model[u'发站装卸费'] != '':
			self._model[u'发站装卸费'].send_keys(model[u'发站装卸费'])
		if model[u'发站其他费'] != '':
			self._model[u'发站其他费'].send_keys(model[u'发站其他费'])
		if model[u'预算送货费'] != '':
			self._model[u'预算送货费'].send_keys(model[u'预算送货费'])
		if model[u'预算转交费'] != '':
			self._model[u'预算转交费'].send_keys(model[u'预算转交费'])
		# 途径
		# self.select_drop_down(self.find_element('toCityId', self.Name), model[u'途经'])
		select_to_city = Select(self.find_element('toCityId', self.Name)).options
		for option in self._model[u'途经'].options:
			if model[u'途经'] in option.text:
				self._model[u'途经'].select_by_visible_text(option.text)
		return self

	def save_order(self, is_success=1):
		# 保存
		if is_success == 1:
			self.find_element('#saveOrderBtn').click()
			self.wait(5)
			return OrderInfoPage.OrderInfoPage()
		else:
			return self
