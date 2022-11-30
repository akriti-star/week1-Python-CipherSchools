n=5
for i in range (n):
    for j in range (n):
        print(j,end=" ")
    print()

for i in range (n):
    for j in range (n):
        print(max(i,j),end=" ")
    print()


for i in range (n):
    for j in range (n):
        print(n-i,end=" ")
    print()

for i in range (n):
    for j in range(n) :
        print(
            max(max(i+1,j+1),max(n-j,n-i 
            )),end= " ")
    print()