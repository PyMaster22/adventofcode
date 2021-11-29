# Input for today.
aocin=open("1.txt","r").read()

# Part 1
print(aocin.count("(")-aocin.count(")"))

# Part 2
lvl=0
char=0
while(lvl>-1):lvl,char=[(lvl+1,lvl-1)[aocin[char]==")"],char+1]
print(char)
