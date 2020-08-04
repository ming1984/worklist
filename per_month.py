# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:50:53 2019

@author: gaoyanming
"""
import zhixing
def menu():
    print('|------------------每---月----------------------|')
    print('|1:合格率一览表                                 |')
    print('|2:月初供应商考核                               |')
    print('|3:部分物料管控表                               |')
    print('|4:部分原物料价格走势图                         |')
    print('|5:采购统计表                                   |')
    print('|6:盘存表                                       |')
    print('|7:降价共享                                     |')
    print('|8:原材料最新价格（会计）                       |')
    print('|9:入库单列表（发票结算）                       |')
    print('|10:A3软钢价格计算                              |')
    print('|11:对账单                                      |')
    print('|q:退出                                         |')
    print('|-----------------------------------------------|')
    choice = input('请输入选项：')
    if choice == '1':
        zhixing.action('合格率一览表').file()
    elif choice =='2':
        zhixing.action('月初供应商考核').folder()
    elif choice =='3':
        zhixing.action('部分物料管控表').folder()
    elif choice =='4':
        zhixing.action('部分原物料价格走势图').file()
    elif choice =='5':
        zhixing.action('采购统计表').file()
    elif choice =='6':
        zhixing.action('盘存表').folder()
    elif choice =='7':
        zhixing.action('降价共享').folder()
    elif choice =='8':
        zhixing.action('原材料最新价格（会计）').folder()
    elif choice =='9':
        zhixing.action('入库单列表（发票结算）').file()
    elif choice =='10':
        zhixing.action('A3软钢价格计算').A3()
    elif choice =='11':
        zhixing.action('对账单').file()
    elif choice =='q':
        pass
    else:
        print('输入错误！请输入正确的选项。')

if __name__ == '__main__':
    menu()