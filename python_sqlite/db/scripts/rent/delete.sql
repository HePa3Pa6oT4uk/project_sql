DELETE FROM users
WHERE
    user_id = ?
    AND
    book_id = ?;
