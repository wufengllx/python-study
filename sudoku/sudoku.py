# 数独求解
# 横排 1-9
# 竖排 1-9
# 九个小九宫格 1-9
import sys
import time

sys.setrecursionlimit(10000)  # 递归深度值：这里设置为一百万
action_count = 0  # 递归次数


# 根据数组中某个位置ID返回和这个位置组成的横排的9个数
def get_hp_arr(idx, all_arr):
    num_arr = []
    for i in range(9):
        n = (idx // 9) * 9 + i
        num_arr.append(all_arr[n])
    return num_arr


# 根据数组中某个位置ID返回和这个位置组成的竖排的9个数
def get_sp_arr(idx, all_arr):
    num_arr = []
    for i in range(9):
        n = i * 9 + idx % 9
        num_arr.append(all_arr[n])
    return num_arr


# 根据数组中某个位置ID返回和这个位置组成的九宫格的9个数
def get_gg_arr(idx, all_arr):
    num_arr = []
    m = ((idx // 9) % 3) * 3 + idx % 3
    for i in range(9):
        n = idx + (i // 3) * 9 - (m // 3) * 9 + i % 3 - m % 3
        num_arr.append(all_arr[n])
    return num_arr


# 寻找最优方案
# 循环整体数组里面没一个空白格，找出空白格可填入的数，如果只能唯一填入，则直接填入，并归并到整体数组里面
# 规则：填入的数是（横、竖、九宫格）三个数组里面不存在的数
def find_optimal(all_arr):
    min_null_num = 999
    optimal_idx = 0
    num_arr_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    optimal_diff_arr = []  # 最优解数组
    # union_arr = []
    null_flag = False  # 是否存在未填空白
    for i in range(len(all_arr)):
        if all_arr[i] == 0:
            null_flag = True
            # 横排
            hp_arr = get_hp_arr(i, all_arr)

            # 竖排
            sp_arr = get_sp_arr(i, all_arr)

            # 九宫格
            gg_arr = get_gg_arr(i, all_arr)

            # 并集
            union_arr = set(hp_arr).union(sp_arr).union(gg_arr)
            # 差集
            difference_arr = set(num_arr_nine).difference(union_arr)

            diff_arr_len = len(difference_arr)

            if 0 < diff_arr_len <= min_null_num:
                optimal_idx = i
                min_null_num = diff_arr_len
                optimal_diff_arr = list(difference_arr)
                if diff_arr_len == 1:
                    # all_arr[i] = list(difference_arr)[0]
                    # return find_optimal()
                    return {"optimal_idx": optimal_idx, "min_null_num": min_null_num,
                            "union_arr": union_arr, "optimal_diff_arr": optimal_diff_arr, "null_flag": null_flag}

    return {"optimal_idx": optimal_idx, "min_null_num": min_null_num, "optimal_diff_arr": optimal_diff_arr, "null_flag": null_flag}


# 执行最优解
def action_optimal(optimal_map):
    global action_count
    action_count += 1
    optimal_diff_arr = optimal_map["optimal_diff_arr"]
    optimal_idx = optimal_map["optimal_idx"]
    null_flag = optimal_map["null_flag"]
    all_arr = optimal_map["all_arr"]
    min_null_num = optimal_map["min_null_num"]
    up_optimal_map = optimal_map["up_optimal_map"]
    # 无空白就结束了
    if not null_flag:
        # print("=== ", optimal_map)
        view_arr(all_arr)
        return True
    elif 9 > min_null_num > 0 and len(optimal_diff_arr) > 0:
        copy_arr = all_arr.copy()
        copy_arr[optimal_idx] = optimal_diff_arr[0]
        optimal_diff_arr.remove(optimal_diff_arr[0])
        optimal_map["optimal_diff_arr"] = optimal_diff_arr
        next_map = find_optimal(copy_arr)
        next_map["up_optimal_map"] = optimal_map
        next_map["all_arr"] = copy_arr
        return action_optimal(next_map)
    elif len(optimal_diff_arr) == 0 and len(up_optimal_map) > 0:
        return action_optimal(up_optimal_map)
    # elif len(up_optimal_map) == 0:
    else:
        return False


def view_arr(all_arr):
    print_arr = []
    for i in range(len(all_arr)):
        print_arr.append(all_arr[i])
        if (i + 1) % 9 == 0:
            print(print_arr)
            print_arr.clear()


def games(all_arr):
    start = time.clock()
    # flag = True
    # while flag:
    optimal_map = find_optimal(all_arr)
    optimal_map["all_arr"] = all_arr
    optimal_map["up_optimal_map"] = {}
    flag = action_optimal(optimal_map)

    end = time.clock()
    print("是否成功获得解：", flag and "成功" or "失败", ", 用时：%f s" % (end - start), ", 递归次数:", action_count)


# 简单
# arr = [5, 0, 0, 7, 0, 6, 4, 0, 0,
#        7, 9, 6, 8, 2, 0, 0, 0, 0,
#        1, 0, 0, 0, 9, 0, 7, 0, 0,
#        0, 4, 8, 0, 0, 7, 0, 0, 0,
#        9, 0, 0, 0, 0, 0, 0, 0, 6,
#        0, 0, 0, 2, 0, 0, 9, 5, 0,
#        0, 0, 7, 0, 8, 0, 0, 0, 5,
#        0, 0, 0, 0, 4, 2, 6, 1, 7,
#        0, 0, 3, 6, 0, 5, 0, 0, 9, ]

# 困难
arr = [0, 2, 5, 0, 0, 0, 0, 4, 0,
       8, 0, 0, 0, 0, 9, 0, 0, 5,
       0, 0, 0, 0, 0, 4, 0, 0, 3,
       0, 6, 8, 0, 5, 0, 0, 0, 0,
       0, 0, 0, 1, 0, 3, 0, 0, 0,
       0, 0, 0, 0, 4, 0, 5, 1, 0,
       6, 0, 0, 4, 0, 0, 0, 0, 0,
       9, 0, 0, 7, 0, 0, 0, 0, 4,
       0, 4, 0, 0, 0, 0, 6, 8, 0, ]

games(arr)
