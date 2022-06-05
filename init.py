#for initalize service
#connect to excle
  #load adjection
from openpyxl import load_workbook
EXCLEconnect=load_workbook("")
#connect to db
import cx_Oracle
ID="user"
PASSWORD="1234"
LOCALHOST="localhost/orcl"
DBconnect=cx_Oracle.conenct(ID,PASSWORD,LOCALHOST)
cursur=DBconnect.cursor()
