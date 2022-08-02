select P.name
from players P, teams T
where (P.team_id = T.team_id) and (T.name = 'All Stars')