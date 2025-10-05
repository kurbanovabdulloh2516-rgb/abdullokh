import sqlite3

connect = sqlite3.connect('footbal.db') # 
cursor = connect.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    nikname TEXT,
    age INTEGER,
    club TEXT,
    goal INTEGER,
    assint INTEGER,
    liga_champion INTEGER,      
    la_liga INTEGER,
    world_cup  INTEGER,
    ballan_dor INTEGER,
    golden_boots INTEGER
)
''')



# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('lionel', 'messi', 38, 'inter miami', 850, 380, 4, 10, 2022, 8, 6))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('cristiano', 'ronaldo', 40, 'al nasr', 940, 300, 5, 2, 0, 5, 4))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('robert', 'lewandowski', 37, 'barcelona', 600, 150, 1, 1, 0, 0, 2))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('karim', 'benzema', 37, 'al ittihad', 450, 180, 5, 4, 0, 1, 0))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('kylian', 'mbappe', 27, 'real madrid', 300, 120, 0, 0, 2018, 0, 1))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('neymar', 'neymar jr', 33, 'al hilal', 400, 250, 1, 2, 0, 0 ,0))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('mohamed', 'salah', 33, 'liverpool', 300, 120, 1, 0, 0, 0, 0))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('luka', 'modric', 40, 'as milan', 150, 130, 6, 3, 0, 1, 0))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('kevin', 'de bruyne', 34, 'man.city', 150, 250, 1, 0, 0, 0, 0))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('erling', 'haaland', 25, 'man.city', 200, 50, 1, 0, 0, 0, 1))
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('vinicius', 'vini jr', 25, 'real madrid', 100, 70, 2, 2, 0, 0, 0))
#

# connect.commit()

# cursor.execute("DELETE FROM users WHERE id=?", (11 ,))
# connect.commit()
# cursor.execute('INSERT INTO users (name, nikname, age, club, goal, assint, liga_champion, la_liga, world_cup, ballan_dor, golden_boots) VALUES (?,?,?,?,?,?,?,?,?,?,?)',('aslan', 'ars', 19, 'barcelona', 700, 400, 3, 7, 0, 5, 5))

# connect.commit()


# cursor.execute('SELECT * FROM users')
# vbn = cursor.fetchall()
# for vbn in vbn:
#     print(vbn)

# connect.commit()


cursor.execute("""
UPDATE users 
SET name=?, nikname=?, age=?, club=?, goal=?, assint=?, liga_champion=?, la_liga=?, world_cup=?, ballan_dor=?, golden_boots=?
WHERE id=?
""", ('abdullokh', 'kurbanov jr', 14, 'real madrid', 400, 200,
      7, 5, 2, 9, 7, 12))

connect.commit()