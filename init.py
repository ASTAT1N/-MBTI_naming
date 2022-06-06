#for initalize service
#connect to db
import cx_Oracle
ID="system"
PASSWORD="Na123456"
LOCALHOST="localhost/orcl"
DBconnect=cx_Oracle.connect(ID,PASSWORD,LOCALHOST)
cursor=DBconnect.cursor()
  #make DB of adjection
cursor.execute("""
CREATE TABLE adjection(
ID int,
adjective varchar2(100) NOT NULL,
MBTI varchar(4) NOT NULL
)
""")

  #make DB of name
cursor.execute("""
CREATE TABLE name(
ID int,
name varchar2(100) not null,
gender char(1) not null
)
""")

  #make DB of question
cursor.execute("""
CREATE TABLE question(
ID int,
type char(1) not null,
question varchar(500) not null,
answer1 char(1) not null,
answer2 char(1) not null
)
""")

