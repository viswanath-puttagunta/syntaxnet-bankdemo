#!/usr/bin/python

s1 = ("balance NN ROOT\n"
" +-- maximum JJ amod\n"
" +-- since IN prep\n"
"     +-- January NNP pobj\n"
"         +-- 2015 CD num")

s2 = ("doing VBG ROOT\n"
" +-- Hello UH discourse\n"
" |   +-- Vish JJ dep\n"
" |       +-- how WRB advmod\n"
" |       +-- are VBP cop\n"
" |       +-- you PRP nsubj\n"
" +-- , , punct\n"
" +-- I PRP nsubj\n"
" +-- am VBP aux\n"
" +-- fine RB advmod")

def line_to_node(line, parent_node):
	a = dict()
	a['key'] = line[0]
	a['pos'] = line[1]
	a['other'] = line[2]
	a['parent'] = parent_node
	a['children'] = list()
	if parent_node != None:
		parent_node['children'].append(a)
	return a

def find_begin_spaces(line):
	l = line.split(' ')
	spaces = 1
	cp = 1
	while((l[cp] == '') | (l[cp] == '|')):
		if l[cp] == '':
			spaces += 1
			cp += 4
		else:
			cp += 3
			spaces += 1
	#should have reached '+--'
	cp += 1
	return (spaces, l[cp:])

def parse_line(stack, lines, curr):
	spaces,cline = find_begin_spaces(lines[curr])
	a = line_to_node(cline, stack[-1])

	#if we're the last line, we're done
	if (len(lines) != curr + 1):
		next_spaces,x = find_begin_spaces(lines[curr+1])
		if (next_spaces > spaces):
			#We're looking at one of our children
			#Push yourself onto stack and get out
			stack.append(a)
		elif next_spaces < spaces:
			#need to pop sufficient parents out of stack
			num_pops = spaces - next_spaces
			i = 0
			while i < num_pops:
				stack.pop(-1)
				i+=1
	return stack


def str_to_tree(s):
	lines = s.split('\n')

	root = line_to_node(lines[0].split(' '), None)

	stack = list()
	stack.append(root)

	curr = 1
	while(curr < len(lines)):
		stack = parse_line(stack, lines, curr)
		curr += 1
	return root

def print_node(node, spaces):
	s = ""
	for i in range(spaces):
		s += '\t'
	print "%s %s" % (s, node['key'])
	for child in node['children']:
		print_node(child, spaces+1)

def getSubTree(t, pos, li):
	"""
	Input: Parsed tree object
	Output: (list of) Subtree that has requested pos
	"""
	for child in t['children']:
		if child['pos'] == pos:
			li.append(child)
		else:
			getSubTree(child, pos, li)

def flattenTreeKeys(t, li):
	"""
	Returns list of keys (words)
	"""
	li.append(t['key'])
	for node in t['children']:
		flattenTreeKeys(node,li)


if __name__ == '__main__' :
	print "-------"

	root = str_to_tree(s1)
	print_node(root, 0)

	root = str_to_tree(s2)
	print_node(root, 0)


