#!/usr/bin/python
#encoding:utf-8
#user:Eric wang
#使用python模拟select语句
import sys
i = raw_input('请输入SQL语句：')

SQLcode=i.split()
if SQLcode[0] != ''

elif 'select'==SQLcode[0].lower:
	with open('/root/studypy/homework2/table.txt') as fd:
		while True:
			x=fd.readline().split()
			#读到文件末尾
			if not x:
				break
			
			if age in SQLcode[1].lower:
				print x[2],
			elif name in SQLcode[1].lower:
				print x[1],
			elif id in SQLcode[1].lower:
				print x[0]
			elif class in SQLcode[1].lower:
				print x[4]
			print ''
elif 'delete'==SQLcode[0].lower:
	SQLcode = i.split('where')
	with open('/root/studypy/homework2/table.txt') as fd:
		with open('/root/studypy/homework2/table1.txt',w) as fd1:
			x=fd.readline()
			x1=x.split()
			fd1.write(x)
			while True:
				x=fd.readline()
				x1=x.split()
				if not x:
					break
				if x1[0] in SQLcode[1] and x1[1] in SQLcode[1] and x1[2] in SQLcode[1] and x1[3] in SQLcode[1]:
					continue
				else fd1.write(x)
			
elif 'update'==SQLcode[0]:
	with open('/root/studypy/homework2/table.txt') as fd:
		with open('/root/studypy/homework2/table1.txt',a+) as fd1:
			x=fd.readline()
			fd1.write(x)
			while True:
				


elif 'insert'==SQLcode[0]:
	
