sample_str="This-is-sample-string"

#Accessing individual chars from string

print(sample_str[8])

#slicing

sub_str=sample_str[2:7]
print(sub_str)

sub_str=sample_str[:]
print(sub_str)

sub_str=sample_str[1:]
print(sub_str)

sub_str=sample_str[:5]
print(sub_str)

sub_str=sample_str[::2]
print(sub_str)

sub_str=sample_str[::-1]
print("Reverse of string:",sub_str)

len_str=len(sample_str)
print("lenght of sample string is:",len_str)

#Methods

sample_str="hello"
print(sample_str.capitalize())

sample_str="HELLO"
print(sample_str.casefold())

#split, join, format, count, string 


#split

sample_str="This is sample string"
sub_str=sample_str.split()
print(sub_str, type(sub_str)), #return the output in list 

#join
join_str=" ".join(sub_str)
print(join_str, type(join_str))

join_str=" #".join(sub_str)
print(join_str,type(join_str))

#count
sample_str="This is a a sample string"
count_str=sample_str.count('a')
print(count_str)

# strip, lstrip(), rstrip()
sample_str="   This is a a sample string     "
strip_str=sample_str.strip()
print(strip_str, type(strip_str))

sample_str="   This is a a sample string     "
strip_str=sample_str.lstrip()
print(strip_str, type(strip_str))

sample_str="   This is a a sample string     "
strip_str=sample_str.rstrip()
print(strip_str, type(strip_str))


