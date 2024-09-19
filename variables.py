
d='Todays\'s weather is nice'
print("single line variable")
print(d)
print(d[14]) #d[14] = print the 14 index letter in the varible

d= "Today's weather is nice"
print("double quote variable")
print(d)
print("#printing required letters using slicing concept +ve indexing")
print(d[4:9+1]) # this is slicing conecpt, this is positive indexing
print("#printing required letters using slicing concept -ve indexing")
print(d[-4:-9+1]) # this is slicing conecpt, this is negative indexing

d= """Today weather is nice"""
print("3 quotes variable")
print(d)

#this is list
test_list=["Hello", "world"]

#this is tuple
test_tuple=("hello", "world")

#this is dict
test_dict={'a':1, 'b':2}

#this is set
test_set={'a','b',"c"}

print("#one way of printing output in new lines")
print(test_tuple)
print(test_dict)
print(test_set)
print(test_tuple)
print("#one way of printing output in single line")
print(test_set,test_dict,test_set,test_tuple)
print("#another way of printing output in new line")
print(f"{test_list},\n{test_tuple},\n{test_dict},\n{test_set}")
print("#another way of print output in new line")
print(f"List: {test_list}\nTuple: {test_tuple}\nDictionary: {test_dict}\nSet: {test_set}")

a=12
print(a)

b=3

c=a+b

#Add
print(c, type(c))

#Mult
d = a*b
print(d, type(d))

#Sub
e=a-b
print(e, type(e))

#Division
f=a/b
print(f, type(f))

# integer division
g=a//b
print(g,type(g))

#Module division
h=a%b
print(h, type(h))

# concatenation
a="2"
b="3"

print(a+b)

#power

a =2
print(a**3) 

# comparsion operators

a=10
b=20

res1=a>b
res2=a<b
res3=a>=b
res4=a<=b
res5=a==b
res6=a!=b
print(res1,res2,res3, res4, res5, res6)

# logical operators
a =True # true is not correct
b=False

res1=a and b
res2=a or b
res3=not a
res4=not b
print(res1,res2,res3,res4)