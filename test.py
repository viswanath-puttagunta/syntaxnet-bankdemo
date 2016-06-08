import bankInfoExtractor as bie
import taggedToTree as ttt


root = ttt.str_to_tree(ttt.s1)
ttt.print_node(root, 0)

li = list()

ttt.getSubTree(root, 'IN', li)

print "len of subtree list: %d" % len(li)

for node in li:
	print "--------"
	ttt.print_node(node, 0)
	print "--------"
