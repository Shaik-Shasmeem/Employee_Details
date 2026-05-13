import pandas as pd
df = pd.read_csv("data/Employee.csv")

def max_age():
    print("Maximum Age:", df["Age"].max())  
def min_age():
    print("Minimum Age:", df["Age"].min())  
def Experience_in_current_domain():
    print("Maximum Experience in Current Domain:", df["ExperienceInCurrentDomain"].max())
def payment_tier():
    print("Payment Tier Counts:", df["PaymentTier"].value_counts())
def city_counts():
    print("City Counts:", df["City"].value_counts())
def first_rows():
    input_value = int(input("Enter the number of rows you want to see from the top of the DataFrame: "))
    print(f"First {input_value} Rows of the DataFrame:\n", df.head(input_value))
def last_rows():
    input_value = int(input("Enter the number of rows you want to see from the bottom of the DataFrame: "))
    print(f"Last {input_value} Rows of the DataFrame:\n", df.tail(input_value)) 
def gender_counts():
    print("Gender Counts:", df["Gender"].value_counts())
def Joining_years():
    print("Joining Year Counts:", df["JoiningYear"].value_counts())
while True:
    print("\n<--------------Information Retrieval Menu:-------------->")
    input_value = int(input("Enter the number corresponding to the information you want to retrieve:" \
    "\n1. Max Age\n2. Min Age\n3. Experience in Current Domain\n4. Payment Tier Counts\n5. City Counts\n6. First number of Rows\n7. Last number of Rows\n8. Gender Counts\n9. Joining Year Counts\n0. Exit\n"
    "---------------------------------------------------------\n" \
    "Your Choice: "))
    
    if input_value == 1:    
        max_age()
    elif input_value == 2:    
        min_age()
    elif input_value == 3:    
        Experience_in_current_domain()  
    elif input_value == 4:    
        payment_tier()
    elif input_value == 5:
        city_counts()
    elif input_value == 6:
        first_rows()
    elif input_value == 7:
        last_rows()
    elif input_value == 8:
        gender_counts()
    elif input_value == 9:
        Joining_years()
    elif input_value == 0:
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 9.")
    