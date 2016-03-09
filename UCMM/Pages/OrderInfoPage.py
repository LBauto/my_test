#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
from Selenium.Model import Order_Model
import Page
from selenium.common.exceptions import NoSuchElementException
import time


class OrderInfoPage(Page.Page):

	_model = Order_Model.OrderModel().model

	def __init__(self):
		self.wait_element_visible(self.find_element('.dl-horizontal'))

		try:
			self._model[u'发站'] = self.find_element('startCity', self.Name)
			self._model[u'到站'] = self.find_element('toCity', self.Name)
			# 途经
			self._model[u'途经'] = self.find_element('toCityId', self.Name)

			self._model[u'运单号'] = self.find_element('OrderNum', self.Name)
			self._model[u'委托单号'] = self.find_element('customer_num', self.Name)
			self._model[u'托运人'] = self.find_element('ConsignorName', self.Name)
			self._model[u'托运人联系电话'] = self.find_element('ConsignorPhone', self.Name)
			self._model[u'托运人联系地址'] = self.find_element('ConsignorAddress', self.Name)
			self._model[u'收货人'] = self.find_element('ConsigneeName', self.Name)
			self._model[u'收货人联系电话'] = self.find_element('ConsigneePhone', self.Name)
			self._model[u'收货人联系地址'] = self.find_element('ConsigneeAddress', self.Name)

			self._model[u'货物名称'] = self.find_elements('.GoodsName')
			self._model[u'件数'] = self.find_elements('.J_numbers')
			self._model[u'包装'] = self.find_elements('.J_packet')
			self._model[u'重量'] = self.find_elements('.J_weight')
			self._model[u'体积'] = self.find_elements('.J_volume')
			self._model[u'单价'] = self.find_elements('.J_unit_price')
			self._model[u'单价单位'] = self.find_elements('.J_unit_price_unit')

			# 运费 送货费。。。
			self._model[u'运费'] = self.find_element('.table-new input[name=freight_price]')
			self._model[u'送货费'] = self.find_element('.table-new input[name=budget_delivery_price]')
			self._model[u'声明价值'] = self.find_element('goods_value', self.Name)
			self._model[u'代收货款'] = self.find_element('.table-new input[name=delivery]')
			self._model[u'装卸费'] = self.find_element('budget_handling_price', self.Name)
			self._model[u'保险费'] = self.find_element('.table-new input[name=insurance]')
			self._model[u'货款手续费'] = self.find_element('co_delivery_fee', self.Name)
			self._model[u'上楼费'] = self.find_element('budget_upstairs_price', self.Name)
			self._model[u'其他费'] = self.find_element('budget_misc_price', self.Name)
			self._model[u'提货费'] = self.find_element('budget_pick_goods_price', self.Name)
			self._model[u'垫付费'] = self.find_element('.table-new input[name=pay_advance]')
			# 付款方式 现返 欠返
			self._model[u'付款方式'] = self.find_element('PaymentMode', self.Name)
			self._model[u'现返'] = self.find_element('cashReturn', self.Name)
			self._model[u'欠返'] = self.find_element('discount', self.Name)

			# 送货方式， 回单
			self._model[u'送货方式'] = self.find_element('ConsigneeMode', self.Name)
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

	def order_number(self):
		return self._model[u'运单号'].get_attribute('value')

	# 点击到达 并取消发送短信
	def arrived_to_city(self, send_text=0):
		self.wait_element_visible(self.find_element('#arrived_confirm_btn'))
		self.find_element('#arrived_confirm_btn').click()
		dia = self.dialog
		if not send_text:
			self.find_element('mes_to_cee', by=self.Name).click()
		dia.accept()
		time.sleep(2)
		return self

	# 签收 并填写少收赔付 和少收赔付理由，去掉勾选发送短信
	def sign_receive(self, pay_lack=-1, pay_lack_msg='', send_text=0):
		self.wait_element_visible(self.find_element('#signReveive'))
		self.find_element('#signReveive').click()
		dia = self.dialog
		if pay_lack != -1:
			self.find_element('#pay_lack').send_keys(pay_lack)
		if pay_lack_msg != '':
			self.find_element('#pay_lack_msg').send_keys(pay_lack_msg)
		if not send_text:
			self.find_element('mes_to_cor', by=self.Name).click()
		dia.accept()
		# 等待取消签收按钮出现
		self.wait_element_visible(self.find_element('#cancelSignReveive'))
		return self

	def get_order_info(self):
		order_model = Order_Model.OrderModel().model
		# order_model[u'开单时间'] = self.find_element_by_class_name('form-datetime').get_attribute('value')
		order_model[u'发站'] = self._model[u'发站'].get_attribute('value')
		order_model[u'到站'] = self._model[u'到站'].get_attribute('value')
		# 途经
		order_model[u'途经'] = self._model[u'途经'].find_element(self.Css, 'option[selected=selected]').text

		order_model[u'运单号'] = self._model[u'运单号'].get_attribute('value')
		order_model[u'委托单号'] = self._model[u'委托单号'].get_attribute('value')
		order_model[u'托运人'] = self._model[u'托运人'].get_attribute('value')
		order_model[u'托运人联系电话'] = self._model[u'托运人联系电话'].get_attribute('value')
		order_model[u'托运人联系地址'] = self._model[u'托运人联系地址'].get_attribute('value')
		order_model[u'收货人'] = self._model[u'收货人'].get_attribute('value')
		order_model[u'收货人联系电话'] = self._model[u'收货人联系电话'].get_attribute('value')
		order_model[u'收货人联系地址'] = self._model[u'收货人联系地址'].get_attribute('value')
		# 货物 1/2/3
		count = len(self._model[u'货物名称'])
		for i in range(0, count):
			se = ''
			if i != count-1:
				se = '/'
			order_model[u'货物名称'] += self._model[u'货物名称'][i].get_attribute('value')+se
			order_model[u'件数'] += self._model[u'件数'][i].get_attribute('value')+se
			order_model[u'包装'] += self._model[u'包装'][i].get_attribute('value')+se
			order_model[u'重量'] += self._model[u'重量'][i].get_attribute('value')+se
			order_model[u'体积'] += self._model[u'体积'][i].get_attribute('value')+se
			order_model[u'单价'] += self._model[u'单价'][i].get_attribute('value')+se
			unit_price_unit_text = self._model[u'单价单位'][i].find_element(self.Css, 'option[selected=selected]').text
			order_model[u'单价单位'] += unit_price_unit_text.split('/')[1]+se
		# 运费 送货费。。。
		order_model[u'运费'] = self._model[u'运费'].get_attribute('value')
		order_model[u'送货费'] = self._model[u'送货费'].get_attribute('value')
		order_model[u'声明价值'] = self._model[u'声明价值'].get_attribute('value')
		order_model[u'代收货款'] = self._model[u'代收货款'].get_attribute('value')
		order_model[u'装卸费'] = self._model[u'装卸费'].get_attribute('value')
		order_model[u'保险费'] = self._model[u'保险费'].get_attribute('value')
		order_model[u'货款手续费'] = self._model[u'货款手续费'].get_attribute('value')
		order_model[u'上楼费'] = self._model[u'上楼费'].get_attribute('value')
		order_model[u'其他费'] = self._model[u'其他费'].get_attribute('value')
		order_model[u'提货费'] = self._model[u'提货费'].get_attribute('value')
		order_model[u'垫付费'] = self._model[u'垫付费'].get_attribute('value')
		# 付款方式 现返 欠返
		order_model[u'付款方式'] = self._model[u'付款方式'].find_element(self.Css, 'option[selected=selected]').text
		order_model[u'现返'] = self._model[u'现返'].get_attribute('value')
		order_model[u'欠返'] = self._model[u'欠返'].get_attribute('value')

		# 送货方式， 回单
		order_model[u'送货方式'] = self._model[u'送货方式'].find_element(self.Css, 'option[selected=selected]').text
		order_model[u'回单'] = self._model[u'回单'].get_attribute('value')
		# 备注
		order_model[u'备注'] = self._model[u'备注'].text

		# 发站实际支出
		order_model[u'发站提货费'] = self._model[u'发站提货费'].get_attribute('value')
		order_model[u'发站装卸费'] = self._model[u'发站装卸费'].get_attribute('value')
		order_model[u'发站其他费'] = self._model[u'发站其他费'].get_attribute('value')
		order_model[u'预算送货费'] = self._model[u'预算送货费'].get_attribute('value')
		order_model[u'预算转交费'] = self._model[u'预算转交费'].get_attribute('value')
		return order_model

	# 获的所有的日志，title和日志内容
	def order_record(self):
		all_record = self.find_elements('#orderOption')
		tmp = {}
		for ele in all_record:
			t = ele.find_element(by=self.Css, value='dt').text
			msg = ele.find_element(by=self.Css, value='dd').text
			tmp[t] = msg
		return tmp
