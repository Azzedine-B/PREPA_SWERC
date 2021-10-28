# Objet : [Price, Weigth]

# [N objet]

# Personne : Max weigth, [ Nmax objet]

# [N personnes]

def SuperSale(weigth, listObject):
    if weigth < 0 :
        return 0
    if  len(listObject) == 0:
        return 0
    if weigth >= listObject[-1]["weigth"]:
        return max(listObject[-1]["price"] + SuperSale(weigth - listObject[-1]["weigth"], listObject[:-1]), SuperSale(weigth, listObject[:-1]))
    else :
        return SuperSale(weigth, listObject[:-1])

def groupPrice(group,listObject):
    summ = 0
    for i in range(len(group)) :
        summ += SuperSale(group[i]["weigth"], listObject)

    return summ


nbTest = int(input())
res = []
for i in range(nbTest):
    nbObject = int(input())
    listObject = []
    for i in range(nbObject):
        price, weigth = input().split(" ")
        obj = {'price': int(price), "weigth" : int(weigth)}
        listObject.append(obj)

    groupSize = int(input())
    group = []
    for i in range(groupSize):
        weigth = int(input())
        obj = {'weigth': weigth}
        group.append(obj)

    res.append(groupPrice(group, listObject))

for i in range(len(res)):
    print(res[i])