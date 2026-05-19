import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shasmeem_786786",
    database="company"
)

print("Connected successfully!")
mycursor = mydb.cursor()

def CreateTable():
    TableName = input("Enter table name: ")
    columnCount = int(input("How many columns do you want to add?" \
    "nNote: 'id' column with INT AUTO_INCREMENT PRIMARY KEY will be added by default.\n"))
    columns = [
        "id INT AUTO_INCREMENT PRIMARY KEY"
    ]
    for i in range(columnCount):
        columnName = input(f"Enter name for column {i+1}: ")
        columnType = input(f"Enter datatype for {columnName} (VARCHAR(255), INT, FLOAT, etc): ")
        columns.append(f"{columnName} {columnType}")
    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {TableName} ({", ".join(columns)})")
    print(f"Table '{TableName}' created and data inserted successfully!")
    
    
def InsertData():
    mycursor.execute("SHOW TABLES")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber = int(input("Enter table number corresponding to the table you want to insert data into(1-{}): ".format(len(myresult))))
    tableName = myresult[tableNumber-1][0]
    mycursor.execute(f"SHOW COLUMNS FROM {tableName}")
    columns = mycursor.fetchall()
    columnNames = []
    values = []
    for column in columns:
        if column[0] == "id":
            continue
        value = input(f"Enter the data for {column[0]}: ")
        columnNames.append(column[0])
        values.append(value)
    sql = f"INSERT INTO {tableName} ({', '.join(columnNames)}) VALUES ({', '.join(['%s'] * len(values))})"
    mycursor.execute(sql, values)
    mydb.commit()
    print("Data inserted successfully!")
    mycursor.execute(f"SELECT * FROM {tableName}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    
def UpdateData():
    mycursor.execute("SHOW TABLES") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber= int(input("Enter table number corresponding to the table you want to insert data into(1-{}): ".format(len(myresult))))
    tableName = myresult[tableNumber-1][0]
    mycursor.execute(f"SELECT * FROM {tableName}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    id = int(input("Enter id: "))
    print("What column do you want to update?")
    mycursor.execute(f"SHOW COLUMNS FROM {tableName}")
    columns = mycursor.fetchall()
    for x in columns:
        print(x)
    column = int(input("Enter the number of the column you want to update(1-{}): ".format(len(columns))))
    newValue = input("Enter new value for {columns[column-1][0]}: ")
    sql = f"UPDATE {tableName} SET {columns[column-1][0]} = %s WHERE id = %s"
    val = (newValue, id)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute(f"SELECT * FROM {tableName}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def DisplayData():
    mycursor.execute("SHOW TABLES") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber = int(input("Enter table number corresponding to the table you want to display data from(1-{}): ".format(len(myresult))))
    tableName = myresult[tableNumber-1][0]
    if tableName not in [x[0] for x in myresult]:
        print(f"Table '{tableName}' does not exist.")
        return
    mycursor.execute(f"SELECT * FROM {tableName}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def DeleteData():
    mycursor.execute("SHOW TABLES") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber = int(input("Enter table number corresponding to the table you want to delete data from(1-{}): ".format(len(myresult))))
    if tableNumber not in range(1, len(myresult) + 1):
        print("Invalid table number. Operation cancelled.")
        return
    tableName = myresult[tableNumber-1][0]
    mycursor.execute(f"SELECT * FROM {tableName}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    id = int(input("Enter id to delete: "))
    confirmation = input(f"Are you sure you want to delete this record from '{myresult[tableNumber-1][0]}'? (yes/no): ")
    if confirmation.lower() != "yes":
        print("Operation cancelled.")
        return
    sql = f"DELETE FROM {tableName} WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute(f"SELECT * FROM {tableName}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def DropTable():
    mycursor.execute("SHOW TABLES") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber = int(input("Enter table number corresponding to the table you want to drop(1-{}): ".format(len(myresult))))
    if tableNumber not in range(1, len(myresult) + 1):
        print("Invalid table number. Operation cancelled.")
        return
    confirmation = input(f"Are you sure you want to drop '{myresult[tableNumber-1][0]}'? This action cannot be undone. (yes/no): ")
    if confirmation.lower() != "yes":
        print("Operation cancelled.")
        return
    tableName = myresult[tableNumber-1][0]
    mycursor.execute(f"DROP TABLE IF EXISTS {tableName}")
    print(f"Table '{tableName}' dropped if it existed.")

def AddColumn():
    mycursor.execute("SHOW TABLES") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber = int(input("Enter table number corresponding to the table you want to add a column to(1-{}): ".format(len(myresult))))
    tableName = myresult[tableNumber-1][0] 
    columnName = input("Enter column name: ")
    columnType = input("Enter column type (e.g., VARCHAR(255), INT): ")
    sql = f"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnType}"
    mycursor.execute(sql)
    print(f"Column '{columnName}' added to '{tableName}' successfully.")

def TruncateTable():
    mycursor.execute("SHOW TABLES") 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    tableNumber = int(input("Enter table number corresponding to the table you want to truncate(1-{}): ".format(len(myresult))))
    if tableNumber not in range(1, len(myresult) + 1):
        print("Invalid table number. Operation cancelled.")
        return
    confirmation = input(f"Are you sure you want to truncate '{myresult[tableNumber-1][0]}'? This action cannot be undone. (yes/no): ")
    if confirmation.lower() != "yes":
        print("Operation cancelled.")
        return
    tableName = myresult[tableNumber-1][0]
    mycursor.execute(f"TRUNCATE TABLE {tableName}")
    print(f"Table '{tableName}' truncated successfully.")

while True:
    print("<-------------Database Operations:------------>")
    InputValue = int(input("Enter the operation you want to perform for Table Data Management:\n"\
    "1. Create Table\n2. Insert data into Table\n3. Update data in Table\n4. Display data from Table\n5. Delete data from Table\n6. Drop Table\n7. Add Column\n8. Truncate Table\n0. Exit\n" \
    "<--------------------------------------------->" \
    "\nYour choice: "))
    
    operations = {
        1: CreateTable,
        2: InsertData,
        3: UpdateData,
        4: DisplayData,
        5: DeleteData,
        6: DropTable,
        7: AddColumn,
        8: TruncateTable
    }

    if InputValue == 0:
        print("Exiting the program.")
        break
    elif InputValue not in range(0, 9):
        print("Invalid choice. Please enter a number between 0 and 8.")
    else:
        operations[InputValue]()
