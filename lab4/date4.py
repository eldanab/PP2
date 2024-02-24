import datetime
d1 = input("Input data in the format of DD-MM-YYYY HH:MM:SS: ")
date1 = datetime.datetime.strptime(d1, '%d-%m-%Y %H:%M:%S')
d2 = input("Input data in the format of DD-MM-YYYY HH:MM:SS: ")
date2 = datetime.datetime.strptime(d2, '%d-%m-%Y %H:%M:%S')
dd = date2 - date1
dt = dd.days * 24 * 60 * 60 + dd.seconds
print(dt)
