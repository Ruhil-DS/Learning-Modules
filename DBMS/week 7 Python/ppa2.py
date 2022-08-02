import psycopg2
import os
import sys

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

curr = conn.cursor()

statement = '''
SELECT t.team_id
FROM teams t
WHERE t.jersey_home_color <> t.jersey_away_color
ORDER BY t.team_id ASC;
'''
curr.execute(statement)

def alpha_encoder(s):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = alpha.index(s)
    return alpha[((index+7)%26)]

def num_encoder(n):
    return (n+7)%10

rows = curr.fetchall()


for row in rows:
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''
    for i in row[0]:
        if i in alpha:
            cipher = alpha_encoder(i)
            output += cipher
        else:
            cipher = num_encoder(int(i))
            output += str(cipher)
    print(output)

curr.close()
conn.close()
