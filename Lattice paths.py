#pascal triangle
a=[1,1]
for i in range (3):
   j=0
   print(a)
   for j in range(j,i+1):
      x=int(a[j])+int(a[j+1])
      k=1
      for k in range (j+1):
      #a.insert(len(a), 1)
       a.insert(j+k+1,x)
       a.pop(j+k+2)








