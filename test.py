#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import hashlib
import random

name = input('entrer un pseudo')
entree = input('entrer un mdp')

salt = random.randint(1,1000)
mdp = hashlib.sha512(str(salt).encode('utf-8') + entree.encode('utf-8')).hexdigest()


conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    mdp TEXT,
    salt TEXT
)
""")
conn.commit()


cursor.execute("""
INSERT INTO users(name, mdp, salt ) VALUES(?, ?, ?)""",(name, mdp, salt))


cursor.execute("""SELECT name, mdp, salt FROM users""")


user1 = cursor.fetchone()
print(user1[1])
print(entree)

newentree = input('entrer de nouveaux le mdp')
if user1[1] == hashlib.sha512(str(user1[2]).encode('utf-8') + newentree.encode('utf-8')).hexdigest() :
    
    print('ok')
else:
    print('pas ok')

conn.close()



