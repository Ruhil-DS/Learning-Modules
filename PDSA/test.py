import re

#Check if the string starts with "The" and ends with "Spain":

t = """
abcd@gmail.com
abcd@gmail_com
foiferer@yahoo.com
21f2001180@student.onlinedegree.iitm.ac.in

"""

p = re.compile(r"\w*@gmail.com")

matches = p.finditer(t)

for match in matches:
	# print(dir(match))
	print(match.span())
