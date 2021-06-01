a=int(input("enter :"))
arr=map(int,input("Enter :").split()) 
j=0
for i in arr:
     while(i>j):
         if(i>1):
             i=i+1
             i=i//2
             print(i%2,end=' ')
         j=j+1
