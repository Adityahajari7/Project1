T = int(raw_input().strip())
N = int(raw_input().strip())
a= str(raw_input())


k = "RBG"
r=0
b=0
g=0
for i in range(N):
  
    if a[i]==k[0]:
        r=r+1
    elif a[i]==k[1]:
     	b=b+1
    		
    elif a[i]==k[2]:
            	
        g=g+1
p = max(r,b,g)
maximum_rooms = N-g
print maximum_rooms