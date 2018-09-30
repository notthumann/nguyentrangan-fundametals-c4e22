while True:
    n = input("enter your password: ")
    l = len(n)
    if l < 8:
        print("not long enough")
    elif n.isdigit():
        print("must not contain only digits")
    elif n.isupper():
        print("must not contain only uppercase letter")
    elif n.islower():
        print("must not contain only lowercase letter")
    else:
        print("ok")
        break