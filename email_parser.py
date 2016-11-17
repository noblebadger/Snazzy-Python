

"""
MY NOTE:
assingment to x makes new list 
the e before the 'for' is not 
the new list only the temp place
holder for each item in em. I assume 
the first occurence of e is to allow
operations to be done on e post assingment

"""
import sys
import re

x = [e for e in sys.stdin if re.match("[A-z]+\s<[a-z](\w|\.|\_|-)+@[a-z]+\.[a-z]{1,3}>$", e) != None]
print("".join(x))