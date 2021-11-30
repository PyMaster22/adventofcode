# Input for Today
aocin=open("1.txt","r").read().split(", ")

# Part 1
pos=complex(0,0)
dir=complex(1,0)
for i in aocin:
	if(i[0]=="L"):
		dir*=0+1j
	if(i[0]=="R"):
		dir*=0-1j
	pos+=dir*int(i[1:])
print(abs(pos.real)+abs(pos.imag))
