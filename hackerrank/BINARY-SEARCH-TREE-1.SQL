-- https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

-- You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.



-- Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

-- Root: If node is root node.
-- Leaf: If node is leaf node.
-- Inner: If node is neither root nor leaf node.
-- Sample Input



-- Sample Output

-- 1 Leaf
-- 2 Inner
-- 3 Leaf
-- 5 Root
-- 6 Leaf
-- 8 Inner
-- 9 Leaf

-- Explanation

-- The Binary Tree below illustrates the sample:





-- INPUT
-- Expected Output
-- 1 Leaf 
-- 2 Inner 
-- 3 Leaf 
-- 4 Inner 
-- 5 Leaf 
-- 6 Inner 
-- 7 Leaf 
-- 8 Leaf 
-- 9 Inner 
-- 10 Leaf 
-- 11 Inner 
-- 12 Leaf 
-- 13 Inner 
-- 14 Leaf 
-- 15 Root


SELECT n,
CASE
    WHEN p IS NULL THEN 'Root'
    WHEN n NOT IN (SELECT p FROM bst WHERE p IS NOT NULL) THEN 'Leaf'
    ELSE 'Inner'
END AS type
FROM bst
ORDER BY N ASC
