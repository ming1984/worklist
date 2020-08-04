import sqlite3
def tianqi(month,day):
    m,d = day_str(month,day)
    conn=sqlite3.connect('D:\Mystuff\weather\weather.db')
    cur=conn.cursor()
    cur.execute('select AVG(最高温度),AVG(最低温度),MAX(最高温度),MAX(最低温度) from TQ where 日期 like "%-{}-{}" '.format(m,d))
    data=cur.fetchone()
    high = str(round(data[0],2))
    low = str(round(data[1],2))
    
    max_high = data[2]
    max_low = data[3]
    conn.commit()
    cur.close()
    conn.close()

    return high,low,max_high,max_low


def day_str(month,day):
    if day < 10:
        res2 = '0'+str(day)
    else:
        res2 = str(day)
    if month < 10:
        res1 = '0'+str(month)
    else:
        res1 = str(month)
    return res1,res2

if __name__=="__main__":
	high,low,max_high,max_low=tianqi(5,29)
	print(high,low)
	print(max_high,max_low)
	
