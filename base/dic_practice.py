#!/usr/bin/pyton

info = {}
name = raw_input("Please input name:")
age = raw_input("Please input age:")
gender = raw_input("Please input gender:")

info['name']= name
info['age'] = age
info['gender'] = gender

for k,v in info.items():
	print k+':'+v
