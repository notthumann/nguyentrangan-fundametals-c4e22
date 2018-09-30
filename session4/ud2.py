person = {
    'name' : 'An',
    'age' : 22,
    'gender' : 'male',
}
print(person)
do = input("do you want to delete or update?(D/U) ")
if do == "D":
    delete = input('what to delete?')
    if delete not in person:
        print("notfound")
    else:
        del person[delete]
    print(person)
elif do == "U":
    key = input("what key to update?")
    value = input("What value?")
    person[key]= value
    print(person)
else:
    print("What?")
    