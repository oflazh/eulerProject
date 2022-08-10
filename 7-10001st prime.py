import math
lower = 2
upper = 144
c=0
for num in range(lower, upper + 1):

   if num > 1:
       for i in range(int(math.sqrt(num)), int(num/2)):
           if (num % i) == 0:
               break
       else:
           c+=1
           print(c, num, (math.sqrt(num)))
