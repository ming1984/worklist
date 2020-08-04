# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:50:53 2019

@author: gaoyanming
"""
import zhixing
import ext
def menu():
    print('|------------------每年、其它------------------|')
    print('|1:天气情况                                    |')
    print('|2:分机号                                      |')
    print('|q:退出                                        |')
    print('|----------------------------------------------|')
    choice = input('请输入选项：')
    if choice =='1':
        zhixing.action('天气情况').weather()
    elif choice =='2':
        ext.menu()#zhixing.action('分机号').file()
    elif choice =='q':
        pass
    else:
        print('输入错误！请输入正确的选项。')

if __name__ == '__main__':
    menu()