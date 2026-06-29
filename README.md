# Library Management System (OOP Project)

A simple Python project that demonstrates Object-Oriented Programming concepts through a Library Management System.

---

## How to Run

```
python main.py
```

---

## OOP Concepts Used

| Concept | Where | Example |
|---|---|---|
| **Classes & Objects** | `book.py`, `member.py`, `library.py` | `Book("Harry Potter", "J.K. Rowling", 3)` |
| **Functions/Methods** | All files | `borrow_book()`, `return_book()`, `search_books()` |
| **Encapsulation** | `book.py` | Private attributes (`__title`, `__author`, `__copies`) with getters and setters |
| **Inheritance** | `member.py` | `Student` and `Teacher` inherit from `Member` |
| **Polymorphism** | `member.py` | `show_info()` behaves differently for Student vs Teacher |

---

## Project Files

| File | Purpose |
|---|---|
| `book.py` | Book class with encapsulation |
| `member.py` | Member (base), Student, Teacher classes with inheritance & polymorphism |
| `library.py` | Library class that manages books and members (contains the intentional bug) |
| `main.py` | Runs the program and shows the bug |
| `DEBUGGING_REPORT.md` | Full debugging report with steps and fix |

---

## Intentional Bug

The `search_books()` method in `library.py` uses `not in` instead of `in`, which returns **wrong books** when searching. See [DEBUGGING_REPORT.md](DEBUGGING_REPORT.md) for the full analysis and fix.
