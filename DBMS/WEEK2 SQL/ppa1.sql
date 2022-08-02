select M.name
from managers M, teams T
where (M.team_id = T.team_id) AND (T.name = 'All Stars')