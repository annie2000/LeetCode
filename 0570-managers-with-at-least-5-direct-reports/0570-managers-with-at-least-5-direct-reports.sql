# Write your MySQL query statement below

with cte as (
    select id, name, managerId, count(id) over(partition by managerId) ct
    from Employee
)
select name 
from employee
where id in (select managerId from cte where ct>=5)
