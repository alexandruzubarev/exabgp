#!/usr/bin/env python
# encoding: utf-8
"""
parser.py

Created by Thomas Mangin on 2009-08-25.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

import unittest

from exabgp.configuration import Configuration

from exabgp.configuration.bgp import SectionBGP
from exabgp.configuration.bmp import SectionBMP
from exabgp.configuration.bgp.family import SectionFamily
from exabgp.configuration.bgp.capability import SectionCapability
from exabgp.configuration.bgp.session import SectionSession
from exabgp.configuration.bgp.process import SectionProcess
from exabgp.configuration.bgp.neighbor import SectionNeighbor

import pprint
pp = pprint.PrettyPrinter(indent=3)

"""
@alexandru zubarev: 
Created a derived class with name TestNewConfiguration with two methods: 
1. test_parsing (with no parameters) 
2. parse (with a set of parameters for constructing and running the tests)
Method parse is returning parsed configuration file according to registered config sections.
Is printing the required sections with its values.
"""
class TestNewConfiguration (unittest.TestCase):
	def test_parsing (self):

		def parse (fname):
			conf = Configuration()
			conf.register(SectionBGP,        ['bgp'])
			conf.register(SectionFamily,     ['bgp','family'])
			conf.register(SectionCapability, ['bgp','capability'])
			conf.register(SectionSession,    ['bgp','session'])
			conf.register(SectionProcess,    ['bgp','process'])
			conf.register(SectionNeighbor,   ['bgp','neighbor'])
			conf.register(SectionBMP,        ['bmp'])

			return conf.parse_file(fname)

		try:
			parsed = parse('./qa/new/simple.conf')
		except IOError:
			parsed = parse('../new/simple.conf')

		for section in ['capability','process','session','neighbor']:
			d = parsed[section]
			for k,v in d.items():
				print '%s %s ' % (section,k)
				pp.pprint(v)
				print
			print

		# print
		# for klass in sorted(registry._klass):
		# 	print '%-20s' % str(klass).split('.')[-1][:-2], registry._klass[klass].content

if __name__ == '__main__':
	unittest.main()
