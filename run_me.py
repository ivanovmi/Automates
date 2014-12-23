from __future__ import division
count = 3
variable=[]
while count != 0:
	variable.append(int(raw_input('Enter the value of variable: ')))
	count -= 1
print '%s' % str(sum(variable)+reduce(lambda x,y: x*y, variable))+'/%s' % str(reduce(lambda x,y: x*y, variable))