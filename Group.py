import json


# ============================================================
# BOOK CLASS
# ============================================================

class Book:
    # The constructor creates a Book object and stores
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

        # Every new book is available when it is first created.
        self.is_borrowed = False

        # No user has borrowed the book yet.
        self.borrowed_by = None

    # This method displays the information of the book.

    def show_info(self):
        # Check whether the book is currently borrowed.
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        # Print the book information in an organized format.
        print("\n-----------------------------------------")
        print("============= BOOK INFO ================")
        print("-----------------------------------------")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Status: {status}")

        # Only display the borrower when the book is borrowed.
        if self.borrowed_by:
            print(f"Borrowed by: {self.borrowed_by}")

        print("-----------------------------------------")

    # This method allows a user to borrow the book.
    def borrow(self, user):
        # A book cannot be borrowed if another user already has it.
        if self.is_borrowed:
            print("This book is already borrowed.")
            return False

        # Change the book status to borrowed.
        self.is_borrowed = True

        # Store the name of the user who borrowed the book.
        self.borrowed_by = user.name

        # True means the borrowing was successful.
        return True

    # This method returns a borrowed book to the library.
    def return_book(self):
        # Make sure the book is actually borrowed first.
        if not self.is_borrowed:
            print("This book is not currently borrowed.")
            return False

        # Change the status back to available.
        self.is_borrowed = False

        # Remove the borrower information.
        self.borrowed_by = None

        # True means the return was successful.
        return True

    # Convert the Book object into a dictionary.
    # Dictionaries can be stored in a JSON file.
    def to_dict(self):
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }


# ============================================================
# NOVEL CLASS
# ============================================================

# Novel inherits the attributes and methods from Book.
class Novel(Book):

    # A Novel has all normal Book information,
    # plus a genre.
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    # Display all information specific to a Novel.
    def show_info(self):
        # Check the current availability of the novel.
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        # Display the novel information in one section.
        print("\n-----------------------------------------")
        print("============= NOVEL INFO ===============")
        print("-----------------------------------------")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Status: {status}")

        # Show the borrower's name if someone borrowed it.
        if self.borrowed_by:
            print(f"Borrowed by: {self.borrowed_by}")

        # Genre is information that only belongs to Novel.
        print(f"Genre: {self.genre}")
        print("-----------------------------------------")

    # Convert the Novel object into a dictionary
    # so that it can also be saved in JSON format.
    def to_dict(self):
        # First get all the normal Book information.
        data = super().to_dict()

        # Change the type so Library.load() knows
        # that this object is a Novel.
        data["type"] = "Novel"

        # Add the information that is specific to Novel.
        data["genre"] = self.genre

        return data


# ============================================================
# MAGAZINE CLASS
# ============================================================

# Magazine also inherits from the Book class.
class Magazine(Book):

    # A Magazine has all normal Book information,
    # plus an issue.
    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue

    # Display all information specific to a Magazine.
    def show_info(self):
        # Check whether the magazine is available or borrowed.
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        # Display all magazine information together.
        print("\n-----------------------------------------")
        print("============ MAGAZINE INFO =============")
        print("-----------------------------------------")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Status: {status}")

        # Display the borrower when the magazine is borrowed.
        if self.borrowed_by:
            print(f"Borrowed by: {self.borrowed_by}")

        # Issue is information specific to Magazine.
        print(f"Issue: {self.issue}")
        print("-----------------------------------------")

    # Convert the Magazine object into a dictionary
    # for saving it in the JSON file.
    def to_dict(self):
        # Start with the information inherited from Book.
        data = super().to_dict()

        # Identify this object as a Magazine.
        data["type"] = "Magazine"

        # Add the Magazine-specific information.
        data["issue"] = self.issue

        return data


# ============================================================
# USER CLASS
# ============================================================

class User:
    # Create a new user with a name and password.
    def __init__(self, name, password):
        self.name = name
        self.password = password

        # This list stores the titles of books
        # currently borrowed by the user.
        self.borrowed_books = []

    # Allow the user to borrow a book.
    def borrow_book(self, book):
        # Ask the Book object to perform the borrowing operation.
        if book.borrow(self):

            # If borrowing is successful, save the book title
            # in the user's borrowed_books list.
            self.borrowed_books.append(book.title)

            print(f"You borrowed: {book.title}")

            # Return True to indicate success.
            return True

        # Return False when the book could not be borrowed.
        return False

    # Allow the user to return a book.
    def return_book(self, book):
        # First check whether this user has this book
        # in their borrowed_books list.
        if book.title not in self.borrowed_books:
            print("You did not borrow this book.")
            return False

        # Ask the Book object to return the book.
        if book.return_book():

            # Remove the title from the user's borrowed list.
            self.borrowed_books.remove(book.title)

            print(f"You returned: {book.title}")

            # Return True to indicate that the return succeeded.
            return True

        return False

    # Display all books currently borrowed by this user.
    def list_borrowed_books(self):
        # If the list is empty, there is nothing to display.
        if not self.borrowed_books:
            print("You have no borrowed books.")
            return

        print("\n-----------------------------------------")
        print("========== YOUR BORROWED BOOKS =========")
        print("-----------------------------------------")

        # enumerate() gives each book a number starting from 1.
        for number, book in enumerate(self.borrowed_books, 1):
            print(f"{number}. {book}")

        print("-----------------------------------------")

    # Convert the User object into a dictionary
    # so the user information can be saved as JSON.
    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.borrowed_books
        }


# ============================================================
# LIBRARY CLASS
# ============================================================

class Library:
    # Create a new Library with a name,
    # An empty list for books and users.
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    # Add a Book, Novel, or Magazine object to the library.
    def add_book(self, book):
        self.books.append(book)

    # Add a User object to the library.
    def add_user(self, user):
        self.users.append(user)

    # Display every book currently stored in the library.
    def show_all_books(self):
        # Check if the library contains any books.
        if not self.books:
            print("\nNo books are currently available in the library.")
            return

        print(f"\n========== {self.name.upper()} - ALL BOOKS ==========")

        # Each book uses its own show_info() method.
        # This works for Book, Novel, and Magazine because
        # they all have their own show_info() method.
        for book in self.books:
            book.show_info()
        print("=====================================================")

    # Check the user's login information.
    def login(self, name, password):
        # Go through all registered users.
        for user in self.users:

            # Compare the entered information with
            # the stored name and password.
            if user.name == name and user.password == password:
                return user

        # None means that no matching user was found.
        return None

    # Save the entire library into a JSON file.
    def save(self, file_name):

        # Convert every book object into a dictionary.
        # The to_dict() method also keeps the correct book type.
        books_data = [b.to_dict() for b in self.books]

        # Convert every user object into a dictionary.
        users_data = [u.to_dict() for u in self.users]

        # Put both groups of information into one dictionary.
        library_data = {
            "books": books_data,
            "users": users_data
        }

        # Open the file in write mode and save the data as JSON.
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(library_data, f, indent=4)

    # Load the library information from a JSON file.
    def load(self, file_name):
        try:
            # Open the JSON file and convert it into Python data.
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Users are loaded first because books may contain
            # information about which user borrowed them.
            for u_item in data.get("users", []):

                user = User(
                    u_item["name"],
                    u_item["password"]
                )

                # Restore the user's list of borrowed book titles.
                user.borrowed_books = u_item.get("borrowed_books", [])

                self.add_user(user)

            # Load all saved books.
            for b_item in data.get("books", []):

                # Read the saved type so we know which class
                # should be created.
                book_type = b_item.get("type", "Book")

                # Recreate the correct class from the JSON data.
                if book_type == "Novel":
                    new_book = Novel(
                        b_item["title"],
                        b_item["author"],
                        b_item["publication_year"],
                        b_item["genre"]
                    )

                elif book_type == "Magazine":
                    new_book = Magazine(
                        b_item["title"],
                        b_item["author"],
                        b_item["publication_year"],
                        b_item["issue"]
                    )

                else:
                    # If the type is Book, create a normal Book.
                    new_book = Book(
                        b_item["title"],
                        b_item["author"],
                        b_item["publication_year"]
                    )

                # Restore the borrowing status saved in JSON.
                new_book.is_borrowed = b_item.get("is_borrowed", False)

                # Book.borrow() stores the user's name,
                # so borrowed_by is restored as the user's name too.
                new_book.borrowed_by = b_item.get("borrowed_by")

                # Add the recreated book to the library.
                self.add_book(new_book)

        # If the file does not exist, simply start with
        # an empty library instead of causing an error.
        except FileNotFoundError:
            print(f"File '{file_name}' was not found.")


# ============================================================
# LIBRARY SETUP
# ============================================================

library = Library("My Library")

library.load("library.json")


# Add test books if the library is empty.
if not library.books:

    library.add_book(
        Book("The Hobbit", "J.R.R. Tolkien", 1937)
    )

    library.add_book(
        Novel(
            "Harry Potter",
            "J.K. Rowling",
            1997,
            "Fantasy"
        )
    )

    library.add_book(
        Novel(
            "1984",
            "George Orwell",
            1949,
            "Dystopian"
        )
    )

    library.add_book(
        Magazine(
            "National Geographic",
            "Various",
            2025,
            "January"
        )
    )


# Add test users if there are no users.
if not library.users:

    library.add_user(
        User("john", "1234")
    )

    library.add_user(
        User("sara", "5678")
    )

    library.save("library.json")


# ============================================================
# LOGIN / CREATE ACCOUNT
# ============================================================

print("1 - Login")
print("2 - Create Account")

choice = input("Enter your choice: ")


# ============================================================
# LOGIN
# ============================================================

if choice == "1":

    user_name = input("Enter your user_name: ")
    password = input("Enter your password: ")

    logged_in_user = library.login(
        user_name,
        password
    )

    if logged_in_user is not None:

        print("Login successful")

        # Main menu
        while True:

            print("\n-----------------------------------------")
            print("============= MAIN MENU ================")
            print("-----------------------------------------")
            print("1 - List all books")
            print("2 - Borrow a book")
            print("3 - Return a book")
            print("4 - Show my borrowed books")
            print("5 - Search for a book")
            print("6 - Save and exit")
            print("-----------------------------------------")

            menu_choice = input(
                "Enter your choice: "
            )


            # ------------------------------------------------
            # OPTION 1: LIST ALL BOOKS
            # ------------------------------------------------

            if menu_choice == "1":

                library.show_all_books()

                # Press Enter to return to the main menu.
                input(
                    "\nPress Enter to return to the main menu..."
                )


            # ------------------------------------------------
            # OPTION 2: BORROW A BOOK
            # ------------------------------------------------

            elif menu_choice == "2":

                print("\nEnter 0 if you want to go back.")

                book_title = input(
                    "Enter a book title: "
                )

                # 0 allows the user to cancel.
                if book_title == "0":
                    continue

                found = False

                for book in library.books:

                    if book_title.lower() == book.title.lower():

                        logged_in_user.borrow_book(book)

                        found = True
                        break

                if not found:
                    print("Book was not found.")

                input(
                    "\nPress Enter to return to the main menu..."
                )


            # ------------------------------------------------
            # OPTION 3: RETURN A BOOK
            # ------------------------------------------------

            elif menu_choice == "3":

                print("\nEnter 0 if you want to go back.")

                book_title = input(
                    "Enter a book title: "
                )

                # 0 allows the user to cancel.
                if book_title == "0":
                    continue

                found = False

                for book in library.books:

                    if book_title.lower() == book.title.lower():

                        logged_in_user.return_book(book)

                        found = True
                        break

                if not found:
                    print("Book was not found.")

                input(
                    "\nPress Enter to return to the main menu..."
                )


            # ------------------------------------------------
            # OPTION 4: SHOW BORROWED BOOKS
            # ------------------------------------------------

            elif menu_choice == "4":

                logged_in_user.list_borrowed_books()

                input(
                    "\nPress Enter to return to the main menu..."
                )


            # ------------------------------------------------
            # OPTION 5: SEARCH FOR A BOOK
            # ------------------------------------------------

            elif menu_choice == "5":

                print("\nEnter 0 if you want to go back.")

                book_title = input(
                    "Enter a book title to search: "
                )

                # 0 allows the user to cancel.
                if book_title == "0":
                    continue

                found = False

                for book in library.books:

                    if book_title.lower() in book.title.lower():

                        book.show_info()

                        found = True

                if not found:
                    print("Book was not found.")

                input(
                    "\nPress Enter to return to the main menu..."
                )


            # ------------------------------------------------
            # OPTION 6: SAVE AND EXIT
            # ------------------------------------------------

            elif menu_choice == "6":

                library.save("library.json")

                print("Goodbye!")

                break


            # ------------------------------------------------
            # INVALID OPTION
            # ------------------------------------------------

            else:

                print("Invalid menu choice.")


    else:

        print("Invalid user_name or password.")


# ============================================================
# CREATE ACCOUNT
# ============================================================

elif choice == "2":

    user_name = input("Enter your user_name: ")
    password = input("Enter your password: ")

    new_user = User(
        user_name,
        password
    )

    library.add_user(new_user)

    library.save("library.json")

    print("Account created successfully.")


# ============================================================
# INVALID LOGIN MENU CHOICE
# ============================================================

else:

    print("Invalid choice.")