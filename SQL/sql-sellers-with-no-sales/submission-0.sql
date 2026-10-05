SELECT seller_name
FROM seller
WHERE seller_id NOT IN (
    SELECT seller_id
    FROM seller
    JOIN orders USING (seller_id)
    WHERE sale_date < '2021-01-01' AND sale_date >= '2020-01-01'
    GROUP BY seller_id, seller_name
)
ORDER BY seller_name ASC;