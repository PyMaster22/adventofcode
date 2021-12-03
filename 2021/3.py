# Input for Today
aocin=open("3.txt","r").read().split("\n")

# Part 1
gamma=""
for i in range(len(aocin[0])):
	ones=0
	for j in range(len(aocin)):
		if(aocin[j][i]==1):ones+=1
	if(ones>500):gamma+="1"
	else:gamma+="0"
epsilon="".join([("1","0")[int(i)] for i in gamma])
print(int(gamma,2)*int(epsilon,2))
