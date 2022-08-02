select student_fname, student_lname
from students stu, members mem
where mem.roll_no = stu.roll_no
and mem.member_no in (select member_no
					 from book_issue)
					 
