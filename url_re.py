# -*- coding: utf-8 -*- 
from urllib import request
import re

some_url = "http://lenta.ru/news/2015/04/26/terrorism/"

filehandle = request.urlopen(some_url)

html_code = filehandle.read()

links_pattern = "<a.*?</a>"

links = re.findall(links_pattern, str(html_code))

# for iiii in links:
# 	print (iiii)

import sys
print("😊😊😊😊")