SELECT u.user_id, u.first_name, u.last_name
FROM rents AS r
JOIN users AS u ON r.user_id = u.user_id
WHERE book_id = ?;
