# 约瑟夫问题

# 优化算法后的想法
def queue(count, num, outList):
    # 循环次数
    loopCount_1, loopCount_2, loopCount_3 = 0, 0, 0

    numList = []
    for i in range(count):
        numList.append(i + 1)

    while len(numList) >= num:
        loopCount_1 += 1
        numLen = len(numList)
        # 整除数
        zcNum = numLen // num
        # 余数
        delCount = 0
        for i in range(zcNum):
            loopCount_2 += 1
            delIndex = ((i + 1) * num - delCount - 1)
            outList.append(numList[delIndex])
            del numList[delIndex]
            delCount += 1
            if i == zcNum - 1:
                numList = listRecombination(numList, delIndex)

    while num > len(numList) > 1:
        loopCount_3 += 1
        numLen = len(numList)
        ysNum = num % numLen
        # 如果余数为0 则移除数组最后一个对象
        if ysNum == 0:
            outList.append(numList[numLen - 1])
            del numList[numLen - 1]
        else:
            # ysNum-1 是要移除对象 index
            outList.append(numList[ysNum - 1])
            # 将 ysNum-1 前的数组移至数组后面 此时得到的数组第一个则是需要移除的对象
            numList = listRecombination(numList, ysNum - 1)
            # 移除第一个对象
            del numList[0]
    print("总循环次数:", loopCount_1 + loopCount_2 + loopCount_3)
    return numList[0]


# 数组重组
# 按照数据中具体的节点（index） 将列表中index的数组（不包括index对象）追加到列表末端。
def listRecombination(list, index):
    list += list[0:index]
    del list[0:index]
    return list


# 原始想法
def queue2(count, num, outList):
    # 循环次数
    loopCount_1, loopCount_2 = 0, 0

    numList = []
    for i in range(count):
        numList.append(i + 1)
    while len(numList) > 1:
        loopCount_1 += 1
        for i in range(num):
            loopCount_2 += 1
            n = numList[0]
            del numList[0]
            if i == num - 1:
                outList.append(n)
            else:
                numList.append(n)
    print("总循环次数:", loopCount_1 + loopCount_2)
    return numList[0]


# 数学公式解
def queue3(n, m):
    loopCount_1 = 0
    s = 0
    for i in range(2, n + 1):
        s = (s + m) % i
        loopCount_1 += 1
    print("总循环次数:", loopCount_1)
    return s+1

# outList = []
# rstNum = queue(100000, 3, outList)
# print("[1]最后的胜利者编号是：", rstNum)
# print("[1]淘汰顺序：",outList)
# outList.clear()
# rstNum = queue2(100, 88, outList)
# print("[2]最后的胜利者编号是：", rstNum)
# # print("[2]淘汰顺序：",outList)

rstNum = queue3(100000,3)
print("[3]最后的胜利者编号是：", rstNum)
