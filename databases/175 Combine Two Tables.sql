# Write your MySQL query statement below

SELECT A.FirstName, A.LastName, B.City, B.State
FROM Person as A
LEFT JOIN Address as B
ON B.PersonId = A.PersonId
