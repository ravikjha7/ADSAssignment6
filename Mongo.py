import pymongo
from tkinter import *
# Create a connection to MongoDB
client = pymongo.MongoClient("mongodb+srv://akshu02:akshata@cluster0.tiqxbn7.mongodb.net/?retryWrites=true&w=majority")
# Create a database
db = client["ads9"]
# Create a collection
collection = db["student"]


# Function to insert data into MongoDB
def insert_data():
    name = name_entry.get()
    age = age_entry.get()
    prn =prn_entry.get()
    mydict = {"Student Name": name, "Age": age, "prn":prn}
    x = collection.insert_one(mydict)
    print(x.inserted_id)
    


# Function to find data in MongoDB
def find_data():
    name = name_entry.get()
    query = {"name": name}
    result = collection.find_one(query)
    print(result)


# Function to update data in MongoDB
def update_data():
    name = name_entry.get()
    age = age_entry.get()
    prn=prn_entry.get()
    query = {"name": name}
    newvalues = {"$set": {"age": age},
                 "$set" :{"prn":prn}
                 }
    collection.update_one(query, newvalues)


# Function to delete data from MongoDB
def delete_data():
    name = name_entry.get()
    query = {"name": name}
    collection.delete_one(query)


# Create a GUI
root = Tk()
root.geometry("800x800")
root.configure(background = "#29f8ff")

name_label = Label(root, text="Name")
name_label.pack(pady=6)

name_entry = Entry(root)
name_entry.pack(pady=6)

prn_label = Label(root, text="PRN NO")
prn_label.pack(pady=6)

prn_entry = Entry(root)
prn_entry.pack(pady=6)

age_label = Label(root, text="Age")
age_label.pack(pady=6)

age_entry = Entry(root)
age_entry.pack(pady=6)

insert_button = Button(root, text="Insert", command=insert_data,background="grey", foreground="white", border=9)
insert_button.pack(pady=6)

find_button = Button(root, text="Find", command=find_data,background="grey", foreground="white", border=9)
find_button.pack(pady=6)

update_button = Button(root, text="Update", command=update_data,background="grey", foreground="white", border=9)
update_button.pack(pady=6)

delete_button = Button(root, text="Delete", command=delete_data,background="grey", foreground="white", border=9)
delete_button.pack(pady=6)

root.mainloop()