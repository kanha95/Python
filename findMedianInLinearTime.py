x = []
y = []


def input_S(n):
	
	for i in range(0,n):
		z = raw_input().split()
		x.append(int(z[0]))
		y.append(int(z[1]))

	return zip(x,y)



pairs = input_S(int(raw_input("Input Size")))

def find_Median(xx, ind):
	pivot = xx[ind]

	low = []
	high = []

	

	for i in range(0,len(xx)):

		if i!=ind and xx[i]<=pivot:
			low.append(xx[i])
		elif i!=ind and xx[i]>pivot:
			high.append(xx[i])




	if len(low)==ind:
		print
		return pivot

	elif len(low)>ind:
		return find_Median(low, ind)

	else: return find_Median(high, len(x)-ind-1)
	

print find_Median(x,len(x)/2)	



	
