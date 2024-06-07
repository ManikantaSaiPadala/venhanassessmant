class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, {self.pages} pages"

title = input()
author = input()
pages = int(input())
book = Book(title, author, pages)
print(book)