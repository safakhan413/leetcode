-- https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
-- Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: 

-- Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

-- Note:

-- The tables may contain duplicate records.
-- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.
-- Input Format

-- The following tables contain company data:
 
-- Company: The company_code is the code of the company and founder is the founder of the company. 

-- Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company. 

-- Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 

-- Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 

-- Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 

-- Sample Input

-- Company Table:  Lead_Manager Table:  Senior_Manager Table:  Manager Table:  Employee Table: 

-- Sample Output

-- C1 Monika 1 2 1 2
-- C2 Samantha 1 1 2 2
-- Explanation

-- In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.

-- In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.

-- 1
-- /*
-- 2
-- Enter your query here.
-- 3
-- */
-- Line: 1 Col: 1
-- Run Code Submit CodeUpload Code as File
-- Blog


/*
Enter your query here.
*/
select DISTINCT c.company_code, c.founder, count(DISTINCT lm.lead_manager_code) as total_lm, count(DISTINCT sm.senior_manager_code)  as total_sm, count(DISTINCT m.manager_code)  as total_m,
count(DISTINCT e.employee_code)  as total_e

-- ,lm.lead_manager_code, sm.senior_manager_code, 

from company c
left join lead_manager lm on c.company_code = lm.company_code
left join senior_manager sm on lm.company_code=sm.company_code and  lm.lead_manager_code = sm.lead_manager_code 
left join manager m on sm.company_code=m.company_code and  sm.senior_manager_code = m.senior_manager_code
left join employee e on m.company_code=e.company_code and  m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code ASC;