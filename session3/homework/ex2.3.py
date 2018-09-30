sizes = [ 7 , 10, 80, 24 , 50 , 75]
print("Hi I am not human being and these are my sheep sizes: ")
print(sizes)
l = len(sizes)
biggest = max(sizes)    
print("Now my biggest sheep has size", biggest, "let's shear it.") 

pos = 0
for _ in range(l):
    if biggest != sizes[pos]:   #find the position of the greatest number in the list
        pos +=1
    else:
        sizes[pos] = 8
print("After shearing, here is my flock")
print(sizes)
