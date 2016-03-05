#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Selenium.Controller import Report
import sys
import HTMLTestRunner


class MyTestCase(unittest.TestCase):

	# 冒泡排序
	def test_quick(self):
		i_list = [1,3,6,34,23,12,5,8,19,9,0,10,11,15]
		print range(len(i_list)-1,-1,-1)
		for i in range(len(i_list)-1,-1,-1):
			for j in range(i):
				if i_list[j] >= i_list[j+1]:
					i_list[j], i_list[j+1] = i_list[j+1], i_list[j]
			print i_list

	def test_try(self):
		i_list = [1,3,6,34,23,12,5,8,19,9,0,10,11,15]
		i = 0
		j = len(i_list)-2
		while i < j:
			t = j
			while i <= t:
				if i_list[t] < i_list[t+1]:
					i_list[t], i_list[t+1] = i_list[t+1], i_list[t]
				t -= 1
			print i_list
			i += 1

	def test_quick_sort(self):
		i_list = [18,13,6,34,23,12,5,8,1,9,0,10,11,15]
		self.quick_sort(i_list, 0, len(i_list)-1)

	def quick_sort(self, i_list, low, high):
		if low<high:
			key = self.sub_sort(i_list, low, high)
			self.quick_sort(i_list, low, key)
			self.quick_sort(i_list, key+1, high)

	def sub_sort(self, i_list, low, high):
		# i_list = [1,3,6,34,23,12,5,8,19,9,0,10,11,15]
		# low = 0
		# high = len(i_list)-1

		tamp = i_list[low]
		while low < high:
			while low < high and i_list[high] >= tamp:
				high -= 1
			while low < high and i_list[high] < tamp:
				i_list[low] = i_list[high]
				low += 1
				i_list[high] = i_list[low]
		i_list[low] = tamp
		return low
if __name__ == '__main__':
	unittest.main()