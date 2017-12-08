# 数独求解
# 横排 1-9
# 竖排 1-9
# 九个小九宫格 1-9


# 横排检查
def hpCheck():
    return True


# 竖排检查
def spCheck():
    return True


# 小九宫格检查
def jggCheck():
    return True


def init(begin_arr, hp_arr, sp_arr, gg_arr):
    for y in range(9):
        arr_hp = []
        arr_sp = []
        arr_gg = []
        for x in range(9):
            arr_hp.append(begin_arr[x + y * 9])
            arr_sp.append(begin_arr[y + x * 9])
        hp_arr.append(arr_hp)
        sp_arr.append(arr_sp)


# 根据数组中某个位置ID返回和这个位置组成的横排的9个数
def getHP(idx, all_arr):
    for i in range(9):
        n = (idx // 9) * 9 + i
        hp_arr.append(all_arr[n])
    print(hp_arr)


# 根据数组中某个位置ID返回和这个位置组成的竖排的9个数
def getSP(idx, all_arr):
    for i in range(9):
        n = i * 9 + idx % 9
        sp_arr.append(all_arr[n])
    print(sp_arr)


# 根据数组中某个位置ID返回和这个位置组成的九宫格的9个数
def getGG(idx, all_arr):
    n = ((idx//9)%3)*3+idx%3
    return n


arr = [1, 0, 0, 0, 0, 0, 0, 0, 0,
       3, 2, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 3, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 4, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 5, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 6, 0, 1, 0,
       0, 0, 0, 0, 0, 0, 7, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 8, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 9, ]

hp_arr = []
sp_arr = []
gg_arr = []
# init(arr, hp_arr, sp_arr, gg_arr)
getHP(9, arr)
getSP(17, arr)
# print(hp_arr)
