-- displays max temperature in each state
SELECT city, max(`value`) AS max_temp
FROM temperatures
group by city
order by max_temp DESC;
