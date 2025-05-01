# Working with Paths
from pathlib import Path

path = Path("emails")
path.mkdir()  # Creates a new directory
print(path.exists())  # Check if path exists
path.rmdir()  # Removes the directory
