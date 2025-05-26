'''
range() returns a sequence of numbers syntax: range(start,stop,step)
default start is 0,step is 1
negetive step for reverse order
'''
#list,tuple,set,dict
print(list(range(1,10)))
print(list(range(-100,101)))
#100,1
print(list(range(100,0,-1)))
#1-50 even numbers with the help of range step size 2
print(list(range(2,50,2)))
#print 0 to 30
print(list(range(31)))

''' Interaction is the repeated execution of a process in
loops. Each pass through a loop is called an interation,

it allows automatic handing of multiple items without manual retition.'''
'''Iterables in python are objects that can be looped over or iterated through.Example are list,
tuple,set,range,string etc'''
