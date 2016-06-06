#!/usr/bin/python

months = ["January", "February","March","April"]
#	  "May", "June","July","August",
#	  "September", "October", "November", "December"]

years = ["2015", "2016"]

def gen_since(mli, yli):
	li = []
	for m in mli:
		for y in yli:
			li.append("since %s %s" % (m,y))
	return li

def gen_from_to(mli, yli):
	li = []
	for m in mli:
		li.append("from %s %s to %s %s" % (m, yli[0],m, yli[1]))
	return li

mkeys = ["balance", "debit", "credit"]
adjkeys = ["maximum", "minimum", "average", "total"]

def genqs(akeys, mkeys, m, y):
	li = []
	since_li = gen_since(m,y)
	from_to_li = gen_from_to(m,y)
	for ak in akeys:
		for mk in mkeys:
			for since_el in since_li:
				li.append("%s %s %s" % (ak, mk, since_el))
			for from_to_el in from_to_li:
				li.append("%s %s %s" % (ak, mk, from_to_el))
	return li

li3 = genqs(adjkeys, mkeys, months, years)
for si in li3:
	print si
