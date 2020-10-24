SELECT
    IFNULL(
    (SELECT Salary 
    FROM Employee
    ORDER BY Salary ASC
    LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary 