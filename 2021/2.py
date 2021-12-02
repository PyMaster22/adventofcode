# Input for today
aocin=open("2.txt","r").read().split("/n")

# Part 1
j=[0,0]
for i in aocin:
	if(i.split(" ")[0]=="forward"):j[1]+=int(i.split(" ")[1])
	if(i.split(" ")[0]=="up"):j[0]-=int(i.split(" ")[1])
	if(i.split(" ")[0]=="down"):j[0]+=int(i.split(" ")[1])
print(j[0]*j[1])
