class Book:
    def __init__(self, title: str, author: str):
        """Intilalizing the argguments title and author

        Args:
            title (str): _description_
            author (str): _description_
        """
        self._title = title
        self._author = author

    def __str__(self):
        """its a dunderate method who retuens string

        Returns:
            _type_: str
        """
        return f"Title :{self._title},Author : {self._author}"

    def get_title(self) -> str:
        """returns the title parameter"""
        return self._title

    def set_title(self, title) -> None:
        """set the title of the Book"""
        self._title = title

    def get_author(self) -> str:
        """returns the author parameter"""
        return self._author

    def set_author(self, author) -> None:
        """_sets the author of the book"""
        self._author = author


class Library:
    def __init__(self):
        """defining Dictionary to store books with key:value (title:author)"""
        self._books = {}

    def add_book(self, other: Book) -> None:
        """it gets the title and author from Book class and add it to the books Dictionary

        Args:
            other (Book):  The Book instance to be added.

        Raises:
            TypeError: Invalid book! Only objects of type 'Book' can be added.
        """
        title = other.get_title()
        author = other.get_author()
        self._books[title] = author

        if not isinstance(other, Book):
            raise TypeError("Invalid book! Only objects of type 'Book' can be added.")

    def list_books(self) -> None:
        """Lists all books in the library along with their authors."""

        if not self._books:
            print("Books does not excist in the liabrary")
        else:
            for title, author in self._books.items():
                print(f"{title} by {author}")


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.list_books()
