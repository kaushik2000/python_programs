# find_all.py
import re

x = 'From: Using xyz@abc.com: Good Morning GMT + 5:30'
# Find all strings starting with 'F' followed by any characters, zero or more in number, ending with ':'
y = re.findall('^F.*:', x)
print(y) # ['From: Using xyz@abc.com:'] The match is greedy
y = re.findall('^F.*?:', x)
print(y) # ['From:'] The match is non-greedy

# Find all vowels in the string x
z = re.findall('[AEIOU]', x)
print(z) # ['U']
z = re.findall('[aeiou]', x)
print(z) # ['o', 'i', 'a', 'o', 'o', 'o', 'o', 'i']

# Using range
z = re.findall('[0-9]', x)
print(z) # ['5', '3', '0']
z = re.findall('[A-Z0-9]', x)
print(z) # ['F', 'U', 'G', 'M', 'G', 'M', 'T', '5', '3', '0']

x = 'From : Using xyz.org@abc.com : Good Morning'
# Find all strings starting with 'F' followed by non-white-space characters, one or more in number, ending with ':'
y = re.findall('^F\S+:', x)
print(y) # []

# Fine-tuning string extraction
y = re.findall('\S+@\S+', x)
print(y) # ['xyz.org@abc.com']
y = re.findall('\S+@\S+?', x) # Non-greedy
print(y) # ['xyz.org@a']

# Precise matching : parenthesis points out which part of the matched string is to be extracted
y = re.findall('^From.+ (\S+@\S+)', x)
print(y) # ['xyz.org@abc.xyz.orcom']
y = re.findall('^From.+(\S+@\S+)', x)
print(y) # ['g@abc.com']

y = re.findall('@([^ ]*)', x) # More precise: y = re.findall('^From .*@([^ ]*)', x)
print(y) # ['abc.com']

# Escape sequence
x = 'We have $10.00 savings left'
y = re.findall('\$[0-9.]+', x)
print(y) # ['$10.00']