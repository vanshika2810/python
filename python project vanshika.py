import random
n=int(input("no. of characters: "))
c=""
l=["$","#","@","_","%"]
if n>=12:
    d=random.randint(0,len(l)-1)
    c+=l[d]
    for i in range(0,(n-4)//2):
            c+=chr(random.randint(65,90))
    for i in range((n-4)//2,n-4):
        c+=chr(random.randint(97,112))
    for i in range(0,3):
        c+=str(random.randint(0,10))
    print(c)
else:
    print("password can't be that short")
    
    
    
    
      
