
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

#Output: {'brand': 'Ford', 'year': 1964}

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)

#Output: {'brand': 'Ford', 'model': 'Mustang'} 

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

#Output: {'brand': 'Ford', 'year': 1964}

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)

#Output: {}