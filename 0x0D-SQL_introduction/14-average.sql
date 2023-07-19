-- script that computes the socre average
-- of all records in the second_table
ALTER TABLE second_table ADD average INT;
UPDATE second_table SET average SUM(socre)/COUNT(score);