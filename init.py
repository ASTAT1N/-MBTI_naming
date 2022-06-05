#for initalize service
#connect to db
import cx_Oracle
ID="user"
PASSWORD="1234"
LOCALHOST="localhost/orcl"
connect=cx_Oracle.conenct(ID,PASSWORD,LOCALHOST)
cursur=connect.cursor()
