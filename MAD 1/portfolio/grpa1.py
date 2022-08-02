import psycopg2
import os
import sys
import string

f = open("date.txt",'r')
date = f.readline()

conn = None
input_db = sys.argv[1]
user = os.environ.get('PGUSER')
pwd = os.environ.get('PGPASSWORD')
host1 = os.environ.get('PGHOST')
port1 = os.environ.get('PGPORT')
conn = psycopg2.connect(database = input_db,
                        user =user,
                        password = pwd,
                        host = host1,
                        port = port1)
cur = conn.cursor()
cur.execute("select M.match_date, T.name \
            from matches M INNER JOIN match_referees P ON M.match_num = P.match_num\
            INNER JOIN referees T on P.referee = T.referee_id")
rows = cur.fetchall()
for row in rows:
    if str(row[0]) == date:
        name = row[1]
        L = []
        count = 0
        for i in name:
            count += 1
            if i == ' ':
                L.append(count)

        Output_name = ''
        for i in range(len(L)):
            if i == 0:
                Output_name = Output_name + name[L[-1]:] + " " + name[0] + "."
            else:
                Output_name = Output_name + " " + name[L[i - 1]] + "."

        print(Output_name)
cur.close()