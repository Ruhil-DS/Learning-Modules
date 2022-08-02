import psycopg2 as pg
import os
import sys

# Setting up the connection
conn = None
try:
    input_db = sys.argv[1]
    user = os.environ.get('PGUSER')
    pwd = os.environ.get('PGPASSWORD')
    host1 = os.environ.get('PGHOST')
    port1 = os.environ.get('PGPORT')
    conn = pg.connect(database = input_db,
                      user = user,
                      password = pwd,
                      host = host1,
                      port = port1)
except:
    print("okay lol")


def isprime(n):
    if n < 2:
        return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True


# creating a curson
cur = conn.cursor()

# Executing SQL using the cursor

statement1 = '''
select jersey_no
from players'''

cur.execute(statement1)

rows = cur.fetchall()

prime_jersey = []
for row in rows:
    if isprime(row[0]):
        prime_jersey.append(row[0])

statement2 = '''
SELECT p.name, t.name, p.jersey_no
FROM players p, teams t
WHERE p.jersey_no IN {prime_jersey}
and p.team_id = t.team_id
ORDER BY p.name DESC, t.name DESC
'''.format(prime_jersey=tuple(prime_jersey))

cur.execute(statement2)

rows = cur.fetchall()

for row in rows:
    print(row[0] + ", " + row[1])

cur.close()
conn.close()
