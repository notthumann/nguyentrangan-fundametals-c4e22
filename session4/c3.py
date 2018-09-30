pokemon = {
    'name':'pikachu'
    
}
text = input("Enter new item: ")
pair = text.split(",")
key, value = pair

#key = pair[0]
#value = pair [1]

pokemon[key] = value
print(pokemon)