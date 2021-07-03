#asssignment -4 to check wheather the number is prime or not:
n=int(input("enter the number- "))
count=0

for i in range(2,n):

 if (n%i)==0:
   count=count+1
   break
    
 else:
   count=0

if (count==0):
  print("prime")
else:
  print("not prime")