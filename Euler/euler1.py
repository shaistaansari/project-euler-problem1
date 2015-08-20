num = []

for i in range(1,1000):
	if i % 3 == 0 or i % 5 == 0:
		num.append(i)


print "The sum all the multiples of 3 or 5 below 1000 is ", sum(num)