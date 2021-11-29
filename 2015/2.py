# Input for today
aocin=[i.split("x") for i in open("2.txt","r").read().split("\n")]

# Part 1
def func(a,b,c):
  if(c<a>=b or c<=a>b):return(b*c)
  if(a<b>=c or a<=b>c):return(a*c)
  if(b<c>=a or b<=c>a):return(a*b)
  if(a==b==c):return(a*b)
area=lambda l,w,h:2*l*w+2*w*h+2*h*l
j=0
for i in aocin:
  j+=area(int(i[0]),int(i[1]),int(i[2]))+func(int(i[0]),int(i[1]),int(i[2]))
print(j)

# Part 2
def func(a,b,c):
  if(c<a>=b or c<=a>b):return(b+c)
  if(a<b>=c or a<=b>c):return(a+c)
  if(b<c>=a or b<=c>a):return(a+b)
  if(a==b==c):return(a+b)
j=0
for i in aocin:
  j+=int(i[0])*int(i[1])*int(i[2])+2*func(int(i[0]),int(i[1]),int(i[2]))
print(j)
