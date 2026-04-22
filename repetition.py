try:
    word = input("Enter the word to search: ")

    with open("data.txt", "r") as file:
        data = file.read()

        count = data.lower().split().count(word.lower())

        print("The word appears", count, "times.")

except FileNotFoundError:
    print("data.txt file not found.")