select to_char(bdate_final, 'YYYY-MM') as MNTH, count(*) as DELIVERIES
from uc
group by MNTH