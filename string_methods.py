# String Manipulation
name = "Alexio"
name_2 = "Jose"
full_name = f"{name} {name_2}"  # Concatenation using f-string
print(full_name)

# String methods
message = "Python is Awesome"
print(message.upper())  # Converts to uppercase
print(message.lower())  # Converts to lowercase
print(message.find("is"))  # Finds index of substring
print(message.replace("Awesome", "great"))  # Replace words
print("Python" in message)  # Checking existence (Boolean)
