# Input for today
aocin=open("2.txt","r").read().split("/n")

# Part 1
j=[0,0]
for i in aocin:
	if(i.split(" ")[0]=="forward"):j[1]+=int(i.split(" ")[1])
	if(i.split(" ")[0]=="up"):j[0]-=int(i.split(" ")[1])
	if(i.split(" ")[0]=="down"):j[0]+=int(i.split(" ")[1])
print(j[0]*j[1])

# Part 2
j=[0,0]
aim=0
for i in aocin:
	if(i.split(" ")[0]=="forward"):
		j[1]+=int(i.split(" ")[1])
		j[0]+=int(i.split(" ")[1])*aim
	if(i.split(" ")[0]=="up"):aim-=int(i.split(" ")[1])
	if(i.split(" ")[0]=="down"):aim+=int(i.split(" ")[1])
print(j[0]*j[1])
