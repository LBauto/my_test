#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import xml.dom.minidom
import os


class Config(object):

	user_data = {}
	i_browser = ''

	def __init__(self):
		# os.getcwd()+'\Data\\'+
		# 打开xml文档
		self.dom = xml.dom.minidom.parse(os.getcwd()+'\Data\\'+'config.xml')
		self.i_browser = self.browser()

	def default_url(self):
		env = {}
		root = self.dom.documentElement
		envs = root.getElementsByTagName('env')
		for e in envs:
			if e.getAttribute("key") == root.getElementsByTagName('browser')[0].getAttribute("selected"):
				env[e.getAttribute("key")] = e.getAttribute("url")
			else:
				print u'没有找到默认的环境url，请更改Config.xml文件browser节点属性'

	def default_user(self):
		user = {}
		root = self.dom.documentElement
		users = root.getElementsByTagName('user')
		for u in users:
			if u.getAttribute("key") == root.getElementsByTagName('users')[0].getAttribute("selected"):
				user[u.getAttribute("username")] = u.getAttribute("userdata")
			else:
				print u'没有找到默认的用户，请更改Config.xml文件users及子节点属性'
		return user

	def users(self):
		user = {}
		root = self.dom.documentElement
		users = root.getElementsByTagName('user')
		default = root.getElementsByTagName('users')[0].getAttribute("selected")
		for u in users:
			if u.getAttribute("username") == default:
				user["default"] = u.getAttribute("userdata")
			user[u.getAttribute("username")] = u.getAttribute("userdata")

		return user

	def envs(self):
		env = {}
		root = self.dom.documentElement
		envs = root.getElementsByTagName('env')
		default = root.getElementsByTagName('envs')[0].getAttribute("selected")
		for e in envs:
			if e.getAttribute("key") == default:
				env["default"] = e.getAttribute("url")
			env[e.getAttribute("key")] = e.getAttribute("url")
		return env

	def browser(self):
		root = self.dom.documentElement
		browser = root.getElementsByTagName('browser')
		return browser[0].getAttribute("selected")
if __name__ == '__main__':

	config = Config()

	print config.user_data