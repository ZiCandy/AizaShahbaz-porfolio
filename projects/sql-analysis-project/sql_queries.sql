-- SQL Data Analysis Project
-- Objective: Analyze a simple sales dataset

-- Create a sample table
CREATE TABLE sales (
    id INT,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    amount INT,
    purchase_date DATE
);

-- Insert sample data
INSERT INTO sales VALUES
(1, 'John', 'NY', 500, '2024-01-01'),
(2, 'Sara', 'LA', 700, '2024-01-02'),
(3, 'Mike', 'NY', 300, '2024-01-03'),
(4, 'Anna', 'Chicago', 900, '2024-01-04'),
(5, 'Tom', 'LA', 400, '2024-01-05');

-- Total sales
SELECT SUM(amount) AS total_sales FROM sales;

-- Sales by city
SELECT city, SUM(amount) AS city_sales
FROM sales
GROUP BY city
ORDER BY city_sales DESC;

-- Top customer
SELECT customer_name, amount
FROM sales
ORDER BY amount DESC
LIMIT 1;

-- Average purchase amount
SELECT AVG(amount) AS avg_purchase FROM sales;
