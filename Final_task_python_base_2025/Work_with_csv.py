import psycopg2
import csv

def insert_csv_to_postgres(csv_file_path, db_config, table_name):
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        print("Connection with base success")

        with open(csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            columns = ','.join(header)
            placeholders = ','.join(['%s']*len(header))
            query = f"insert into {table_name} ({columns}) values ({placeholders})"
            for row in reader:
                cursor.execute(query, row)
            conn.commit()
            print('Data add success')
    except Exception as e:
        print(f"Error: {e}")

        if conn:
            cursor.close()
            conn.close()
            print("Connection with database closed ")


if __name__ == "__main__":
    db_config = {"host": "localhost", "dbname": "t_input_test", "user": "postgres", "password":"admin", "port": 5432}
    csv_file_path = "Name_age.csv"
    table_name = "t_input_test"
    insert_csv_to_postgres(csv_file_path, db_config, table_name)
