try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
