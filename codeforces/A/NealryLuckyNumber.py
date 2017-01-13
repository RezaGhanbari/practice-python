from __future__ import print_function

s = raw_input()
print(['YES', 'NO'][s.count('4') + s.count('7') not in [4, 7]])
