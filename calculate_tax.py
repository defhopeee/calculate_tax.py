def calculate_tax():
    salary = input("Enter your salary: ")
    salary = float(salary)

    if salary < 0:
        print("Invalid salary")
    else:
        tax = 0.2 * salary
        print("Your tax is:", tax)

        if tax > 1000:
            print("You are in the higher tax bracket")
        else:
            print("You are in the lower tax bracket")