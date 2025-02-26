SELECT
    first_name,
    last_name,
    patronymic
FROM
    users
WHERE
    user_id = ?;
