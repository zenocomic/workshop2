  
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
model = thisdict["color"] = "red"
print(thisdict)

#Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
model = thisdict.update({"color": "red"})
print("model:", model)

#Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}