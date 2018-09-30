fav_item = ["film","code","game"]
print(fav_item)
new_fav_item = input("do you like anything else ?")
fav_item.append(new_fav_item)
print(fav_item)
new_fav_item2 = input("anything else ? ")
fav_item.insert(0, new_fav_item2)
print(fav_item)