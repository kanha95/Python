a=3
b=5


print b if a<b else a

#or

print (a, b)[a<b]

#or

print (lambda : a, lambda : b)[a<b]()
