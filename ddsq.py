# -*- coding: UTF-8 -*-
#创建数据库并把txt文件的数据存进数据库
import sqlite3 #导入sqlite3
import time

def select(i):
	conn = sqlite3.connect(r'D:\Database\data.db') #创建数据库，如果数据库已经存在，则链接数据库；如果数据库不存在，则先创建数据库，再链接该数据库。
	cur = conn.cursor() #定义一个游标，以便获得查询对象。
	cur.execute('create table if not exists dingdan (date date,dd_from text,dd_to text,tjd_from text,tjd_to,yn char(20))')#创建表
	if i==1:
		cur.execute('select * from dingdan order by rowid desc limit 1')
		f=cur.fetchall()
		if f[0][5]=="":
			text='送签中...'
		else:
			text='已签完。'
		print('☆'*24,'\n')
		print("日期:{}  订单：{}-{}  调价单：{}-{}  状态：{}".format(f[0][0],f[0][1],f[0][2],f[0][3],f[0][4],text))
		print('\n','☆'*24)
	elif i==2:
		d=input("输入日期：")
		df=input("订单开始：")
		dt=input("订单结束：")
		tjdf=input("调价单开始：")
		tjdt=input("调价单结束：")
		cur.execute('insert into dingdan(date,dd_from,dd_to,tjd_from,tjd_to,yn) values (?,?,?,?,?,"")',(d,df,dt,tjdf,tjdt))
	elif i==3:
		f2=cur.execute('select rowid,date,dd_from,dd_to,tjd_from,tjd_to from dingdan where yn=""')
		p=cur.fetchall()
		if len(p)==0:
			print('☆'*24,'\n')
			print("没有送签中资料！")
			print('\n','☆'*24)
		else:
			print('☆'*24,'\n')
			for i in p:
				print("序号：{} 日期：{} 订单：{}-{} 调价单：{}-{}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
			print('\n','☆'*24)
			ch=int(input("请选择需要标记完成的序号："))
			cur.execute('update dingdan set yn=date("now") where rowid={}'.format(ch))

	elif i==4:
		exit()
	else:
		print("输入错误！")
	cur.close()#关闭游标
	conn.commit()#事务提交
	conn.close()#关闭数据库
	
	

while True:
	print('''===============================================================================
订单送签情况

请输入数字选择：
 1.查询最后一份送签情况
 2.新增送签数据
 3.送签资料标记完成
 4.退出
===============================================================================
	''')
	
	i=int(input('请输入选项：'))
	select(i)





