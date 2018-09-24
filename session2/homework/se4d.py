n = int(input("Enter a number: "))
stars = ("*")
if n % 2 == 0 :
    for _ in range (int(n/2)):
        print ("x",end="")
        print (" ",end="")
        print (stars,end="")
        print (" ",end="")
else :
    for _ in range (int(n/2)):
        print ("x",end="")
        print (" ",end="")
        print (stars,end="")
        print (" ",end="")
    print ("x")  