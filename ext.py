# coding: utf-8 
import sqlite3
def chaxun1(name):
    conn = sqlite3.connect(r'D:\Database\data.db')
    cur = conn.cursor()
    cur.execute('select number from ext where name="{}"'.format(name))
    res = cur.fetchone()
    print('☆'*24,'\n')
    print(name,'的分机号是：',res[0],'\n')
    print('☆'*24)
    cur.close()
    conn.commit()
    conn.close()
def chaxun2(number):
    conn = sqlite3.connect(r'D:\Database\data.db')
    cur = conn.cursor()
    cur.execute('select name from ext where number="{}"'.format(number))
    res = cur.fetchone()
    print('☆'*24,'\n')
    print(number,'是',res[0],'的分机号','\n')
    print('☆'*24)
    cur.close()
    conn.commit()
    conn.close()
def chaxun_all():
    conn = sqlite3.connect(r'D:\Database\data.db')
    cur = conn.cursor()
    cur.execute('select * from ext')
    res = cur.fetchall()
    print('☆'*24,'\n')
    for r in res:
        print(r[0],':',r[1])
    print('\n','☆'*24)
    cur.close()
    conn.commit()
    conn.close()

def menu():
    print('|------------------ 分机号---------------------|')
    print('|1:按姓名查询                                  |')
    print('|2:按分机号查询                                |')
    print('|3:列出所有                                    |')
    print('|q:退出                                        |')
    print('|----------------------------------------------|')
    choice = input('请输入选项：')
    if choice == '1':
        name=input('请输入查询的姓名：')
        chaxun1(name)
    elif choice =='2':
        number=input('请输入查询的分机号：')
        chaxun2(number)
    elif choice =='3':
        chaxun_all()
    elif choice =='q':
        pass
    else:
        print('输入错误！请输入正确的选项。')

if __name__ == '__main__':
    while True:
        menu()
