#A small tool to export sqlite database to a mysql server by table name;
#charset=utf-8
import MySQLdb
import re
import sqlite3

#configuration

sqlite_path='./data.db'
mysql_connect_args={
 'host':''
,'user':''
,'passwd':'' 
,'db':''     
,'port':      
,'charset':''} #conplete it yourself.
sqlite_table_name='User'

#end of configuration
###############################################
#init of connection to the sqlite database

sqlite_conn=sqlite3.connect(sqlite_path)
sqlite_cur=sqlite_conn.cursor()

#end of init the connection
###############################################
#init of connection to  the MySQL database
try:
	mysql_conn=MySQLdb.connect(host=mysql_connect_args['host']
		,user=mysql_connect_args['user']
		,passwd=mysql_connect_args['passwd']
		,db=mysql_connect_args['db']
		,port=mysql_connect_args['port'],charset=mysql_connect_args['charset'])
	mysql_cur=mysql_conn.cursor()
except MySQLdb.Error,e:
	print(e.args)

#end of init the connection
##################################################
#init the table of MySQL database:

table=sqlite_cur.execute('select sql  from sqlite_master where type=\'table\'and name=\''+sqlite_table_name+'\'')
for line in table:
	table_init_sql=line[0]
try:
	mysql_cur.execute(table_init_sql)
except MySQLdb.Error,e:
	print(e.args)

#end of table init
#################################################
#copy data from sqlite to MySQL server

raws=sqlite_conn.execute('select * from '+sqlite_table_name)

for line in raws:
	mysql_insert_sql='insert into '+sqlite_table_name+'  values('
	index=1
	for item in line:
		item='\''+item+'\''
		if index==1:
			mysql_insert_sql=mysql_insert_sql+item
		if index==0:
			mysql_insert_sql=mysql_insert_sql+','+item
		index=0
	mysql_insert_sql=mysql_insert_sql+')'
	try:
		mysql_cur.execute(mysql_insert_sql)
	except MySQLdb.Error ,e :
		print(e.args)
#end of data copy
mysql_conn.commit()
mysql_cur.close()
mysql_conn.close()






