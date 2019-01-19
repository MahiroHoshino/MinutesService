#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 
import cgi
import sys
import io
 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
 
form = cgi.FieldStorage()
  
text_data = form.getvalue('text', 'no data')
  
print('Content-type: text/html; charset=UTF-8')
print('')
print(text_data)