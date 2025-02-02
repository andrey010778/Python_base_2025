import psycopg2
from psycopg2 import sql
conn = psycopg2.connect(dbname="postgres", user="postgres", password='admin', host='localhost')
print("Подключение установлено")
cursor = conn.cursor()

conn.autocommit = True

sql = 'create database metanit'
cursor.execute(sql)
print('Create database success')


cursor.execute('create table if not exists people  (id serial primary key, name varchar(50), age integer)')
name = input('Введите имя')
age = int(input('Введите возрвст'))
cursor.execute("insert into people (name, age) values (%s, %s)", name, age)

conn.commit()

cursor.close()
conn.close()
