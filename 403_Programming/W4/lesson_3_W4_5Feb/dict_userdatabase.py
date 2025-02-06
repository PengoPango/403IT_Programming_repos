user_database = {}

def add_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")
    
    user_database[name] = {"email": email, "age": age}

while True:
    print("\nUser Management System")
    print("1. Add User ")
    print("2. See database ")
    print("3. Exit ")

    
    choice = input("Enter Action ")
    if choice == "3":
        print("Goodbye")
        break
    elif choice == "2":
        print(user_database)
    elif choice == "1":
        add_user()
      

