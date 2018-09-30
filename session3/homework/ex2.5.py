sizes = [5 , 7 , 300, 90, 24 , 50 , 400]
print("Hi I am not human being and these are my sheep sizes: ")
print(sizes)
l = len(sizes)
nom = int (input("enter the number of months have passed:"))
for i in range(nom):
    print("Month",i +1 )
    pos = 0
    for _ in range(l):
        sizes[pos]=sizes[pos]+50
        pos+=1
    print("One month has passed, now here is my flock")
    print(sizes)
    biggest = max (sizes)
    print("Now my biggest sheep has size", biggest, "let's shear it.") 
    pos = 0
    for _ in range(l):
        if biggest != sizes[pos]:
            pos +=1
        else:
            sizes[pos] = 8
    print("After shearing, here is my flock")
    print(sizes)