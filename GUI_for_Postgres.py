import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        conn = psycopg2.connect(dbname="t_input_test", user="postgres", password='admin', host='localhost')
        return conn
    except Exception as e:
        messagebox.showerror("Error", f"Unable to connect to database {e}")
        return None

def fetch_data():
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("select * from t_input_test")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def add_data(name, age):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("insert into t_input_test (name, age) values (%s, %s)", (name, age))
        conn.commit()
        messagebox.showinfo("Success")
    except Exception as e:
        messagebox.showerror("Error", f"Can't add data: {e}")
    finally:
        cursor.close()
        conn.close()

def update_data(id, name, age):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute('update t_input_test set name = %s, age=%s where id = %s', (name, age, id))
        conn.commit()
        messagebox.showinfo("Success. Data update.")
    except Exception as e:
        messagebox.showerror(f'Error: Unable to update data: {e}')
    finally:
        cursor.close()
        conn.close()
def delete_data(id):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("Delete from t_input_test where id=%s", (id,))
    except Exception as e:
        messagebox.showerror("Error", f"Unable to delete data: {e}")
    finally:
        cursor.close()
        conn.close()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("List of person")

        # Input fields
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(root, text="Age")
        self.age_label.grid(row=1, column=0)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1)

        #Buttons
        self.add_button = tk.Button(root, text="Add record", command=self.add)
        self.add_button.grid(row=2, column=0)
        self.update_button = tk.Button(root, text="Update record", command=self.update)
        self.update_button.grid(row=2, column=1)
        self.delete_button = tk.Button(root, text="Delete record", command=self.delete)
        self.delete_button.grid(row=2, column=2)

        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=4, column=0, columnspan=3)
        self.refresh_list()

    def add(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        self.refresh_list()

    def update(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Choose record to update")
            return
        id = self.listbox.get(selected[0]).split()[0]
        name = self.name_entry.get()
        age = self.age_entry.get()
        update_data(id, name, age)
        self.refresh_list()

    def delete(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error choose record to delete")
        id = self.listbox.get(selected[0]).split()[0]
        delete_data(id)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        rows = fetch_data()
        for row in rows:
            self.listbox.insert(tk.END, f"{row[0]} {row[1]} {row[2]}")




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()