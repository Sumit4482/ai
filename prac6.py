# Implement any cryptarithmetic puzzle. 

from itertools import permutations
flag=0
n=int(input("Enter the number of strings: "))
arr=[]
for i in range(n):
    arr.append(str(input("Enter the string: ")))
s=str(input("Enter the string which is should be equal: "))
q=[0,1,2,3,4,5,6,7,8,9]
l=[]
for i in range(len(s)):
    l.append(s[i])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        l.append(arr[i][j])
l=list(set(l))
if(len(l)>10):
    print("false")
else:
    
    p=list(permutations(q,len(l)))
    for i in p:
        z=dict(zip(l,i))
        all_joint="".join(arr)
        suma_arr=0
        for i in all_joint:
            suma_arr+=z[i]
        suma_result=0
        for i in s:
            suma_result+=z[i]
        if(suma_arr==suma_result):
            flag=1
            j=z
            break
    if flag == 1:
        print("YES",j)
    else:
        print("NO")
        

        

