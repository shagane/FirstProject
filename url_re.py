# -*- coding: utf-8 -*- 

import urllib
import re

some_url = "http://lenta.ru/news/2015/04/26/terrorism/"

filehandle = urllib.urlopen(some_url)

html_code = filehandle.read()

links_pattern = "<a.*</a>"

links = re.findall (links_pattern, html_code)

for i in links:
	try:
		print i.decode('utf8')
	except:
		print i
