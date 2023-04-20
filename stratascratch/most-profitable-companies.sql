-- https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3
SELECT company, profits FROM forbes_global_2010_2014 ORDER BY `profits` DESC Limit 3 ;
-- The ORDER BY keyword is used to sort the result-set in ascending or descending order.

-- The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword.