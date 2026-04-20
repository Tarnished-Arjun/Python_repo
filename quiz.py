quiz = {
    "Which company makes Ninja 300?": {
        "options": ["A. Yamaha", "B. Kawasaki", "C. Honda", "D. Suzuki"],
        "answer": "B"
    },
    "Hayabusa belongs to which brand?": {
        "options": ["A. KTM", "B. Suzuki", "C. BMW", "D. Ducati"],
        "answer": "B"
    },
    "How many wheels does a bike have?": {
        "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer": "B"
    }
}

score = 0

for question, data in quiz.items():
    print("\n" + question)

    for option in data["options"]:
        print(option)

    user = input("Enter option / skip / quit: ").upper()

    if user == "QUIT":
        break
    elif user == "SKIP":
        continue
    elif user == data["answer"]:
        score += 1
        print("Correct")
    else:
        score -= 1
        print("Wrong")

print("Final Score:", score)