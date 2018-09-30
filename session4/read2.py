movie = {
    'name': 'Pulp Fiction',
    'year':'1994'
}
while True:
    key = input ("Key?")
    if key in movie: #try except
        break
    else:
        print("notfound")
print(movie[key])