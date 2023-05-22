from tkinter import *
from cassandra.cluster import Cluster

# Establish connection to Cassandra
cluster = Cluster(['localhost'])  # Replace 'localhost' with your Cassandra cluster address
print(cluster)
session = cluster.connect('friends')  # Replace 'your_keyspace' with your keyspace name

# CRUD functions
def create_data():
    id = int(id_entry.get())
    name = name_entry.get()
    age = int(age_entry.get())
    address = address_entry.get()

    session.execute("INSERT INTO friends_circle (id,name,age,address) VALUES (%s, %s,%s,%s)", (id,name,age,address))

def read_data():
    result_set = session.execute("SELECT * FROM friends_circle")
    for row in result_set:
        print(row.id,row.name,row.age,row.address) 

def update_data():
    id=int(id_entry.get())
    name = name_entry.get()
    age = int(age_entry.get())
    address=address_entry.get()
    # Execute UPDATE statement to modify data in Cassandra
    session.execute("UPDATE friends_circle SET age = %s WHERE id = %s", (age,id))

def delete_data():
    id = int(id_entry.get())
    # Execute DELETE statement to remove data from Cassandra
    session.execute("DELETE FROM friends_circle WHERE id= %s", (id,))

# GUI setup
root = Tk()
root.title("Cassandra CRUD")
root.geometry("300x200")

# Labels
id_label = Label(root, text="id:")
id_label.pack()
name_label = Label(root, text="Name:")
name_label.pack()
age_label = Label(root, text="age:")
age_label.pack()
address_label = Label(root, text="Address:")
address_label.pack()


# Entry fields
id_entry = Entry(root)
id_entry.pack()
name_entry = Entry(root)
name_entry.pack()
age_entry = Entry(root)
age_entry.pack()
address_entry = Entry(root)
address_entry.pack()

# Buttons
create_button = Button(root, text="Create", command=create_data)
create_button.pack()
read_button = Button(root, text="Read", command=read_data)
read_button.pack()
update_button = Button(root, text="Update", command=update_data)
update_button.pack()
delete_button = Button(root, text="Delete", command=delete_data)
delete_button.pack()

root.mainloop()
