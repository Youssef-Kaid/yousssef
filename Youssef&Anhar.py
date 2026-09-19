# Order of Python program/ codes is organized like this: 
# 1. movies = [...]
# 2. snacks = [...]

# 3. add_movie()
# 4. display_movies()
# 5. display_movie()
# 6. start_order()
# 7. book_tickets(order)
# 8. add_snack_to_order(order)
# 9. display_order(order)
# 10. order = None
# 11. MAIN MENU
#
# ----------------


# Staff should be able to add a new movie.
# Customers can order from the snack bar.
#
# For each movie we record:
# - Title
# - Genres
# - Age category
# - Showtimes
# - Ticket price
# - Number of auditorium seats

# For each snack we record:
# - Name
# - Price

movies = [
    {
        "Title": "The lord of the rings",
        "Genres": ["Epic fantasy", "Adventure"],
        "Age Categories": "+16",
        "Showtimes": [
            {"Showtime": "3:00 pm", "Ticket price": 13, "Auditorium seats": 100}, 
            {"Showtime": "5:00 pm", "Ticket price": 13, "Auditorium seats": 100},
            {"Showtime": "7:30 pm", "Ticket price": 13, "Auditorium seats": 150},
            {"Showtime": "9:00 pm", "Ticket price": 13, "Auditorium seats": 180}
        ]
    },

    {
        "Title": "Apex",
        "Genres": ["Thriller", "Action"],
        "Age Categories": "+18",
        "Showtimes": [
            {"Showtime": "4:30 pm", "Ticket price": 11, "Auditorium seats": 100},
            {"Showtime": "6:00 pm", "Ticket price": 11, "Auditorium seats": 120},
            {"Showtime": "8:00 pm", "Ticket price": 11, "Auditorium seats": 140},
            {"Showtime": "9:30 pm", "Ticket price": 11, "Auditorium seats": 160},
            {"Showtime": "11:00 pm", "Ticket price": 13, "Auditorium seats": 180}
        ]
    },

    {
        "Title": "Mad max",
        "Genres": ["Science Fiction", "Thriller"],
        "Age Categories": "+18",
        "Showtimes": [
            {"Showtime": "6:30 pm", "Ticket price": 15, "Auditorium seats": 100},
            {"Showtime": "8:30 pm", "Ticket price": 15, "Auditorium seats": 120},
            {"Showtime": "10:30 pm", "Ticket price": 15, "Auditorium seats": 140},
            {"Showtime": "12:30 pm", "Ticket price": 17, "Auditorium seats": 180}
        ]
    },

    {
        "Title": "The nun",
        "Genres": ["Horror", "Mystery"],
        "Age Categories": "+18",
        "Showtimes": [
            {"Showtime": "8:30 pm", "Ticket price": 17, "Auditorium seats": 100},
            {"Showtime": "9:45 pm", "Ticket price": 17, "Auditorium seats": 120},
            {"Showtime": "10:45 pm", "Ticket price": 17, "Auditorium seats": 140},
            {"Showtime": "12:00 pm", "Ticket price": 19, "Auditorium seats": 180}
        ]
    },

    {
        "Title": "The bad guys",
        "Genres": ["Comedy", "Adventure"],
        "Age Categories": "+6",
        "Showtimes": [
            {"Showtime": "5:45 pm", "Ticket price": 14.5, "Auditorium seats": 100},
            {"Showtime": "7:30 pm", "Ticket price": 14.5, "Auditorium seats": 120},
            {"Showtime": "9:30 pm", "Ticket price": 14.5, "Auditorium seats": 140},
            {"Showtime": "10:45 pm", "Ticket price": 16, "Auditorium seats": 180}
        ]
    },

    {
        "Title": "Inside out",
        "Genres": ["Family-film", "Animation"],
        "Age Categories": "All ages",
        "Showtimes": [
            {"Showtime": "3:30 pm", "Ticket price": 9, "Auditorium seats": 100},
            {"Showtime": "5:30 pm", "Ticket price": 9, "Auditorium seats": 120},
            {"Showtime": "7:30 pm", "Ticket price": 9, "Auditorium seats": 140},
            {"Showtime": "9:30 pm", "Ticket price": 9, "Auditorium seats": 180}
        ]
    },

    {
        "Title": "Shutter island",
        "Genres": ["Mystery", "Drama"],
        "Age Categories": "+18",
        "Showtimes": [
            {"Showtime": "4:00 pm", "Ticket price": 13.5, "Auditorium seats": 100},
            {"Showtime": "5:45 pm", "Ticket price": 13.5, "Auditorium seats": 120},
            {"Showtime": "7:30 pm", "Ticket price": 13.5, "Auditorium seats": 140},
            {"Showtime": "9:45 pm", "Ticket price": 13.5, "Auditorium seats": 180},
            {"Showtime": "11:45 pm", "Ticket price": 15, "Auditorium seats": 180}
        ]
    }
]


snacks = [
    {"Name": "Popcorn", "Price": 5},
    {"Name": "Nachos", "Price": 6},
    {"Name": "Chocolate", "Price": 3},
    {"Name": "Soft drink", "Price": 3},
    {"Name": "Water", "Price": 2}
]

# --------------------------------------------------
# FUNCTION: ADD A NEW MOVIE
# --------------------------------------------------

def add_movie():

    print("\n===== Add a New Movie =====")

    title = input("Enter a movie title: ")
    age_category = input("Enter age category: ")

    # --------------------------------------------------
    # Enter genres
    # --------------------------------------------------

    genres = []

    number_of_genres = int(input("How many genres does this movie have? "))

    while len(genres) < number_of_genres:

        add_genre = input(
            f"Enter genre {len(genres) + 1}: "
        ) 

        # Check if the genre already exists
        genre_already_exists = add_genre in genres

        if genre_already_exists:
            print("This genre has already been added. Please enter another genre.")

        else:
            genres.append(add_genre)

    # --------------------------------------------------
    # Enter showtimes
    # --------------------------------------------------

    showtimes = []

    number_of_showtimes = int(
        input("How many showtimes does this movie have? ")
    )

    for i in range(number_of_showtimes):

        print(f"\nShowtime {i + 1}")

        showtime = input("Enter showtime: ")

        ticket_price = float(
            input("Enter ticket price: ")
        )

        auditorium_seats = int(
            input("Enter the number of auditorium seats: ")
        )

        showtimes.append({
            "Showtime": showtime,
            "Ticket price": ticket_price,
            "Auditorium seats": auditorium_seats
        })

    # --------------------------------------------------
    # Create the movie
    # --------------------------------------------------

    movie = {
        "Title": title,
        "Genres": genres,
        "Age Categories": age_category,
        "Showtimes": showtimes
    }

    # Add the movie to the movies list
    movies.append(movie)

    print("\nMovie added successfully!")


# --------------------------------------------------
# FUNCTION: DISPLAY MOVIES
# --------------------------------------------------

def display_movies():

    print("\n===== Movies Currently Showing =====")

    for i in range(len(movies)):
        print(f"{i + 1}- {movies[i]['Title']}")


# --------------------------------------------------
# FUNCTION: DISPLAY ONE MOVIE
# --------------------------------------------------

def display_movie():

    display_movies()

    choice = input(
        "\nChoose a movie number: "
    )

    # Check if the user entered a number
    if choice.isdigit():

        movie_number = int(choice)

        # Check if the number is valid
        if 1 <= movie_number <= len(movies):

            selected_movie = movies[movie_number - 1]

            print("\n===== Selected Movie =====")

            print("Title:", selected_movie["Title"])

            print(
                "Genres:",
                ", ".join(selected_movie["Genres"])
            )

            print(
                "Age category:",
                selected_movie["Age Categories"]
            )

            print("\n===== Showtimes =====")

            for showtime in selected_movie["Showtimes"]:

                print(
                    "Showtime:",
                    showtime["Showtime"],
                    "| Ticket price:",
                    showtime["Ticket price"],
                    "| Auditorium seats:",
                    showtime["Auditorium seats"]
                )

        else:
            print("Invalid movie number.")

    else:
        print("Please enter a number.")

# --------------------------------------------------
# FUNCTION: START ORDER
# --------------------------------------------------

def start_order():

    print("\n===== Start New Order =====")

    order = {
        "Tickets": [],
        "Snacks": []
    }

    print("New order started successfully!")

    return order

# --------------------------------------------------
# FUNCTION: BOOK TICKETS
# --------------------------------------------------

def book_tickets(order):

    print("\n===== Book Tickets =====")

    display_movies()

    choice = input("\nChoose a movie number: ")

    if choice.isdigit():

        movie_number = int(choice)

        if 1 <= movie_number <= len(movies):

            selected_movie = movies[movie_number - 1]

            print("\n===== Showtimes =====")

            for i in range(len(selected_movie["Showtimes"])):

                showtime = selected_movie["Showtimes"][i]

                print(
                    f"{i + 1} - {showtime['Showtime']} | "
                    f"€{showtime['Ticket price']} | "
                    f"{showtime['Auditorium seats']} seats"
                )

            showtime_choice = input("\nChoose a showtime number: ")

            if showtime_choice.isdigit():

                showtime_number = int(showtime_choice)

                if 1 <= showtime_number <= len(selected_movie["Showtimes"]):

                    selected_showtime = selected_movie["Showtimes"][showtime_number - 1]

                    number_of_tickets = int(
                        input("How many tickets would you like? ")
                    )

                    if number_of_tickets <= selected_showtime["Auditorium seats"]:

                        ticket = {
                            "Movie": selected_movie["Title"],
                            "Showtime": selected_showtime["Showtime"],
                            "Ticket price": selected_showtime["Ticket price"],
                            "Number of tickets": number_of_tickets
                        }

                        order["Tickets"].append(ticket)

                        print("\nTickets added successfully!")

                    else:

                        print("There are not enough seats available.")

                else:

                    print("Invalid showtime number.")

            else:

                print("Please enter a number.")

        else:

            print("Invalid movie number.")

    else:

        print("Please enter a number.")



# --------------------------------------------------
# FUNCTION: ADD SNACK TO ORDER
# --------------------------------------------------

def add_snack_to_order(order):

    print("\n===== Snack Bar =====")

    for i in range(len(snacks)):

        print(
            f"{i + 1} - {snacks[i]['Name']} "
            f"€{snacks[i]['Price']}"
        )

    choice = input("\nChoose a snack number: ")

    if choice.isdigit():

        snack_number = int(choice)

        if 1 <= snack_number <= len(snacks):

            selected_snack = snacks[snack_number - 1]

            quantity = int(
                input("How many would you like? ")
            )

            snack_order = {
                "Name": selected_snack["Name"],
                "Price": selected_snack["Price"],
                "Quantity": quantity
            }

            order["Snacks"].append(snack_order)

            print("\nSnack added successfully!")

        else:

            print("Invalid snack number.")

    else:

        print("Please enter a number.")

# --------------------------------------------------
# FUNCTION: DISPLAY ORDER
# --------------------------------------------------

def display_order(order):

    print("\n===== Your Order =====")

    total = 0

    # --------------------------------------------------
    # Tickets
    # --------------------------------------------------

    print("\nTickets:")

    if len(order["Tickets"]) == 0:

        print("No tickets booked.")

    else:

        for ticket in order["Tickets"]:

            ticket_total = (
                ticket["Ticket price"]
                * ticket["Number of tickets"]
            )

            total = total + ticket_total

            print("Title:", ticket['Movie'],
                  "\nShowtime:", ticket['Showtime'],
                  "\nNumber of tickets:", ticket['Number of tickets'], 
                  "\nticket(s) price:€", ticket_total
                  )

    # --------------------------------------------------
    # Snacks
    # --------------------------------------------------

    print("\nSnacks:")

    if len(order["Snacks"]) == 0:

        print("No snacks added.")

    else:

        for snack in order["Snacks"]:

            snack_total = (
                snack["Price"]
                * snack["Quantity"]
            )

            total = total + snack_total

            print(f"\nSnacks: {snack['Name']} \nQuantity: {snack['Quantity']} \nTotal price: {snack_total}")

    print("\nTotal price: €", total)

order = None

# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

while True:

    print("\n==============================")
    print("       CINEMA SYSTEM")
    print("==============================")

    print("1 - Display movies")
    print("2 - View movie information")
    print("3 - Add a new movie")
    print("4 - Start order")
    print("5 - Book tickets")
    print("6 - Add snack to order")
    print("7 - View order")
    print("8 - Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        display_movies()

    elif choice == "2":

        display_movie()

    elif choice == "3":

        add_movie()

    elif choice == "4":

        order = start_order()

    elif choice == "5":

        if order is None:

            print("\nPlease start an order first.")

        else:

            book_tickets(order)

    elif choice == "6":

        if order is None:

            print("\nPlease start an order first.")

        else:

            add_snack_to_order(order)

    elif choice == "7":

        if order is None:

            print("\nPlease start an order first.")

        else:

            display_order(order)

    elif choice == "8":

        print("Thank you for using the cinema system.")
        break

    else:

        print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6, 7, or 8.")


