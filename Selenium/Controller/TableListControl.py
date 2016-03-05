#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Driver


class Table(Driver.Driver):

	header = ''

	def __init__(self):
		# 新板财务表头单独拿出一个table来处理
		# To do.. 只能获得显示出来的表头，隐藏在右边的列名不能获取到
		temp = self.find_elements('.headers')
		if temp:
			self.header = temp[0]
		else:
			self.header = self.find_element('table thead tr')
		self.body = self.find_element('tbody', self.Tag_Name)

	# 获得表头
	@property
	def table_header(self):
		heard_text = []
		for heard in self.header.find_elements_by_tag_name('th'):
			heard_text.append(heard.text)
		return heard_text

	@property
	# 表中数据很多的话会很慢。。。。。需要优化
	# 获得table某一个值，key为表头，index为行数
	def table_data(self):
		h = self.table_header
		rows = [[u'站位行']]
		row = self.body.find_elements_by_tag_name('tr')
		for r in row:
			row_info = []
			row_data = r.find_elements_by_tag_name('td')
			for t in h:
				row_info.append(row_data[h.index(t)].text)
			rows.append(row_info)
		return rows

	@property
	def row_count(self):
		return len(self.body.find_elements_by_tag_name('tr'))

	# 获得index行所有显示的内容
	# 返回字典类型，key为相应的列名
	def row(self, index):
		row_info = {}
		assert index < self.row_count, u'Row index should be less than ' + self.row_count
		row_data = self.body.find_elements_by_css_selector('tr:nth-of-type('+str(index)+') td')
		h = self.table_header
		for t in h:
			row_info[t] = row_data[h.index(t)].text
		return row_info

	# 获得name列的显示页所有的值
	def get_column_value(self, name):
		data = []
		try:
			index = self.table_header.index(name)
			all_rows = self.body.find_elements_by_tag_name('tr')
			for c in all_rows:
				column = c.find_element_by_css_selector('td:nth-of-type('+str(index+1)+')')
				data.append(column.text)
		except ValueError:
			print('Please input a valid header. ')
		return data

	# 获得value值所在的行index， value为唯一的link text（例如order number 批次号。。）
	def get_index(self, value):

		pass
