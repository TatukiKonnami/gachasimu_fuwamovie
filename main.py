import numpy as np

"""天井"""
count_max = 90
count = 0


def turn_rare():
    """単発ガチャを回す"""
    global count_max
    global count
    result = []

    weight = [0.943, 0.051, 0.006]
    count= count+1
    result.append(pickup_rare(weight))
    return result

def turn_10rare():
    """10 連ガチャを回す"""
    global count_max
    global count
    isRera = False
    result = []

    weight = [0.943, 0.051, 0.006]
    # 9 回抽選する
    for v in range(0, 9):
        count= count+1
        v = pickup_rare(weight)
        if v != "★3":
            isRera = True
        result.append(v)
    #  1 回は必ず 星4以上 が当選する
    count= count+1
    if isRera:
        result.append(pickup_rare(weight))
    else:
        result.append(pickup_rare_last())
    return result

def pickup_rare(weight):
    global count_max
    global count
    rarities = ["★3", "★4", "★5"]
    picked_rarity = np.random.choice(rarities, p=weight)

    if count >= count_max:
        picked_rarity ="★5"

    if picked_rarity == "★5":
        count = 0

    return picked_rarity

def pickup_rare_last():
    global count_max
    global count
    weight = [0.994,0.006]
    rarities = [ "★4", "★5"]
    picked_rarity = np.random.choice(rarities, p=weight)

    if count >= count_max:
        picked_rarity ="★5"

    if picked_rarity == "★5":
        count = 0

    return picked_rarity






charenge = 4200
three = 0
four = 0
five = 0
i = 0
while i < charenge:
    res = turn_rare()
    for r in res:
        if r =="★3":
            three += 1
        elif r =="★4":
            four+=1
        else:
            five += 1
    i+=1

print("★3:{}".format(three))
print("★4:{}".format(four))
print("★5:{}".format(five))



        



