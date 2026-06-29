from book import Book


class Member:
    """
    Base class for a library member.
    Demonstrates: Classes/Objects, Inheritance (parent class), Polymorphism (overridden methods)
    """
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book if copies are available."""
        if book.get_copies() <= 0:
            print(f"  Sorry, '{book.get_title()}' is not available.")
            return
        book.set_copies(book.get_copies() - 1)
        self.borrowed_books.append(book.get_title())
        print(f"  {self.name} borrowed '{book.get_title()}'.")

    def return_book(self, book):
        """Return a borrowed book."""
        if book.get_title() not in self.borrowed_books:
            print(f"  {self.name} hasn't borrowed '{book.get_title()}'.")
            return
        book.set_copies(book.get_copies() + 1)
        self.borrowed_books.remove(book.get_title())
        print(f"  {self.name} returned '{book.get_title()}'.")

    def show_info(self):
        """Polymorphism: this method is overridden by child classes."""
        print(f"  Member: {self.name} (ID: {self.member_id})")
        print(f"  Borrowed: {self.borrowed_books if self.borrowed_books else 'None'}")


class Student(Member):
    """
    Student member — can borrow up to 3 books.
    Demonstrates: Inheritance, Polymorphism (overrides show_info)
    """
    def __init__(self, name, member_id, grade):
        super().__init__(name, member_id)   # call parent constructor
        self.grade = grade
        self.max_books = 3

    def borrow_book(self, book):
        """Override: students have a borrowing limit."""
        if len(self.borrowed_books) >= self.max_books:
            print(f"  {self.name} has reached the limit of {self.max_books} books.")
            return
        super().borrow_book(book)

    def show_info(self):
        """Polymorphism: different output than base Member."""
        print(f"  Student: {self.name} (ID: {self.member_id}) | Grade: {self.grade}")
        print(f"  Borrowed: {self.borrowed_books if self.borrowed_books else 'None'} (Limit: {self.max_books})")


class Teacher(Member):
    """
    Teacher member — can borrow up to 10 books.
    Demonstrates: Inheritance, Polymorphism (overrides show_info)
    """
    def __init__(self, name, member_id, subject):
        super().__init__(name, member_id)
        self.subject = subject
        self.max_books = 10

    def borrow_book(self, book):
        """Override: teachers have a higher borrowing limit."""
        if len(self.borrowed_books) >= self.max_books:
            print(f"  {self.name} has reached the limit of {self.max_books} books.")
            return
        super().borrow_book(book)

    def show_info(self):
        """Polymorphism: different output than base Member and Student."""
        print(f"  Teacher: {self.name} (ID: {self.member_id}) | Subject: {self.subject}")
        print(f"  Borrowed: {self.borrowed_books if self.borrowed_books else 'None'} (Limit: {self.max_books})")
