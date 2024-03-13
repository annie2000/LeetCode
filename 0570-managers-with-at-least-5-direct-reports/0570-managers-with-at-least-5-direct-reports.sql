# Write your MySQL query statement below

with cte as (
    select *, count(id) over(partition by managerId) ct
    from employee
)
select name
from employee
where id in (select managerId from cte where ct>=5)
