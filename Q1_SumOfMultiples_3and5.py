i = 0
three = 0
five = 0
while (i<1000):
	if(i % 3 == 0):
		three = three + i
	elif( i % 5 == 0):
		five = five + i
	i += 1
tot = three + five 
print(tot)
