# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:50:53 2019

@author: gaoyanming
"""
import zhixing
def menu():
    print('|------------------日---常---------------------|')
    print('|1:报关资料                                    |')
    print('|2:国外采购订单                                |')
    print('|3:交期管理表                                  |')
    print('|4:国外采购记录表                              |')
    #print('|5:订单送签情况                                |')
    #print('|6:扫描文件夹                                  |')
    #print('|7:固定资产扫描                                |')
    #print('|8:报价单                                      |')
    #print('|9:电子发票                                    |')
    #print('|10:清空桌面数据                               |')
    #print('|11:备份数据                                   |')
    print('|q:退出                                        |')
    print('|----------------------------------------------|')
    choice = input('请输入选项：')
    if choice == '1':
        zhixing.action('报关资料').folder()
    elif choice =='2':
        zhixing.action('国外采购订单').folder()
    elif choice =='3':
        zhixing.action('交期管理表').folder()
    elif choice =='4':
        zhixing.action('国外采购记录表').file()
    #elif choice =='5':
        #zhixing.action('订单送签情况').file()
    #elif choice =='6':
        #zhixing.action('扫描文件夹').folder()
    #elif choice =='7':
        #zhixing.action('固定资产扫描').folder()
    #elif choice =='8':
        #zhixing.action('报价单').folder()
    #elif choice =='9':
        #zhixing.action('电子发票').folder()
    #elif choice =='10':
        #zhixing.action('清空桌面数据').del_desktop()
    #elif choice =='11':
        #zhixing.action('备份数据').backup()
    elif choice =='q':
        pass
    else:
        print('输入错误！请输入正确的选项。')

if __name__ == '__main__':
    menu()