import pandas as pd
import numpy as np
df=pd.read_csv("data/Employee.csv")

def InsertSalary():
    n=int(input("Enter the salary you want to insert for all employees: "))
    df["Salary"]=n
    print(df["Salary"])
def AgeCategory(): 
    b=int(input("Enter the age threshold to categorize employees as Young or Senior: "))
    print("Creating Age Category based on Age column...")
    df["AgeCategory"] = np.where(df["Age"] < b, "Young", "Senior")
    print(df["AgeCategory"].value_counts())
def ReplaceCity():
    print("Current City Counts:\n", df["City"].value_counts())
    c=str(input("Enter the city name you want to replace: "))
    nc=str(input("Enter the new city name: "))
    df["City"] = df["City"].replace(c, nc)
    print(df["City"].value_counts())    
def SetAgeNull():
    a=int(input("Enter the index of the row for which you want to set Age to null: "))
    if pd.isnull(df.loc[a, "Age"]):
        print(f"Age is already null for index {a}.")
    else:
        df.loc[a,"Age"] = None
        print(f"Age has been set to null for index {a}.\n", df["Age"])
def CheckAgeNull():
    print(df["Age"].isnull().value_counts())
def FillAgeNull():
    print("Age mean before filling null values:", df["Age"].mean())
    print("Filling null values in Age column with mean...")
    df["Age"]=df["Age"].fillna(df["Age"].mean())
    print(df["Age"])
def DeleteColumn():
    print("Current columns in the DataFrame:\n", df.columns)
    colname=str(input("Enter the column name you want to delete: "))
    df.drop(columns=[colname], inplace=True)
    print(f"Column '{colname}' has been deleted. Current columns:\n", df.columns) 
def NewColumn():
    colname=str(input("Enter the name of the new column you want to create: "))
    df[colname]=0
    print(f"New column '{colname}' has been created with default value 0.\n", df.head())
def UpdateColumn():
    ColumnArray=df.columns.tolist()
    print("Current columns in the DataFrame:\n", ColumnArray)
    colname=int(input("Enter the number corresponding to the column you want to update: "))
    if 0 <= colname < len(df.columns):
        newvalue=int(input(f"Enter the new value(integer) you want to set for all rows in column '{df.columns[colname-1]}': "))
        df.iloc[:, colname-1] = newvalue
        print(f"Column '{df.columns[colname]}' has been updated with new value {newvalue}.\n", df.head())
    else:
        print(f"Column '{colname}' does not exist in the DataFrame.")
def SetNull():
    colname=str(input("Enter the name of the column you want to set to null: "))
    if colname in df.columns:
        df[colname]=None
        print(f"Column '{colname}' has been set to null.\n", df.head())
    else:
        print(f"Column '{colname}' does not exist in the DataFrame.")


while True:
    print("\n<--------------Data Manipulation Menu:-------------->")
    valueInput=int(input("Enter the number corresponding to the operation you want to perform:" \
"\n1. Insert Salary\n2. Create Age Category\n3. Replace City Name\n4. Set Age to Null\n5. Check for Null Values in Age\n6. Fill Null Values in Age with Mean\n7. Delete Column\n8. Create New Column\n9. Update Column\n10. Set Column to Null\n0. Exit\n" \
"---------------------------------------------------------\n" \
"Your Choice: "))
    operations={
    1:InsertSalary,
    2:AgeCategory,
    3:ReplaceCity,
    4:SetAgeNull,
    5:CheckAgeNull,
    6:FillAgeNull,
    7:DeleteColumn,
    8:NewColumn,
    9:UpdateColumn,
    10:SetNull
}
    if valueInput == 0:
        print("Exiting the program.")
        break
    elif valueInput not in range(0, 11):
        print("Invalid choice. Please enter a number between 0 and 10.")
    else:
        operations[valueInput]()


"""df["Salary"]=5000
print(df["Salary"])
df["AgeCategory"] = np.where(df["Age"] < 30, "Young", "Senior")
print(df["AgeCategory"])
df["City"] = df["City"].replace("Pune", "Pune City")
print(df["City"].value_counts())
df.loc[0,"Age"] = None
print(df["Age"])
print(df["Age"].isnull())
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df["Age"])"""