# Handling Exceptions
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Invalid entry")
except ZeroDivisionError:
    print("Age cannot be zero")
