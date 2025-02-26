SELECT
    book_id,
    row_number,
    shelf_number
FROM
    books
WHERE
    (title LIKE '%' || ? || '%')
    AND (author LIKE '%' || ? || '%');
