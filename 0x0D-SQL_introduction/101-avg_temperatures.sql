-- Compute the average using AVG
SELECT city, ROUND(avg(value)) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
