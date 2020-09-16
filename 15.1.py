import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    (name, corp) = email.split('@')
    print(name, corp)

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (corp,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)', (corp,))
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?', (corp,))
conn.commit()
cur.close()
