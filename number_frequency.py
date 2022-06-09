a=input("enter the limit")
k={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(0,len(a)):
    if a[i].isdigit()==True:
        t=int(a[i])
        k[t]=k[t]+1   
for i in range(0,10):
    print(k[i] ,end=" ")