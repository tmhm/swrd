# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def add_list(p):
    p1 = p +[5,6]
    p = p + [5,6]

p1 = [1,2,3]
add_list(p1)
print p1

a = []
b = {'num':0, 'sqrt':0}
resurse = [1,2,3]
for i in resurse:
  b['num'] = i
  b['sqrt'] = i * i
  d = b.copy()
  a.append(b)
  #a.append(d)
print "a: ",a

c=[]
for i in resurse:
    c.append({"num":i, "sqrt":i*i})
print "c: ",c

#def hello():
#    """Print "Hello World" and return None"""
#    print("Hello World")

# main program starts here


def hello(name):
    """Given an object 'name', print 'Hello ' and the object."""
    print("Hello {}".format(name))

# need  net start mysql
import pymysql 

def  connDB():                              #连接数据库
    conn=pymysql.connect(host="localhost",user="root",passwd="mysql2",\
    db="xwei",charset="utf8")
    cur=conn.cursor()
    return (conn,cur)

def exeUpdate(conn,cur,sql):                #更新或插入操作
    try:
        sta=cur.execute(sql)
        conn.commit()
        print("update succeed")
        return (sta)
    except Exception:
        print("update failure")

def exeDelete(conn,cur,IDs):                #删除操作
    sta=0;
    for eachID in IDs.split(' '):
        sta+=cur.execute("delete from students where Id=%d"%(int(eachID)))
    conn.commit()
    return (sta)
        
def exeQuery(cur,sql):                      #查找操作
    cur.execute(sql)
    return (cur)
    
def connClose(conn,cur):                    #关闭连接，释放资源
    cur.close()
    conn.close()


if __name__ == "__main__":
    
    try:
        #exeUpdate(conn, cur, sql);
        conn,cursor = connDB()
        
        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS GD_TRAIN_DATA")
        
        # 创建数据表SQL语句
        sql = """CREATE TABLE GD_TRAIN_DATA (
                 USE_CITY  VARCHAR(2) NOT NULL,
                 LINE_NAME  VARCHAR(4),
                 TERMINAL_ID VARCHAR(32),  
                 CARD_ID VARCHAR(32),  
                 CREATE_CITY VARCHAR(2),     
                 DEAL_TIME VARCHAR(10),   
                 CARD_TYPE VARCHAR(4))"""
                 
        cursor.execute(sql)
                 
        #        cursor = exeQuery(cursor,"select version()")
        #        row = cursor.fetchone()
        #        print "server version:",row[0]
        #        print("查询成功")
        
        connClose
               
    except Exception:
        print("查询失败")
      
      
      
      
      
      
      
      
      
      
      