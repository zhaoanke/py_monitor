
import pymysql
db = pymysql.connect(user="root", passwd="zak@123456", db="monitor", host="1.117.176.78")
cur = db.cursor()
 
# from sqlalchemy import create_engine
# engine = create_engine(
#     "mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")
# print(engine)
  
 
# 创建数据表--系统信息监控
sql="""CREATE TABLE IF NOT EXISTS system_info(
     ID int(8) not null auto_increment COMMENT '序号',
     TIME datetime not null COMMENT '记录时间',
     mem_free VARCHAR (100) NOT NULL COMMENT '可用内存',
     mem_total VARCHAR (100) NOT NULL COMMENT '总内存',
     mem_percent VARCHAR (100) NOT NULL COMMENT '内存百分比',
     mem_used VARCHAR (100) NOT NULL COMMENT '占用内存',
     cpu VARCHAR (100)  COMMENT 'CPU占比',
     disk1 VARCHAR (100)  COMMENT 'C盘使用占比',
     disk2 VARCHAR (100)  COMMENT 'D盘使用占比',
     primary key(ID)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT = '系统信息监控'
"""
cur.execute(sql)
cur.close()