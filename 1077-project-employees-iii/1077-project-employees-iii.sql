# Write your MySQL query statement below


with t as (
    select p.project_id, p.employee_id, e.name, e.experience_years,
    rank() over(partition by p.project_id order by e.experience_years desc) rnk
    from Project p
    left join Employee e
    on p.employee_id = e.employee_id
    
)

select project_id, employee_id
from t
where rnk =1