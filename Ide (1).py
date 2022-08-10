# shoping cost (list) problem....
n=int(input())
while(n!=0):
  x=input().split()
  p=int(x[0])
  q=int(x[1])
  if(p>100):
    print(float((p*q)-(p*q)/5))
  print(float(p*q))  
  n=n-1  
#shoping cost 
n=int(input())
while(n!=0):
  x=input().split()
  p=int(x[0])
  q=int(x[1])
  if(p>100):
    print(float((p*q)-(p*q)/5))
  else:  
    print(float(p*q))  
  n=n-1  
