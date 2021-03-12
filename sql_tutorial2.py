from os.path import join
from typing import NewType
import mysql.connector

# parameter is one user row data
def data_form(user_data_ary):

    print("User Primary id : {}\nUser name is : {}\nUser address is : {}\n".format(
        user_data_ary[2],user_data_ary[1],user_data_ary[0]
        )
    )
    return None

# Pass one data row to data_form function
def data_out_form(argment):

    for x in argment:
        data_form(x)

    return None

def mysql_data_formatting():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password",
    database = "mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    # If you are only interested in one row, you can use the fetchone() method.
    myresult = mycursor.fetchall()
    new_ary = []
    other_ary = []

    # Each data row is appending this for loop
    for x in range(5):
        new_ary.append(myresult[x])

    # when you use mycursor.fetchall function. you get the data tuple type.
    # This is because tuple type data is type-safe way of containing multiple value with multiple types

    # Third index in mydatabase db is integer type. so when you use this row
    # You should change data type tuple to string
    # Behind for loop makes it possible
    for y in range(5):
        string_ary = [str(x) for x in new_ary[y]]
        other_ary.append(string_ary)
    
    # sum(list, []) function makes 2nd list to integrate one list
    temp_string = sum(other_ary, [])

    data_out_form(other_ary)

def main():
    mysql_data_formatting()

if __name__ == '__main__':
    main()
    
# Creating a Database
# mycursor.execute("CREATE DATABASES dbname")

# check if Database Exists
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# Creating A Table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("CREATE TABLE merchandise (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")

# ALTER TABLE Keyword
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# One row insert to table
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ('lee', 'highway 21')
# mycursor.execute(sql, val)

# mydb.commit()
# # if you want to count table row number, use rowcount
# print(mycursor.rowcount, "record inserted.")

########## I use beyond data set
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit() // db commit은 반드시 해줘야 한다.
# print(mycursor.rowcount, "was inserted. ")