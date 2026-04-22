class Book:
    def __init__(self, id, name, author, publish_date):
        self.id = id
        self.name = name
        self.author = author
        self.publish_date = publish_date

book = Book(46, "How to Ride", "Rossi", "2023")

print("Book Name:", book.name)

book.name = "How to ride Motorcyles for beginners"

print("Modified Name:", book.name)

print("author" in book.__dict__)

del book.publish_date
