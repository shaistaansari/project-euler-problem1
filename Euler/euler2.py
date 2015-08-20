a=0
b=1
solution=0

while b <=4000000:
	if b % 2 == 0:
		solution += b
	a,b = b, a+b
print "The sum of even valued terms in Fibonacci sequence whose value does not exceed 4 million is:",(solution)