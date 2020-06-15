people =["cha", 'cat', 'cath']
# do all of the people have a name that starts with c
all([name[0]=='c' for name in people])

people2 =["cha", 'cat', 'cath', 'ste']
# do any name start with c
any([name[0]=='c' for name in people2])

# can just do this
# ie you don't need alist .its called a generator expression
# if you are just passing it into any function and don't want list
# at the end of it - use a generator expression
# https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension
any(name[0]=='c' for name in people2)

