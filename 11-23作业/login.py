#/usr/bin/python
#encoding:utf-8
#auth:Eric wang
#登陆系统联系

user='Eric wang'
pw='EricAndBubble'

userInput=input("请输入用户名：")
pwInput=input("请输入密码：")

if (userInput==user and pwInput==pw):
    print('Login in!')
elif(userInput==user and pwInput != pw):
    print("密码输入错误！")
else:
    print("没有该用户：%s" %userInput)
