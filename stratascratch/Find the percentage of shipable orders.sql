-- both for amazon and google
-- Find the percentage of shipable orders.
-- Consider an order is shipable if the customer's address is known.

-- Tables: orders, customers

-- It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

-- We will have to use the IS NULL and IS NOT NULL operators instead.
-- SQL aliases are used to give a table, or a column in a table, a temporary name.

-- Aliases are often used to make column names more readable.

-- An alias only exists for the duration of that query.

-- An alias is created with the AS keyword.


SELECT COUNT(*) AS total,
    (SELECT COUNT(*) FROM customers t1 inner JOIN orders t2
                         ON t2.cust_id = t1.id where t1.address is not null) AS num_orders_percent
FROM customers s
inner JOIN orders o
    ON o.cust_id = s.id

-- need to complete later