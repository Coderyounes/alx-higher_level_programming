-- Compute the average using AVG
SELECT city, avg(value) AS temp FROM temperatures GROUP BY city ORDER BY temp DESC; 
