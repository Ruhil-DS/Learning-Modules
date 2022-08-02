select bc.title, cnt
from book_catalogue as bc, (
							select isbn_no, count(*) as cnt
							from book_copies
							group by isbn_no
							) as book_count
where title like '%Database%' and bc.isbn_no = book_count.isbn_no
