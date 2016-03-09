#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os
import datetime
import time
import Report

global driver, index
driver = ''
index = 1


class Driver(WebElement):

	def __init__(self):
		pass

	# By
	Css = By.CSS_SELECTOR
	Class_Name = By.CLASS_NAME
	ID = By.ID
	Link_Text = By.LINK_TEXT
	Name = By.NAME
	Tag_Name = By.TAG_NAME
	XPath = By.XPATH

	@property
	def my_driver(self):
		global driver, index
		if not driver:
			driver = webdriver.Chrome()
		if index == 0:
			driver = webdriver.Chrome()
			index = 1
		return driver

	# reset driver index, reset后可从新初始化driver
	@staticmethod
	def reset():
		global index
		index = 0

	@staticmethod
	def click(element):
		element.click()

	def save_screen(self, png_name):
		for filename in os.listdir(os.getcwd()):
			if filename == "Results":
				break
		else:
			os.mkdir(os.getcwd()+'\\Results')
		screen_shot_path = os.getcwd()+'\\Results\\'+png_name
		self.my_driver.get_screenshot_as_file(screen_shot_path+datetime.datetime.now().strftime('_%H_%M_%S')+'.png')

	@staticmethod
	def report():
		return Report.Report()

	def open(self, url):
		return self.my_driver.get(url)

	def quit(self):
		self.my_driver.quit()

	def max_browser(self):
		return self.my_driver.maximize_window()

	def find_element(self, value, by=Css):
		return self.my_driver.find_element(by, value)

	def find_elements(self, value, by=Css):
		return self.my_driver.find_elements(by, value)

	def wait(self, second):
		self.my_driver.implicitly_wait(second)

	def wait_element_visible(self, element, time_out=5):
		WebDriverWait(self.my_driver, time_out).until(EC.visibility_of(element))

	def wait_element_text(self, element, text, time_out=5):
		WebDriverWait(self.my_driver, time_out).until(EC.text_to_be_present_in_element(element, text))

	def wait_element_clickable(self, element, time_out=5):
		WebDriverWait(self.my_driver, time_out).until(EC.element_to_be_clickable(element))

	def wait_fuc(self, bool, time_out=5):
		WebDriverWait(self.my_driver, time_out).until(bool)

	# 确认alert
	def accept_alert(self):
		self.my_driver.switch_to().alert.accept()

	# 取消alert
	def dismiss_alert(self):
		self.my_driver.switch_to().alert.dismiss()

	# 鼠标悬停在一个元素上
	def hover(self, element):
		ActionChains(self.my_driver).move_to_element(element).perform()
		time.sleep(1)

	# 鼠标按下的源元素；target：鼠标释放的目标元素
	def drag_and_drop(self, element, target):
		ActionChains(self.my_driver).drag_and_drop(element, target).perform()

	# 获得所有element下的dropdown 子元素，子元素tagname 为li或者option
	def drop_element(self, element):
		# 点击element（弹出下拉列表）
		element.click()
		# 找到class name为  drop_panel的元素
		WebDriverWait(self.my_driver, 10).until(self.find_element('.drop_panel').is_displayed())
		# 在父亲元件下找到link为Action的子元素
		drop_down = self.find_element('.drop_panel')
		li = drop_down.find_elements(by=By.TAG_NAME, value='li')
		if not li:
			li = drop_down.find_elements(by=By.TAG_NAME, value='option')
		return li

	# 选择dropdown下面的某一项
	def select_drop_down(self, element, select_text):
		li = ''
		li = self.drop_element(element)
		for i in li:
			if i.text == select_text:
				i.click()
				break

	# 获得dropdown下面的某一项text值
	def drop_text(self, element):
		text = []
		li = self.drop_element(element)
		for i in li:
			text.append(i.text)
		return text


	# TO do...
	# 智能等待
	# hover
	# 选择option 和 text值
