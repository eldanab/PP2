#Ex.1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Ex.2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car["year"])
#Ex.3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car.items())
#Ex.4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car.keys())
#Ex.5

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car.items())