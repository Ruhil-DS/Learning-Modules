select * 
from uc 
where (cast(bdate_final as time ) between '10:26:00' and '23:00:00')
and date(bdate_final) = '2020-07-21'
