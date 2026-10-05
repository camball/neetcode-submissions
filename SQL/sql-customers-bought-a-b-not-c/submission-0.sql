SELECT customer_id, customer_name
FROM customers c
JOIN orders o USING (customer_id)
GROUP BY customer_id
HAVING
    COUNT(CASE WHEN o.product_name = 'A' THEN 1 END) > 0
    AND COUNT(CASE WHEN o.product_name = 'B' THEN 1 END) > 0
    AND COUNT(CASE WHEN o.product_name = 'C' THEN 1 END) = 0
ORDER BY customer_name;