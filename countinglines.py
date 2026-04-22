try:
    with open("story.txt", "r") as file:
        data = file.read()

        lines = data.split("\n")
        words = data.split()

        print("Number of lines:", len(lines))
        print("Number of words:", len(words))

except FileNotFoundError:
    print("story.txt file not found.")
