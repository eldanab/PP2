import random
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Ex.1
dict1 = random.choice(movies)
print(dict1)
if dict1["imdb"] > 5.5:
    print(True)
else:
    print(False)
print()

#Ex.2
sublist = []
for i in movies:
    if i["imdb"] > 5.5:
        sublist.append(i["name"])
print(sublist)
print()

#Ex.3
categories = []
for i in movies:
    categories.append(i["category"])
def cat(mov):
    c = random.choice(categories)
    print(c)
    m = []
    for i in mov:
        if i["category"] == c:
            m.append(i["name"])
    print(m)
cat(movies)
print()

#Ex.4
movies2 = random.sample(movies, random.randint(1, len(movies)))
sum = 0
for i in movies2:
    sum += i["imdb"]
av = sum / len(movies2)
print(av)
print()

#Ex.5
a = random.choice(categories)
print(a)
sum = 0 
len = 0
for i in movies:
    if i["category"] == a:
        len += 1
        sum += i["imdb"]
print(sum/len)