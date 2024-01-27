# Write your MySQL query statement below

select c.customer_id, c.customer_name
from Customers c
left join Orders o
on c.customer_id = o.customer_id
group by c.customer_id
having sum(product_name = "A") > 0
        and sum(product_name = "B") > 0
        and sum(product_name = "C") = 0
order by 1