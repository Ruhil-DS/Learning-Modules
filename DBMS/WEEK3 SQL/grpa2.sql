select ply.name
from players ply, teams
where teams.name = 'All Stars' and ply.team_id = teams.team_id
order by ply.dob desc
limit 1
