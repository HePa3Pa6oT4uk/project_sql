SELECT
    user_id
FROM
    users
WHERE
    (first_name LIKE '%' || ? || '%')
    AND (last_name LIKE '%' || ? || '%');
