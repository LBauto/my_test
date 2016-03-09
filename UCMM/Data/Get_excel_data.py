#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import xlrd
import os
from UCMM.Model import Order_Model


class GetData(object):

	order_model = Order_Model.OrderModel().model

	def __init__(self, file_path=''):
		try:
			xlrd.Book.encoding = 'gbk'
			if file_path != '':
				# os.getcwd()+'\Data\\'+file_path
				self.excel_file = xlrd.open_workbook(os.getcwd()+'\Data\\'+file_path)
			else:
				self.excel_file = xlrd.open_workbook(os.getcwd()+'\Data\\'+'excel_order_model.xlsx')
		except:
			return
		self.table = self.excel_file.sheets()[0]

	def get_row(self, r):
		return self.table.row_values(r)

	def get_column(self, t):
		if isinstance(t, int):
			return self.table.col_values(t)[1:]
		else:
			index = self.get_row(0).index(t)
			return self.table.col_values(index)[1:]
		pass

	# i_range 设置生成i_range[0]到i_range[1]之间的model，方便批量生成model
	def get_order_models(self, rows=[], i_range=[0, 0], set_model={}):
		models = []
		if not rows:
			for r in range(i_range[0], i_range[1]+1):
				models.append(self.get_order_model(r, set_model).copy())
		else:
			for r in rows:
				models.append(self.get_order_model(r, set_model).copy())
		return models

	# 字典不是根据书写顺序排序
	def get_order_model(self, r, set_model={}):
		if isinstance(r, int):
			model = self.order_model
			row = self.get_row(r)
			row_title = self.get_row(0)
			for index in range(0, 49):
				title = row_title[index]
				if title in set_model.keys():
					model[title] = set_model[title]
				else:
					model[title] = row[index]
				if isinstance(model[title], float):
					split_value = str(model[title]).split('.')
					if split_value[1] == '0':
						model[title] = split_value[0]
		else:
			# 通过付款方式列生成对应的运单model
			pass
		return model

	def edit_order_model(self):

		pass

if __name__ == '__main__':
		print os.getcwd()+'\\'+'excel_order_model.xlsx'
		test = GetData('excel_order_model.xlsx')
		order_model = test.get_order_models([1, 2, 3, 5])
		print order_model[0][u'备注']





