item = ['no1','no2','no3','no4']
print (*item, sep="\n")
while True:
    i = int(input("what number do you want to see?"))
    if i <= -4:
        print("re_enter")
    elif i > 3:
        print ("re_enter")
    else:
        print(item[i])
        break
