#!/usr/bin/python
#encoding:utf-8
import os

def ChangeWeight(servers,state):
	if 'A'==servers:
		oldStr='10.0.0'
	else:
		oldStr='192.168.0'
	if 'down' == state:
		oldWeight='100'
		newWeight='0'
	else:
		oldWeight='0'
		newWeight='100'
	oldFile=os.path.join(os.path.abspath('..'),'conf/nginx.conf')
	newFile=oldFile + ".bak"
	with open(oldFile) as fd1,open(newFile,'w') as fd2:
		for line in fd1:
			if oldStr in line:
				line.replace('weight = %s' %(oldWeight),'weight= %s' %(newWeight))
			fd2.write(line)
	os.remove(oldFile)
	os.rename(newFile,oldFile)
	print("重启nginx！")
			

def UpdateCode(servers='A'):
#更新service组的代码
#先将service组的nginx权重设置为0
	print ("切下主机组%s" %(servers))
	ChangeWeight(servers,'down')
	print("更新主机组%s代码" %(servers))
	ChangeWeight(servers,'up')
	print ("主机组%s切上成功" %(servers))

#读取用户的输入，输入格式为 python update.py A 
server=raw_input("请输入你需要更新的主机组[A,B]：")
UpdateCode(server)
