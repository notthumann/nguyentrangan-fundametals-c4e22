quiz = {
    'stimulus':['Answer the following algebra question:','Estimate the answer (exact calculation not needed)'],
    'stem':['If x = 8, then what is the value of 4(x + 3) ?','Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is this mean ?'],
    'answer': [[35,36, 40, 44],['About 55','About 65', 'About 75', 'About 85']],
    'rightchoice': [4,2]
}
count = 0
for i in range (2):
    print(quiz['stimulus'][i])
    print(quiz['stem'][i])
    for n in range (4):
        print( n+1 , '.' ,' ', quiz['answer'][i][n], sep='')
    while True:
        answer = input('Your choice: ')
        if answer.isdigit() == False:   #handle the exception
            print('Answer not found')
        elif int(answer) not in range(1,5):   #handle the exception
            print('Answer not found')
        else:
            if int(answer) == quiz['rightchoice'][i]:
                print('Bingo')
                if int(answer) == quiz['rightchoice'][i]:
                    count+=1
                break
            else:
                print(':(')
                break
    
print('You correctly answer', count,'out of 2 questions')
