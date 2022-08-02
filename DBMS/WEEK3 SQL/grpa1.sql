select matches.match_num, referees.name
from matches, match_referees mr, referees
where matches.match_date = '2020-05-11' 
AND matches.match_num = mr.match_num 
AND referees.referee_id = mr.referee 	