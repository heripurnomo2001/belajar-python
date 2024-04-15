import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)        

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return f"Book '{title}' has been borrowed."
        return f"Book '{title}' is either not available or does not exist in the library."

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return f"Book '{title}' has been returned."
        return f"Book '{title}' cannot be returned."

    def available_books(self):
        available_books_list = [book for book in self.books if book.available]
        if available_books_list:
            return [str(book) for book in available_books_list]
        else:
            return []

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.library = Library()

        self.label_title = tk.Label(root, text="Library Management System", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_info = tk.Label(root, text="Enter book title:")
        self.label_info.pack()
        self.entry_title = tk.Entry(root, width=30)
        self.entry_title.pack()

        self.button_add = tk.Button(root, text="Entry Book", command=self.add_book)
        self.button_add.pack(pady=5)

        self.button_borrow = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.button_borrow.pack(pady=5)

        self.button_return = tk.Button(root, text="Return Book", command=self.return_book)
        self.button_return.pack(pady=5)

        self.button_show_books = tk.Button(root, text="Show Available Books", command=self.show_books)
        self.button_show_books.pack(pady=5)

        self.label_result = tk.Label(root, text="")
        self.label_result.pack(pady=10)

    # def add_book(self):
    #     title = self.entry_title.get()
    #     result = self.library.add_book(title)
    #     self.label_result.config(text=result)        
    #     # self.library.add_book(title)
    #     messagebox.showinfo("Notification", f"Book '{title}' has been added to the library.")
    
    def add_book(self):
        title = self.entry_title.get()
        new_book = Book(title, "", "")  # Membuat objek Book baru dengan judul yang dimasukkan pengguna
        self.library.add_book(new_book)  # Menambahkan buku baru ke perpustakaan
        messagebox.showinfo("Notification", f"Book '{title}' has been added to the library.")

    
    def borrow_book(self):
        title = self.entry_title.get()
        result = self.library.borrow_book(title)
        self.label_result.config(text=result)

    def return_book(self):
        title = self.entry_title.get()
        result = self.library.return_book(title)
        self.label_result.config(text=result)
    
    def show_books(self):
        available_books = self.library.available_books()
        if available_books:
            book_list = "\n".join(available_books)
            messagebox.showinfo("Available Books", book_list)
        else:
            messagebox.showinfo("Available Books", "No books available in the library.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x750")  # Mengatur lebar dan tinggi jendela
    root.configure(bg="green")
    app = LibraryApp(root)
    root.mainloop()
