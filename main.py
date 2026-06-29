from book import Book
from member import Student, Teacher
from library import Library


def main():
    print("=" * 50)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)

    # --- Step 1: Create Library ---
    lib = Library("City Central Library")
    print()

    # --- Step 2: Add Books (Classes & Objects) ---
    print("--- Adding Books ---")
    b1 = Book("Harry Potter", "J.K. Rowling", 3)
    b2 = Book("The Hobbit", "J.R.R. Tolkien", 2)
    b3 = Book("Python Crash Course", "Eric Matthes", 5)
    b4 = Book("Clean Code", "Robert Martin", 1)
    b5 = Book("Harry Potter and the Chamber", "J.K. Rowling", 4)

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(b4)
    lib.add_book(b5)

    # --- Step 3: Register Members (Inheritance) ---
    print("\n--- Registering Members ---")
    s1 = Student("Tirth", "S001", "12th")
    t1 = Teacher("Mr. Shah", "T001", "Computer Science")
    lib.add_member(s1)
    lib.add_member(t1)

    # --- Step 4: Borrow Books (Functions & Encapsulation) ---
    print("\n--- Borrowing Books ---")
    s1.borrow_book(b1)    # Tirth borrows Harry Potter
    s1.borrow_book(b3)    # Tirth borrows Python Crash Course
    t1.borrow_book(b2)    # Mr. Shah borrows The Hobbit
    t1.borrow_book(b4)    # Mr. Shah borrows Clean Code

    # --- Step 5: Return a Book ---
    print("\n--- Returning a Book ---")
    s1.return_book(b1)    # Tirth returns Harry Potter

    # --- Step 6: Show All Info (Polymorphism in action) ---
    lib.show_all_books()
    lib.show_all_members()

    # --- Step 7: Search for Books (BUG SHOWS HERE) ---
    print("=" * 50)
    print("  SEARCHING FOR BOOKS WITH KEYWORD: 'Harry'")
    print("=" * 50)

    results = lib.search_books("Harry")

    print(f"\n  Found {len(results)} result(s):")
    for book in results:
        book.display()

    # --- Verification ---
    print("\n--- VERIFICATION ---")
    print("  EXPECTED: Should find 2 books with 'Harry' in the title.")
    if len(results) != 2:
        print("  ACTUAL:   BUG DETECTED! Wrong books were returned.")
        print("            The search returned books WITHOUT 'Harry' instead.")
    else:
        print("  ACTUAL:   Search works correctly! Bug has been fixed.")

    print("=" * 50)


if __name__ == "__main__":
    main()
