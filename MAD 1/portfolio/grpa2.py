import psycopg2
import os
import sys
import math
import string

f = open("parameter.txt",'r')
char = f.readline()

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
cur.execute(f"select SUM(host_team_score) \
            from matches inner join teams on matches.host_team_id = teams.team_id \
            where host_team_score > guest_team_score and teams.name LIKE '{char}%'")
rows = cur.fetchall()
S = rows[0][0]
X = round(math.cos((S*10)*(math.pi/180)),2)
print(X)
cur.close()