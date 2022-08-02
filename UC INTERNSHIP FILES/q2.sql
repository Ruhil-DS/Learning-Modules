select to_char(bdate_final, 'yyyy-mm') as MNTH, count(distinct responded_pro_booking) as active_pro
from uc
group by mnth

