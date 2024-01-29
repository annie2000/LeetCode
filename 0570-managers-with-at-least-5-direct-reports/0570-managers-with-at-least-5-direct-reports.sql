# Write your MySQL query statement beloww


# with t as (
#     select e2.name as name
#         ,count(*) ct
#     from employee e1
#     left join employee e2
#     on e2.id = e1.managerId
#     group by e1.managerId
#     having ct>=5
# )
# select Name
# from t
# where name is not null

with mgr as(
    select distinct(managerId) mgr, count(id) over(partition by managerId) ct
    from Employee
    )
select name
from Employee 
where id in (select mgr from mgr where ct>=5 )

    
