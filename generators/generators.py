import random
import itertools as it
#1) Írj egy Python generátor kifejezést (generator expression) ami kiszámítja a köbét minden páros számnak az alábbi listából [10,3,7,9,11,33,22,8,2]. Használd a `list` függvényt, hogy az eredményeket egy listában tudd prezentálni. 

b_list = [10,3,7,9,11,33,22,8,2]

def mod(x):
   
    if (x % 2 == 0):
        return (x**3)

result = map(mod, b_list)
#print(list(result))


re = (x ** 3  for x in b_list if x % 2 == 0)
#print(list(re))

#2) Készítsünk Python generátor piplinet, azaz ágyazzunk egymásba több generátor kifejezéséseket.

#a) Írj egy python generátor kifejezést ami a `random.randint` függvény segítségével generál legfeljebb 100 random számot 1 es 1000 között.
#b) Írj egy másik kifejezést ami négyzetre négyzetre emeli a számokat
#c) Írj egy harmadik kijezést ami stringge konvertálja az értékeket
#d) Ellenőrzés képpen irasd ki az összes egyedi stringet amit kaptunk. (Hasznos lehet a `set` halmaz adatszerkezet)

#print(random.randint(1, 1000))

ra = (random.randint(1, 1000) for _ in range(100)  )
#print (list(ra))

ra_2 = (x ** 2 for x in ra)
#print (list(ra_2))

ra_3 = (str(x) for x in ra_2 )
#print (list(set(ra_3)))

def unique(iterable):
    for i in set(iterable):
            yield i

u = unique([1, 'Tamas',2,1,5,32,2,1, 'Valaki', 33.3, 33.3, 33.3])

print(next(u))
print(next(u))
print(next(u))
print(next(u))
print(next(u))
print(next(u))
print(next(u))
print(next(u))