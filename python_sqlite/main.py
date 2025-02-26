from db.models import Book, User, Rent, sqlite3
import sys

def main():
    '''main            
    '''
    db_path = "./library.db"
    conn = sqlite3.connect(db_path)
    book_table = Book(conn)
    user_table = User(conn)
    rents_table = Rent(conn)

    print("Welcome to the Library System. Type 'help' for available commands.")

    while True:
        user_input = input("Enter command: ")
        args = user_input.split()

        if not args:
            continue

        match args[0]:
            case "create_book" | "cb":
                if len(args) < 7:
                    print("Usage: create_book book_id title, author, year, edition, shelf_number, row_number")
                    continue
                book_id = int(args[1])
                title = args[2]
                author = args[3]
                year = int(args[4])
                edition = args[5]
                shelf_number = int(args[6])
                row_number = int(args[7])
                book_table.objects.create(book_id, title, author, year, edition, shelf_number, row_number)
                print(f"Book '{title}' created.")
            
            case "delete_book" | "remove_book":
                if len(args) < 2:
                    print("Usage: delete_book book_id")
                    continue
                book_id = int(args[1])
                book_table.objects.delete(book_id)
                print(f"Book with ID {book_id} has been deleted.")
            
            case "all_books" | "ab":
                books = book_table.objects.all()
                print(f"Found {len(books)} book(s)")
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Edition: {book[4]}, Shelf_number: {book[5]}, Row_number: {book[6]}")

            case "find_book" | "fb":
                if len(args) < 3:
                    print("Usage: find_book title, author")
                    continue
                title = args[1]
                author = args[2]
                books = book_table.objects.search_book(title, author)
                print(f"Found {len(books)} book(s)")
                for book in books:
                    print(f"ID: {book[0]}, Row_number: {book[1]}, Shelf_number: {book[2]}")
            
            case "search_info" | "book_info":
                if len(args) < 2:
                    print("Usage: search_info book_id")
                    continue
                book_id = int(args[1])
                info = book_table.objects.search_info(book_id)
                print(f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Edition: '{book[3]}'")
            
            case "search_person_info" | "spi":
                if len(args) < 2:
                    print("Usage: search_person_info book_id")
                    continue
                book_id = args[1]
                person_info = book_table.objects.search_person_info(book_id)
                print(f"ID: {person_info[0]} First name: {person_info[1]} Last name: {person_info[2]}")
            
            case "register_user" | "ru":
                if len(args) < 6:
                    print("Usage: register_user first_name, last_name, patronymic, user_id, address")
                    continue
                user_id = int(args[1])
                first_name = args[2]
                last_name = args[3]
                patronymic = args[4]
                address = args[5]
                user_table.objects.create(first_name, last_name, patronymic, user_id, address)
                print(f"User '{first_name} {last_name} {patronymic}' registered.")

            case "all_users" | "au":
                users = user_table.objects.all()
                print(f"Found {len(users)} user(s)")
                for user in users:
                    print(f"First_name: {user[0]}, Last_name: {user[1]}, Patronymic: {user[2]}, ID: {user[3]}, Address: {user[4]}")

            case "delete_user" | "du":
                if len(args) < 2:
                    print("Usage: delete_user user_id")
                    continue
                user_id = int(args[1])
                user_table.objects.delete(user_id)
                print(f"User with ID {user_id} has been deleted.")

            case "search_user":
                if len(args) < 3:
                    print("Usage: search_user first_name last_name")
                    continue
                first_name = args[1]
                last_name = args[2]
                users = user_table.objects.search_user(first_name, last_name)
                for user in users:
                    print(f"ID: {user}")

            case "search_info":
                if len(args) < 2:
                    print("Usage: search_info user_id")
                    continue
                user_id = int(args[1])
                info = user_table.objects.search_info(user_id)
                print(f"FIrst_name: {info[0]}, Last_name: {info[1]}, Patronymic: {info[2]}")

            case "search_books":
                if len(args) < 2:
                    print("Usage: search_books user_id")
                    continue
                user_id = int(args[1])
                books = user_table.objects.search_books(user_id)
                print(f"ID: {books[0]}, Title: {books[1]}, Author: {books[2]}")
                
            case "all_rents":
                rents = rents_table.objects.all()
                for rent in rents:
                    print(f"User_ID: {rent[0]}, Book_ID: {rent[1]}")
            
            case "rent_book" | "rb":
                if len(args) < 3:
                    print("Usage: rent_book user_id book_id")
                    continue
                user_id = int(args[1])
                book_id = int(args[2])
                rents_table.objects.rent_book(user_id, book_id)
                print(f"Book with ID {book_id} rented to user with ID {user_id}.")

            case "return_book" | "rt":
                if len(args) < 3:
                    print("Usage: return_book user_id book_id")
                    continue
                user_id = int(args[1])
                book_id = int(args[2])
                rents_table.objects.delete(user_id, book_id)

            case "currently_reading" | "cr":
                if len(args) < 2:
                    print("Usage: currently_reading user_id")
                    continue
                user_id = int(args[1])
                book_reading = rents_table.objects.currently_reading(user_id)
                print(f"ID: {book_reading}")

            case "exit":
                print("Exiting the program.")
                sys.exit()


if __name__ == "__main__":
    main()
