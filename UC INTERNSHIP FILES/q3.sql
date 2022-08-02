select mnth, deliveries, active_pros, (deliveries*1.0)/active_pros as utilization
from (select to_char(bdate_final, 'YYYY-MM') as MNTH, 
count(*) as Deliveries, 
count(distinct responded_pro_booking) as active_pros
from uc
group by mnth) as sub