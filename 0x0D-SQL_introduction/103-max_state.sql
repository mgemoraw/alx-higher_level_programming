-- displays max temperature in each state
SELECT `state`, max(`value`) AS max_temp
FROM temperatures
group by `state`
order by `state` DESC;
