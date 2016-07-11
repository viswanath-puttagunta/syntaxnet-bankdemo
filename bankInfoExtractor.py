import taggedToTree as ttt

adjd = {"average":"avg", "avg":"avg", \
	"maximum":"max", "max":"max", \
	"minimum":"min", "min":"min"}
keywordl = ['balance','debit','credit']

def cleanTree(t):
	"""Removes unnecesary nodes from tree
	   Remove things like "What is", "Who Are"
	      WP + VBZ, WP   VBP
	"""
	for node in t['children']:
		if node['pos'] == 'WP':
			wpnode = node
			vbznode = t['children'][t['children'].index(node) + 1]
			t['children'].remove(wpnode)
			t['children'].remove(vbznode)

	return t

def bankKeyWord(t):
	"""
	Input: Parsed Tree obj
	Output Tuple:
    	    (keyword, adj(optional))
	    Possible Keywords: balance, debit, credit
	    Possible Adj (optional): max, min, avg 
    	    Eg: (balance, avg)
            (debit, max)
	    (balance,)
	"""
	keyword = ""
	adj = ""

	#If root word is 'NN', this is most likely the keyword
	if (t['pos'] == 'NN'):
		if t['key'] in keywordl:
			keyword = t['key']
			#If I find the key word
			#avb,max,min is at first level child
			#unless there is determiner.
			if t['children'][0]['pos'] == 'DT':
				tadj = t['children'][1]['key']
			else:
				tadj = t['children'][0]['key']
			if tadj in adjd.keys():
				adj = adjd[tadj]
	return (keyword,adj)

def timeLine(t):
	"""
	Input: Parsed tree object
	Output: (from, to) or None
	"""
	li = list()
	ttt.getSubTree(t, 'IN', li)
	for node in li:
		print "Tree form"
		ttt.print_node(node, 0)
		print "-----"
		li2 = list()
		ttt.flattenTreeKeys(node, li2)
		print ' '.join(li2[1:])
