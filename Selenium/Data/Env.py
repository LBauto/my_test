#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lonwu'
import Config


class Env(object):

	@property
	def envs(self):
		return Config.Config().envs()

	def __getitem__(self, item):
		if item in self.envs.keys():
			return self.envs[str(item)]
		else:
			print u'没有发现这个环境'


if __name__ == '__main__':

	user = Env()
	print user['pro']
