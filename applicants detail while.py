''' This programe takes new applicant/employees name (by creating a list that accepts first, middle and last name) and create a short form of their name and email addres for their onboarding'''


while True:    
    first_name = input("Enter First Name:")
    middle_name = input("Enter Middle Name:") #where there is no middle name, leave blank and press enter
    last_name = input("Enter Last Name:")
    full_name = [first_name,middle_name,last_name]
    short_name = full_name[0][0] + "." + full_name[1][0] + " " + full_name[2]
    creat_email = full_name[0] + "." + full_name[2]
    print("New Employee's details:")
    print(f"Employee's Name:  {short_name}")
    print(f"Office Email: {creat_email.lower()}"+ "@aria.com")
    print("______________________________________")
    
    
