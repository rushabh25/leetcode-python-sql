-- Write your PostgreSQL query statement below
select case
    when id %2 = 0 then id-1
    when id %2 != 0 and id < (select max(id) as max_id from seat) then id + 1
    else id
    end as id, student
from seat
order by 1