quiz = {
    'stimulus':'today blem blem blem.',
    'stem':'who is not human?',
    'choices':['1.me','2.not me', '3.someoneelse'],
}
print(quiz['stimulus'])
print(quiz['stem'])
print(*quiz['choices'])

a = int(input("Your answer is : "))
while True:
    if a in (1,4):    
        if a == 1:
            print("true, true, true.")
            break
        else:
            print("false")
            break
    else:
        print("Your answer not found.")
        break
