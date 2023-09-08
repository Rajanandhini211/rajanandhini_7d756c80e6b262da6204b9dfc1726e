def factrec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factrec(n-1)
  
number=int(input("enter a number:")) 
res=factrec(number)

print ("the factorial of {} is {}.".format(number,res))