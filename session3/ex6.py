item=["item1","item2","item3","item4"]
print(item)
n = input ("what do you want to delete?")
if n.isdigit():
    item.pop(int(n-1))
else:
    item.remove(n)
print(item)