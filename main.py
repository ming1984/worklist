# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:28:55 2019

@author: gaoyanming
"""
import sys
import richang
import per_month
import quarter_year
import guowai
import other
def main():
    while True:
        print('|------------------菜---单---------------------|')
        print('|1:日常                                        |')
        print('|2:每月                                        |')
        print('|3:季度、年                                    |')
        print('|4:国外采购                                    |')
        print('|5:其    它                                    |')
        print('|q:退出                                        |')
        print('|----------------------------------------------|')        
        choice = input('请输入选项：')
        if choice == '1':
            richang.menu()
        elif choice =='2':
            per_month.menu()
        elif choice =='3':
            quarter_year.menu()
        elif choice =='4':
            guowai.menu()
        elif choice =='5':
            other.menu()
        elif choice =='q':
            sys.exit(1)
        else:
            print('输入错误！请输入正确的选项。')

if __name__ == '__main__':
    main()