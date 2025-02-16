-- Write your PostgreSQL query statement below
with cte as (
    select * ,
    min(event_date) over (partition by player_id) as first_date,
    lead(event_date, 1) over (partition by player_id order by event_date) as lead_date
    from activity
) , cte2 as (
    select count(distinct player_id) as dist_players from cte where lead_date - first_date = 1
), cte3 as (
    select count(distinct player_id) as total_players from activity
)
select round(dist_players * 1.0 /total_players, 2) as fraction from cte2, cte3