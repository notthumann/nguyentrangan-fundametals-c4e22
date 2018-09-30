while True:
    pw = input("enter your password: ")

    if not pw.islower() and not pw.isupper() and not pw.isdigit():
        print("ok")
        break
    else:
        print("re-enter")