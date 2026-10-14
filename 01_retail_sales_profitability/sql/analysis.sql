-- SQLite compatible; load orders.csv into a table named orders first.
SELECT category, ROUND(SUM(quantity*unit_price*(1-discount_rate)),2) AS revenue, ROUND(SUM(quantity*(unit_price*(1-discount_rate)-unit_cost)),2) AS gross_profit FROM orders GROUP BY category ORDER BY revenue DESC;
SELECT region, ROUND(SUM(quantity*(unit_price*(1-discount_rate)-unit_cost)),2) AS gross_profit FROM orders GROUP BY region ORDER BY gross_profit DESC;
SELECT substr(order_date,1,7) AS month, ROUND(SUM(quantity*unit_price*(1-discount_rate)),2) AS revenue FROM orders GROUP BY month ORDER BY month;
