# search.py
import re

x = 'From: Using xyz@abc.com: Good Morning'
# Search for strings starting with 'F' followed by any characters, zero or more in number, ending with ':'
y = re.search('^F.*:', x)
print(y) # <re.Match object; span=(0, 24), match='From: Using xyz@abc.com:'> The match is greedy
y = re.search('^F.*?:', x)
print(y) # <re.Match object; span=(0, 24), match='From:'> The match is non-greedy

z = re.search('^f.*:', x)
print(z) # None

x = 'From : Using xyz@abc.com: Good Morning'
# Search for strings starting with 'F' followed by non-white-space characters, one or more in number, ending with ':'
y = re.search('^F\S+:', x)
print(y) # None