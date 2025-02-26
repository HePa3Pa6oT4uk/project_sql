import sqlite3
from db.utils import get_script_from_file

class Book:
    """
    Class implementing book table logic
    """

    class BookObjects:
        """
        Proxy class for books table
        """
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"book/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, int, str, int, int]]:
            '''all'''
            return self._template_query("all.sql")

        def create(self, book_id: int, title: str, author: str, year: int, edition: str, shelf_number: int, row_number: int) -> None:
            '''create'''
            self._template_query("create.sql", book_id, title, author, year, edition, shelf_number, row_number)

        def delete(self, book_id: int) -> None:
            '''delete'''
            self._template_query("delete.sql", book_id)
        
        def search_book(self, title: str, author: str):
            '''search_book'''
            return self._template_query("search_book.sql", title, author)
        
        def search_info(self, book_id: int):
            '''search_info'''
            return self._template_query("search_info.sql", book_id)
        
        def search_person_info(self, book_id: int):
            '''search_person_info'''
            return self._template_query("search_person_info.sql", book_id)
     
    conn: sqlite3.Connection
    objects: BookObjects

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Book.BookObjects(self.conn)

class User:
    """
    Class implementing user table logic
    """

    class UserObjects:
        """
        Proxy class for users table
        """
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"user/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, str, int, str]]:
            '''all'''
            return self._template_query("all.sql")

        def create(self, first_name: str, last_name: str, patronymic: str, user_id: int, address: str) -> None:
            '''create'''
            self._template_query("create.sql", first_name, last_name, patronymic, user_id, address)

        def delete(self, user_id: int) -> None:
            '''delete'''
            return self._template_query("delete.sql", user_id)
        
        def search_user(self, first_name: str, last_name: str):
            '''search_user'''
            return self._template_query("search_user.sql", first_name, last_name)

        def search_info(self, user_id: int):
            '''search_info'''
            return self._template_query("search_info.sql", user_id)
        
        def search_books(self, user_id: int):
            '''search_books'''
            return self._template_query("search_books.sql", user_id)

    conn: sqlite3.Connection
    objects: UserObjects

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = User.UserObjects(self.conn)


class Rent:
    """
    Class implementing rentals table logic
    """

    class RentObjects:
        """
        Proxy class for rentals table
        """
        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"rent/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[int, int]]:
            '''all'''
            return self._template_query("all.sql")

        def rent_book(self, user_id: int, book_id: int) -> None:
            '''rent_book'''
            self._template_query("rent.sql", user_id, book_id)

        def delete(self, user_id: int, book_id: int) -> None:
            '''delete'''
            self._template_query("delete.sql", user_id, book_id)

        def currently_reading(self, user_id: int) -> list[tuple[int]]:
            '''currently_reading'''
            return self._template_query("currently_reading.sql", user_id)
    conn: sqlite3.Connection
    objects: RentObjects

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Rent.RentObjects(self.conn)
