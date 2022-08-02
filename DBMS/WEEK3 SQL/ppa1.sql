select teams.name
from (select host_team_id as team_id_comb, count(*) as match_count
		from matches
		group by team_id_comb
		union all
		select guest_team_id as team_id_comb, count(*)
		from matches
		group by team_id_comb
		) as team_count, teams
where  match_count > 3 
and team_count.team_id_comb=teams.team_id