print "Type number of array elements"
N = raw_input()

N=int(N)
print "Input array elements one by one"
A1=[]
for i in range(N):
    n = raw_input()
    n = str(n)
    A1.append(n)

j = raw_input()
j = int(j)
A2= []
for i in range(j):
    k = raw_input()
    k = int(k)
    A2.append(k)
for i in range(j):
	if i==0:
		A1.remove(A1[A2[i]])
	else:
		A2[i]=A2[i]-i
		A1.remove(A1[A2[i]])
print A1
