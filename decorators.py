import re
import sys

def amend(func):
    def stdnum(mob_list):
    	for i in xrange(len(mob_list)):
    		midpoint = len(mob_list[i]) // 2
    		mob_list[i] = "+91 " + mob_list[i]


        func(mob_list)
    # return object ref of the 'new func'
    return stdnum


@amend
def sort_nums(mob_list):
	mob_list.sort()
	print("\n".join(mob_list))

mob = []
l = "start"

while l != "":
	l = raw_input()
	mob.append(l)

sort_nums(mob)
