# Write your MySQL query statement below

#write a solution to report the IDs of the transctions with the maximum amount on their respective day.

with cte as (
    select transaction_id
            , day
            , amount
            , dense_rank() over(partition by day order by amount desc) as drk
    from Transactions
)
select transaction_id
from cte
where drk = 1
order by transaction_id
