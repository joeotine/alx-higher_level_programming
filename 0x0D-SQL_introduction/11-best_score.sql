-- This will list all the records in the table second_table with a score >= 10.
-- The records will be ordered in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
