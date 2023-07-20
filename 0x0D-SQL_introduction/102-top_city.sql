-- displays top 3 of cities temperature
SELECT city, AVG(`value`) AS  avg_temp
FROM temperatures
where month=7 or month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
