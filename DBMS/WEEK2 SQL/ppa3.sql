SELECT BC.title
from book_authors BA, book_catalogue BC
where (BA.isbn_no = BC.isbn_no) and (BA.author_fname = 'Joh Paul') and (BA.author_lname = 'Mueller')