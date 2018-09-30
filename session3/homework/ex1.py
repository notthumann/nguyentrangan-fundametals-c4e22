clothes = ["T-shirt","Sweater","Hoodie","Jacket"]
l = len(clothes)
while True:
    c = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if c == "R" :               #read
        print ("Our items:",*clothes, sep = " ")
    
    elif c == "C" :             #creat
        while True:
            new_item = input("Enter new item: ")
            if new_item.isdigit():  #handle exception
                print("must not be a number")
            elif new_item.isupper():
                print("must not contain only uppercase letter")
            elif new_item.islower():
                print("must not contain only lowercase letter")
            else:
                clothes.append(new_item)
                break
        print ("Our items:",*clothes, sep = " ")
    
    elif c == "U" : #update
        while True:
            pos = int(input("Update position? "))
            if pos > (l):   #handle exception
                print("Position not found")
            else:
                break
        while True:
            new_item = input("New item: ") 
            if new_item.isdigit(): #handle exception
                print("must not be a number")
            elif new_item.isupper():
                print("must not contain only uppercase letter")
            elif new_item.islower():
                print("must not contain only lowercase letter")
            else:
                clothes[pos-1] = new_item
                break
        print ("Our items:",*clothes, sep = " ")
    
    elif c == "D" : #delete
        while True:
            pos = int(input("Delete position? "))
            if pos > (l): #handle exception
                print("Position not found") 
            else:
                break
        clothes.pop(pos-1)
        print ("Our items:",*clothes, sep = " ")
