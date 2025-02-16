-- Write your PostgreSQL query statement below
with cte as (
select id,visit_date,
lag(people, 2) over (order by id) as lag2,
lag(people, 1) over (order by id) as lag1,
people,
lead(people, 1) over (order by id) as lead1,
lead(people, 2) over (order by id) as lead2
from stadium
)
select id, visit_date, people from cte
where (lag2 >= 100 and lag1 >= 100 and people >= 100) or
    (lag1 >= 100 and people >= 100 and lead1 >= 100) or
    (people >= 100 and lead1 >= 100 and lead2 >= 100)
