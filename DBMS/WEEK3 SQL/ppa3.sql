select count(*)
from book_catalogue c, book_copies bc,(select accession_no 
									   from book_issue 
									   where doi='2021-08-11' ) as a
where c.isbn_no=bc.isbn_no and a.accession_no=bc.accession_no