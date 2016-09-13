#!/usr/bin/env python
# coding:utf-8

"""
connect mysql instance
"""
import os, sys, string
import MySQLdb

#     reload(sys)
#     sys.setdefaultencoding('utf-8')

DBhost = "192.168.1.165"
DBuser = "root"
DBpasswd = "mysql"
DBport = 3306
DBbase = "pytest"
DBcharset = "utf8"
query="select * from users"
update="update users set password='ERT' where id=4"

class Connect_mysql(object):
    def __init__(self, host, user, passwd, port, db, charset):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.charset = charset
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,port=self.port,db=self.db,charset=self.charset)
            self.cur = self.conn.cursor()
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self):
        try:
            self.cur.execute(query)
            self.result=self.cur.fetchall()
            self.desc=self.cur.description
            self.rows=self.cur.rowcount
            return self.result,self.desc,self.rows

        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def update(self):
        try:
            result=self.cur.execute(update)
            if result==1:
                up=True
            else:
                up=False
            return up
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    s = Connect_mysql(DBhost, DBuser, DBpasswd, DBport, DBbase, DBcharset)
    #result=s.update()
    #s.commit()
    #查询展示
    data=s.query()[0]
    desc=s.query()[1]
    count=s.query()[2]
    s.close()
    print "%s %10s %10s %10s" %(desc[0][0],desc[1][0],desc[2][0],desc[3][0])
    for row in data:
        print "%2s %10s %10s %10s" %row

    print "total rows:%s" %count
