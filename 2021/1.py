# Input for today
aocin=[int(i) for i in open("1.txt","r").read().split("\n")]

# Part 1
char=0
great=0
while(char<len(aocin)):
	if(char==0):pass
	elif(aocin[char]>aocin[char-1]):great+=1
	char+=1
print(great)

# Part 2
char=0
great=0
while(char<len(aocin)-2):
	if(char==0):pass
	elif((aocin[char]+aocin[char+1]+aocin[char+2])>(aocin[char-1]+aocin[char]+aocin[char+1])):great+=1
	char+=1
print(great)
