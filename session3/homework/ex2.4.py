sizes = [5 , 7 , 10, 22, 24 , 50 , 75]
print("Hi I am not human being and these are my sheep sizes: ")
l = len(sizes)
print(sizes)
biggest = max(sizes)
print("Now my biggest sheep has size", biggest, "let's shear it.") 
pos = 0
for _ in range(l):
    if biggest != sizes[pos]:
        pos +=1
    else:
        sizes[pos] = 8
print("After shearing, here is my flock")
print(sizes)
pos = 0     #reset the position
for _ in range(l): 
    sizes[pos]=sizes[pos]+50
    pos+=1
print("One month has passed, now here is my flock")
print(sizes)