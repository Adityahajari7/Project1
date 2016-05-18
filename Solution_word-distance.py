print "Type the sentence"
p = str(raw_input())
b=[' ']
n=0
for i in range(len(p)):
	if p[i]==b[0]:
		n=n+1
		

a = map(str,p.strip().split(' '))

 
print "now type the two words one by one"
c=[]
for i in range(2):
	c1= str(raw_input())
	c.append(c1)
t=[]
f=[]
for j in range(n+1):
	if a[j]==c[0]:
		t1=j
		t.append(j)
	
	
	elif a[j]==c[1]:
		
	    f.append(j)
m=[]	    

for i in range(len(f)):
 	for j in range(len(t)):
 		m1=f[i]-t[j]
 		m.append(m1)
print m 		
print "the distance between two words is "
print  min(abs(x) for x in m)