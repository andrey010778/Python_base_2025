# import pymysql
#
# try:
#     connection = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user='andrey',
#         password='qwerty',
#         database="flights",
#         )
#     print(connection)
# except Exception as ex:
#     print('Connection Error')
#     print(ex)
# with connection.cursor() as cursor:
#     sql = 'select * from flights.airlines limit 10'
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for i in result:
#         print(i)

import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password='admin', host='localhost')
print("Подключение установлено")
cursor = conn.cursor()

try:
    conn.autocommit = True
    # команда для создания базы
    sql = "CREATE DATABASE t_input_test"

    # выполняем код sql
    cursor.execute(sql)
    print("База данных успешно создана")
except Exception:
    print("База данных уже существует")


conn = psycopg2.connect(dbname="t_input_test", user="postgres", password='admin', host='localhost')
print("Подключение установлено")
cursor = conn.cursor()

cursor.execute("create table if not exists t_input_test (id serial primary key, name varchar(50), age integer)")
conn.commit()


def add_record():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    query = "insert into t_input_test (name, age) values (%s, %s)"
    cursor.execute(query, (name, age))
    conn.commit()

def update_record():
    try:
        # Показ всех записей
        show_all()
        # Запрос данных от пользователя
        record_id = input("Введите ID записи, которую хотите отредактировать: ")
        new_value = input("Введите новое значение для записи: ")

        #Получение списка столбцов
        query = "select column_name from information_schema.columns where table_name = 't_input_test'"
        cursor.execute(query)
        list_column_name = cursor.fetchall()
        print([column[0] for column in list_column_name])

        column_name = input("Введите название столбца, который хотите обновить: ")

        # Формирование SQL-запроса
        query = f"UPDATE t_input_test SET {column_name} = %s WHERE id = %s"

        # Выполнение SQL-запроса
        cursor.execute(query, (new_value, record_id))

        # Подтверждение изменений
        conn.commit()
        print("Запись успешно обновлена!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        conn.rollback()

def delete_record():
    # Подсчет общего количества записей
    query1 = "select count(*) from t_input_test"
    cursor.execute(query1)
    row_count = cursor.fetchone()[0]
    print(f'Количество записей в таблице всего {row_count}')
    # Вывод всех записей
    print("Список записей: ")
    show_all()
    # Пользовательский ввод
    record_id = input("Введите ID записи для удаления: ")

    # SQL-запрос для удаления записи
    query = "DELETE FROM t_input_test WHERE id = %s"

    try:
        # Выполнение SQL-запроса
        cursor.execute(query, (record_id,))

        # Подтверждение изменений
        conn.commit()

        print(f"Запись с ID {record_id} успешно удалена.")

    except Exception as e:
        # Откат изменений в случае ошибки
        conn.rollback()
        print(f"Ошибка при удалении записи: {e}")

    # cursor.execute("ALTER SEQUENCE t_input_test_id_seq RESTART WITH 1")
    # conn.commit()
    # cursor.close()
    # conn.close()


def show_all():
    # Показ всех записей в таблице
    cursor.execute("SELECT * FROM t_input_test")
    list = cursor.fetchall()
    print('Таблица записей: ')
    for data in list:
        print(data)

def conn_close():
    # При выходе закрываем курсор и подключение к БД
    cursor.close()
    conn.close()


