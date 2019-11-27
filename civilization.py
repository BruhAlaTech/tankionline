from random import randint

mapz = []
h=int(input())
w = int(input())
for i in range(h):
    mapz.append([])
    for j in range(w):
        mapz[i].append(randint(0,1))

for i in range(h):
    print(mapz[i])
