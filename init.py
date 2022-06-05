#for initalize service
#connect to db

#import cx_Oracle
ID="sys"
PASSWORD="1234"
LOCALHOST="localhost/orcl"
#DBconnect=cx_Oracle.connect(ID,PASSWORD,LOCALHOST)
#cursur=DBconnect.cursor()
#connect to excle
import struct
from openpyxl import load_workbook
  #load adjection
EXCLEConnect=load_workbook("./mbti_adjectives.xlsx",data_only=True)
loadSheet=EXCLEConnect['Sheet1']
start='A3'
end='B4'#B348
getCells=loadSheet[start:end]
for row in getCells:
  print(row[0].value)#adjective
  print(row[1].value)#MBTI

  #load name
EXCLEConnect=load_workbook("./name_gender_dataset.xlsx",data_only=True)
loadSheet=EXCLEConnect['Worksheet']
start='A2'
end='B3'#B147270
getCells=loadSheet[start:end]
for row in getCells:
  print(row[0].value)#name
  print(row[1].value)#gender
  #load question
EXCLEConnect=load_workbook("./MBTI_question.xlsx",data_only=True)
MBTIType=['M','B','T','T']
loadSheet=EXCLEConnect[MBTIType[0]]
start='A2'
end='C3'
getCells=loadSheet[start:end]
for row in getCells:
  print(row[0].value)#question
  print(row[1].value)#answer1

