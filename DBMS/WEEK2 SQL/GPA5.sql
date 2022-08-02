select F.faculty_fname, F.faculty_lname
from faculty F, departments D
where (F.department_code = D.department_code) and (D.department_name = 'Computer Science')