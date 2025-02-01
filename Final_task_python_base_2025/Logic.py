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
conn = psycopg2.connect(dbname="Test", user="postgres", password='admin', host='localhost')
print("Подключение установлено")
cursor = conn.cursor()

def show_all():
    cursor.execute("SELECT * FROM test_input.t_input_test")
    print(cursor.fetchall())
    cursor.close()
    conn.close()


