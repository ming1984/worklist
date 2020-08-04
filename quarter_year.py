# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:50:53 2019

@author: gaoyanming
"""
import zhixing
def menu():
    print('|------------------每年、其它------------------|')
    print('|1:合格供应商一览表                            |')
    print('|2:固定资产盘点                                |')
    print('|3:供应商综合评价表                            |')
    print('|4:供应商排名                                  |')
    print('|q:退出                                        |')
    print('|----------------------------------------------|')
    choice = input('请输入选项：')
    if choice == '1':
        zhixing.action('合格供应商一览表').folder()
    elif choice =='2':
        zhixing.action('固定资产盘点').folder()
    elif choice =='3':
        zhixing.action('供应商综合评价表').folder()
    elif choice =='4':
        zhixing.action('供应商排名').folder()
    elif choice =='q':
        pass
    else:
        print('输入错误！请输入正确的选项。')

if __name__ == '__main__':
    menu()