-- This will list all the records of the table second_table having a name value.
-- The records will be ordered in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
