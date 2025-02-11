def name():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    print(firstname + " " +lastname)
    return(lastname, firstname)

name()
print(name())