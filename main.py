from abc import ABC, abstractmethod

# ======================
# USER
# ======================

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role(self):
        pass


class Admin(User):
    def role(self):
        return "admin"


class Student(User):
    def role(self):
        return "student"


# ======================
# BOOK
# ======================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Bor" if self.available else "Band"
        return f"{self.title} - {self.author} ({status})"


# ======================
# LIBRARY
# ======================

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Kitob qo‘shildi")

    def show_books(self):
        if not self.books:
            print("Kutubxona bo‘sh")
            return
        for i, b in enumerate(self.books, 1):
            print(i, b)

    def borrow_book(self, index):
        try:
            book = self.books[index]
            if book.available:
                book.available = False
                print("Oldingiz")
            else:
                print("Band")
        except:
            print("Xato index")

    def return_book(self, index):
        try:
            self.books[index].available = True
            print("Qaytarildi")
        except:
            print("Xato index")

    def save(self):
        with open("books.txt", "w") as f:
            for b in self.books:
                f.write(f"{b.title}|{b.author}|{b.available}\n")

    def load(self):
        try:
            with open("books.txt") as f:
                for line in f:
                    title, author, avail = line.strip().split("|")
                    book = Book(title, author)
                    book.available = avail == "True"
                    self.books.append(book)
        except:
            pass


# ======================
# MAIN
# ======================

def main():
    lib = Library()
    lib.load()

    user = Admin("Ali")
    print(f"Login: {user.name} ({user.role()})")

    while True:
        print("\n1.Add 2.Show 3.Borrow 4.Return 0.Exit")
        c = input(">>> ")

        if c == "1":
            t = input("Title: ")
            a = input("Author: ")
            lib.add_book(t, a)

        elif c == "2":
            lib.show_books()

        elif c == "3":
            i = int(input("Index: ")) - 1
            lib.borrow_book(i)

        elif c == "4":
            i = int(input("Index: ")) - 1
            lib.return_book(i)

        elif c == "0":
            lib.save()
            break


if __name__ == "__main__":
    main()
