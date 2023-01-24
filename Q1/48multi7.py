
i = 1
counter = 0
goal = 0

while ( counter < 48 ):
	
	while i%7 != 0 :
		i+=1
	#print(i,"is a multiple of 7")

	if str(7) in str(i):
		goal = i
		counter+=1
		#print(i,"includes 7")
		print(counter, i)
	i+=1

print("The 48th multiple of 7 that contains 7 is:", goal)

