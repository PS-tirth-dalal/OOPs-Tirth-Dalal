class Book:
    """
    Represents a book in the library.
    Demonstrates: Encapsulation (private attributes with getters/setters)
    """
    def __init__(self, title, author, copies):
        self.__title = title       # private
        self.__author = author     # private
        self.__copies = copies     # private

    # --- Getters (Encapsulation) ---
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_copies(self):
        return self.__copies

    # --- Setter with validation (Encapsulation) ---
    def set_copies(self, count):
        if count < 0:
            print("Error: Copies cannot be negative.")
            return
        self.__copies = count

    def display(self):
        """Show book info."""
        print(f"  '{self.__title}' by {self.__author} — {self.__copies} copies available")
