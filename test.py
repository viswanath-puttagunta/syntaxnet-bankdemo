import bankInfoExtractor as bie
import taggedToTree as ttt
import sys
import os
import subprocess

#TBD: Remove hard coding of paths
SD_PATH = '/home/vishp/linaro/tools/syntaxnet/models/syntaxnet/syntaxnet'
DEMO_CMD = 'demo.sh'
CWD = '/home/vishp/linaro/tools/syntaxnet/models/syntaxnet'
s = raw_input().lower()
cmd = 'echo "' + s + '" | ' + SD_PATH + '/' + DEMO_CMD + ' 2>/dev/null'


sno = subprocess.check_output(cmd, shell=True, cwd=CWD)

sno_st = '\n'.join(sno.split('\n')[2:]).rstrip()
print sno_st

print "-----"
root = ttt.str_to_tree(sno_st)
ttt.print_node(root, 0)

print "--- clean up tree to remove unnecessary nodes---"
root = bie.cleanTree(root)
ttt.print_node(root, 0)

print "Extracting (keyword,adj)"
(keyword,adj) = bie.bankKeyWord(root)
print "keyword: " + keyword
print "adj: " + adj

print "Extracting Timeline"
bie.timeLine(root)
