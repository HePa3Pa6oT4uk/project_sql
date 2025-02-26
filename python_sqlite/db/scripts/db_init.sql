CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title VARCHAR(1024) NOT NULL,
    author VARCHAR(1024) NOT NULL,
    year INTEGER,
    edition VARCHAR(1024),
    shelf_number INTEGER,
    row_number INTEGER
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR(1024) NOT NULL,
    last_name VARCHAR(1024) NOT NULL,
    patronymic VARCHAR(1024),
    address VARCHAR(1024)
);

CREATE TABLE IF NOT EXISTS rentals (
    rent_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
);
