#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Config


class User(object):
	data = {}

	def __getitem__(self, item):
		users = Config.Config().users()
		if item in users.keys():
			# telephone password
			self.data['telephone'] = str(users[str(item)]).split('/')[0]
			self.data['password'] = str(users[str(item)]).split('/')[1]
			return self.data
		else:
			print u'没有发现这个用户'


if __name__ == '__main__':

	user = User()
	print user['longbin']
	print user['longbin']['telephone']