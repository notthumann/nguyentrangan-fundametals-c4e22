text  = input('Enter the data: ')
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in (alphabet):
    if (text.lower().count(i)) > 0:
        print(i,'\t', text.lower().count(i))

