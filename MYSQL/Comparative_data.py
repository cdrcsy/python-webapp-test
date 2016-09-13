#!/usr/bin/env python
# coding:utf-8

"""
Comparative data from different mysql。
"""
import os, sys, string
import MySQLdb

query = "select * from users"

config_1 = {
    'host': '192.168.1.165',
    'port': 3306,
    'user': 'root',
    'passwd': 'mysql',
    'db': 'pytest',
    'charset': 'utf8'
}

config_2 = {
    'host': '192.168.1.165',
    'port': 3306,
    'user': 'root',
    'passwd': 'mysql',
    'db': 'test',
    'charset': 'utf8'
}

class ConnectMYSQL(object):
    """
    初始化相互比较的2个库的连接对象，游标
    对比两个表的数据是否一致。
    """
    def __init__(self):
        try:
            self.conn_1 = MySQLdb.connect(**config_1)
            self.cur_1 = self.conn_1.cursor()
            self.conn_2 = MySQLdb.connect(**config_2)
            self.cur_2 = self.conn_2.cursor()
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

# 查询1对象
    def query_1(self):
        try:
            self.cur_1.execute(query)
            count_1 = self.cur_1.rowcount
            desc_1 = self.cur_1.description
            result_1 = self.cur_1.fetchall()
            return result_1, desc_1,count_1

        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

# 查询2对象
    def query_2(self):
        try:
            self.cur_2.execute(query)
            count_2 = self.cur_2.rowcount
            desc_2 = self.cur_2.description
            result_2 = self.cur_2.fetchall()
            return result_2,desc_2,count_2
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


# chuck判断，chuck不同的，需要进行行比较

    def chuck_check(self):
        data_1 = self.query_1()[0]
        data_2 = self.query_2()[0]

        if cmp(data_1,data_2) == 0:
             return True
        else:
            row_1 = [val for val in data_1 if val not in data_2]
            row_2 = [val for val in data_2 if val not in data_1]
            return row_1, row_2

# 查询数据格式化输出

    def format_out(self, result, column, count):
        self.result = result
        self.column = column
        self.count = count
        print "==============================="
        desc = ([self.column[x][0] for x in range(len(self.column))])
        for i in desc:
            print "%s"%i+'     ',

        print '\r'
        for y in range(len(self.result)):
            for z in range(len(self.column)):
                print str(self.result[y][z]) + '       ',
            print '\r'
        print "total rows :%s" % self.count

    def close(self):
        self.cur_1.close()
        self.cur_2.close()
        self.conn_1.close()
        self.conn_2.close()


if __name__ == "__main__":
    s = ConnectMYSQL()
    t=s.chuck_check()
    for row in t:
        print row
    result=s.query_1()[0]
    column = s.query_1()[1]
    count=s.query_1()[2]
    desc=s.format_out(result,column,count)
    s.close()

# 输出的data的行，类似如下：tuple
#((1L, u'qiwsir', u'123123', u'qiwsir@gmail.com'), (2L, u'python', u'123456', u'python@gmail.com'))
#((1L, u'qiwsir', u'123123', u'qiwsir@gmail.com'), (2L, u'python', u'123456', u'python@gmail.com'))

#比较这两个元组，是否相等。返回0才是完全相等。此方法可以结合 分块方法，每次对块tuple进行对比。
#达到快速校验数据一致的目的。如果块不一致，就需要进行 行比较，最后输出，不一致的行。





"""
格式化，数据输出：
    print "=============第一部分==============="
    print "%s %10s %10s %10s" % (desc_1[0][0], desc_1[1][0], desc_1[2][0], desc_1[3][0])
    for row_1 in data_1:
        print "%2s %10s %10s %10s" % row_1
    print "total rows:%s" % count_1

    print "=============第二部分==============="
    print "%s %10s %10s %10s" % (desc_2[0][0], desc_2[1][0], desc_2[2][0], desc_2[3][0])
    for row_2 in data_2:
        print "%2s %10s %10s %10s" % row_2
    print "total rows:%s" % count_2
"""