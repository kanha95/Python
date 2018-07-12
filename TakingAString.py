

temp1 = map(int, raw_input().split())

#or

temp2 = [int(i) for i in raw_input().split()]

#or

temp3 = map(lambda x: int(x), raw_input().split())

print temp1[2]

print temp2[1]

#input
# 3 2 4
# 4 3 2 1

#output
#4
#3
