
try:
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    with open(source, "r") as f1:
        data = f1.read()

    with open(destination, "w") as f2:
        f2.write(data)

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")

except PermissionError:
    print("Permission denied while accessing file.")
