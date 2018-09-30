quiz = {
    'stimulus':'Answer the following algebra question:',
    'stem':'If x = 8, then what is the value of 4(x + 3) ?',
    'answer': [35,36, 40, 44],
    'rightchoice': 4
}
print(quiz['stimulus'])
print(quiz['stem'])
for i in range (4):
    print( i+1 , '.' ,' ', quiz['answer'][i], sep='')
while True:
    answer = input('Your choice: ')
    
    if answer.isdigit() == False:
        print('Answer not found')
    elif int(answer) not in range(1,5):
        print('Answer not found')
    else:
        if int(answer) == quiz['rightchoice']:
            print('Bingo')
            break
        else:
            print(':(')
            break


