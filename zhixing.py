# -*- coding: UTF-8 -*-

import os
from datetime import datetime
import shutil
import time


class action:
	def __init__(self,name):
		self.name=name        

	def folder(self):
		if self.name=='非U8订单':
			os.system(r"explorer E:\采购课\供应商\采购订单\非U8订单") #
			
		elif self.name=='采购订单':
			os.system(r"explorer E:\采购课\供应商\采购订单")
			
		elif self.name=='扫描文件夹':
			os.system(r"explorer R:\采购课\扫描文件夹")
			
		elif self.name=='固定资产扫描':
			os.system(r"explorer E:\采购课\固定资产扫描")
			
		elif self.name=='报价单':
			os.system(r"explorer E:\采购课\报价单")
			
		elif self.name=='电子发票':
			os.system(r"explorer E:\电子发票")
			
		elif self.name=='月初供应商考核':
			os.system(r"explorer E:\采购课\供应商\月初供应商考核表")
			
		elif self.name=='部分物料管控表':
			os.system(r"explorer E:\采购课\部分物料管控表")
			
		elif self.name=='盘存表':
			os.system(r"explorer E:\采购课\盘存表")
			
		elif self.name=='降价共享':
			os.system(r"explorer \\ZENGJING\Users\zengjing\Desktop\降价共享")
			
		elif self.name=='原材料最新价格（会计）':
			os.system(r"explorer E:\采购课\供应商\每月提交资料\会计")
			
		elif self.name=='合格供应商一览表':
			os.system(r"explorer E:\采购课\供应商\合格供应商一览表")
			
		elif self.name=='固定资产盘点':
			os.system(r"explorer E:\采购课\固定资产盘点")
			
		elif self.name=='供应商综合评价表':
			os.system(r"explorer E:\采购课\供应商\供应商综合评价表")
			
		elif self.name=='供应商排名':
			os.system(r"explorer E:\采购课\供应商\供应商排名")	
			
		elif self.name=='报关资料':
			os.system(r"explorer \\linshaoli\报关资料相关")
			
		elif self.name=='国外采购订单':
			os.system(r"explorer \\linshaoli\国外采购")
			
		elif self.name=='交期管理表':
			os.system(r"explorer Z:\采购课\林少丽\交期管理表")
			print('password: 946934')
	def file(self):
		if self.name=='订单执行统计表':
			os.system(r"start E:\采购课\供应商\采购订单执行统计表\订单执行统计表.xlsm")
			print('打开的文件路径:E:\采购课\供应商\采购订单执行统计表\订单执行统计表.xlsm')
		if self.name=='合格率一览表':
			os.system(r"start R:\采购课\合格率一览表.xlsm")
			print('打开的文件路径:R:\采购课\合格率一览表.xlsm')
		if self.name=='部分原物料价格走势图':
			os.system(r"start E:\采购课\部分物料管控表\部分原物料价格走势图.xlsx")
			print('打开的文件路径:E:\采购课\部分物料管控表\部分原物料价格走势图.xlsx')
		if self.name=='采购统计表':
			os.system(r'start E:\采购课\供应商\每月提交资料\2020年" "统计表(每月8日提交)实验版.xlsm')
			print('打开的文件路径:E:\采购课\供应商\每月提交资料\2020年" "统计表(每月8日提交)实验版.xlsm')
		if self.name=='入库单列表（发票结算）':
			os.system(r"start E:\采购课\供应商\采购入购单列表\入库单列表.xlsm")
			print('打开的文件路径:E:\采购课\供应商\采购入购单列表\入库单列表.xlsm')
		if self.name=='对账单':
			os.system(r"start E:\采购课\供应商\对账单\对账单.xlsm")
			print('打开的文件路径:E:\采购课\供应商\对账单\对账单.xlsm')
		if self.name=='费用报销清单':
			os.system(r"start E:\采购课\供应商\采购订单\非U8订单\费用报销清单.xlsm")
			print('打开的文件路径:E:\采购课\供应商\采购订单\非U8订单\费用报销清单.xlsm')
		if self.name=='订单送签情况':
			os.system(r"start D:\Mystuff\files\ddsq.py")

		if self.name=='国外采购记录表':
			os.system(r"start E:\国外采购\国外采购记录表.xlsx")
		if self.name=='分机号':
			os.system(r"start D:\Mystuff\files\worklist\ext.py")			

	def del_desktop(self):
		check = input('确定要删除桌面除worklist以外所有数据？(Y/N)')
		if check.lower() == 'y':
			path=r"C:\Users\gaoyanming.RIKEN\Desktop"
			filelist=os.listdir(path)
			for x in filelist:
				filepath=os.path.join(path,x)
				if os.path.isfile(filepath) and x!='worklist.lnk' and x!='main.lnk':
					os.remove(filepath)
				elif os.path.isdir(filepath):
					shutil.rmtree(filepath,True)
				
	def backup(self):
		t=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
		rootdir=r"R:/总经理室/扫描文件夹"
		aimdir=r"D:/扫描文件夹"
		dir1=r"R:\采购课\合格率一览表.xlsm"
		dir2=r"E:\My_Backup\合格率一览表"+t+".xlsm"
		worklist1=r"D:\Mystuff\files\worklist.py"
		worklist2=r"E:\My_Backup\worklist"+t+".py"
		
		filelist=os.listdir(rootdir)
		filelist2=os.listdir(aimdir)
		for x in filelist:
			filepath=os.path.join(rootdir,x)
			if x not in filelist2:
				shutil.copy(filepath,aimdir)
		shutil.copyfile(dir1,dir2)
		shutil.copyfile(worklist1,worklist2)
		print('文件已备份完成！')

		
	def A3(self):
		#print("请输入本月三宝的价格：")
		price1 =int(input('请输入本月三宝价格：'))
		price2=price1+460
		price3=round(price2*1.145,2)
		year=datetime.now().year
		month=datetime.now().month+1
		line1=f"{year}年{month}月计算出来的价格为{price3}请确认：\n"
		line2=f"取三宝价格:{price1}加上200，再加上运费160，加管理费利润100，={price2}\n"
		line3=f"再加上14.5%的税费，最终为{price2}*1.145={price3}"
		line4=f"{month-1}月25日富宝资讯漳州三宝报价{price1}元/吨，故A3软钢{year}年{month}月份售价为：（{price1}+200+160+100)*1.145={price3}元/吨。"
		#print(f"{line1}",end='')
		#print(f"{line2}",end='')
		#print(line3)
		#print(line4)
		filename=f"{year}年{month}月A3软钢价格.txt"
		indata=open(filename,'w')
		indata.write(line1)
		indata.write(line2),
		indata.write(line3)
		indata.write("\n\n")
		indata.write(line4)
		indata.close()
		os.system(filename)
	def weather(self):
		import urllib.request as r
		url='http://api.openweathermap.org/data/2.5/weather?q=xiamen&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
		data=r.urlopen(url).read().decode('utf-8')
		import json
		data=json.loads(data)
		mm=datetime.now().month
		dd=datetime.now().day
		import weather
		h_av_temp,l_av_temp,max_high,max_low = weather.tianqi(mm,dd)
		description='天气：'+str(data['weather'][0]['description'])+'\n温度：'+str(data['main']['temp'])+'℃\n湿度：'+str(data['main']['humidity'])+'%'+'\n近八年当日历史平均：'+'\n最高温度：'+ h_av_temp +'℃\n最低温度度：'+ l_av_temp + '℃'+'\n近八年当日历史最高：'+'\n高温：'+  max_high + '℃'+'\n低温：'+ max_low + '℃'
		
		print(description)



