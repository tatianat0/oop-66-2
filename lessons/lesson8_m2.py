import sqlite3
from termios import CREAD

from HomeWork.homework5_m2 import user

connect= sqlite3.connect('grade.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS grade ('''
               CREATE TABLE IF NOT EXISTS users(
               id    

)

               ''')