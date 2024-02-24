import datetime
x = datetime.date.today()
print("Today:", x)
y= x - datetime.timedelta(1)
print("Yesterday:", y)
z = x + datetime.timedelta(1)
print("Tomorrow:", z)