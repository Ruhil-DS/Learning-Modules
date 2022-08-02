select distinct teams.name
from teams, players
where players.team_id = teams.team_id
and players.team_id not in (select team_id
							 from players
							 where jersey_no = 74)