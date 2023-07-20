-- lists number of records
SELECT `score`, count(*) AS `number`
FROM `second_table` GROUP BY `score`
order by `number` desc;
