n = int(input("Enter n: ")) #number of stars in one row
m = int(input("Enter m: ")) #number of rows
stars = ("*")
for _ in range (m):    
    for _ in range (n):
        print (stars,end="")
        print (" ",end="")
    print("")