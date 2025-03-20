n=int(input("Number: "))
if n<0:print("No negatives!")
else:
 b=""
 while n>0:
  b=str(n%2)+b
  n//=2
 print(b or 0)