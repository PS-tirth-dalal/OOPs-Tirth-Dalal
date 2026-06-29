class Library:
    """
    Manages all books and members.
    Demonstrates: Functions, Classes/Objects, Encapsulation
    Contains the INTENTIONAL BUG in search_books().
    """
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"  Added '{book.get_title()}' to {self.name}.")

    def add_member(self, member):
        """Register a member."""
        self.members.append(member)
        print(f"  Registered {member.name} (ID: {member.member_id}).")

    def show_all_books(self):
        """Display all books in the library."""
        print(f"\n  All books in {self.name}:")
        for book in self.books:
            book.display()

    def show_all_members(self):
        """Display all members — demonstrates Polymorphism."""
        print(f"\n  All members of {self.name}:")
        for member in self.members:
            member.show_info()   # Each type (Student/Teacher) shows differently
            print()

    def search_books(self, keyword):
        """
        Search for books whose title contains the keyword.

        *** INTENTIONAL BUG ***
        Uses 'not in' instead of 'in', so it returns
        books that do NOT match the keyword!
        """
        keyword_lower = keyword.lower()

        # BUG: 'not in' should be 'in'
        results = [book for book in self.books if keyword_lower not in book.get_title().lower()]

        return results
