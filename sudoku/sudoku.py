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
init(arr, hp_arr, sp_arr)
print(hp_arr)
