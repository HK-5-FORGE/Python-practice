# Variables is basically a name assigned to referrence a value
'''rules for naming variables::
variable names canonly contain letters, digits andunderscore
a variable name can not start with a digit
variable names are case sensitive
avoid using python keywords'''

age = 21
_colour = "black"
total_marks = 98
print(age, _colour, total_marks)

# Dynamic typing
x = 10
x = 'now a string'
print(x)
'''here we can see that variable is just referrencing the value and not holding it as xwas referrencing to 10 first and then when it referrenced to the next value the old value that was 10 was put in garbage'''

# multiple assignment
a=b=c=100
print(a,b,c)

u,v,w=1,2.80,'python'
print(u,v,w)