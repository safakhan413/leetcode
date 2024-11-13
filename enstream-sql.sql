select e.name, d.departmentName
from Employees e
join department d
on e.DepartmentID = d.DepartmentID
where e.salary > (
    select avg(e2.salary)
    from Employees e2
    -- join department d2 on e2.DepartmentID = d2.DepartmnetID
    -- group by d2.departmentName
    where e2.DepartmentID = e.DepartmnetID
    
) 


