# 约瑟夫问题
def queue(count,num,outList):
    numList = []
    for i in range(count):
        numList.append(i+1)

    while len(numList)>=num:
        # print("初始列表:", numList)
        numLen = len(numList)
        zcNum = numLen // num
        ysNum = numLen % num
        delCount = 0
        for i in range(zcNum):
            delIndex = ((i+1)*num-delCount-1)
            outList.append(numList[delIndex])
            del numList[delIndex]
            delCount += 1
            if i == zcNum-1:
                # print("执行列表:", numList)
                for x in range(ysNum)[::-1]:
                    addIndex = delIndex+ysNum-1
                    addNum = numList[addIndex]
                    del numList[addIndex]
                    numList.insert(0,addNum)

    if len(numList)<num and len(numList)>1:
        queue3(numList, num, outList)

    return numList[0]


def queue3(numList,num,outList):
    while len(numList)>1:
        for i in range(num):
            n=numList[0]
            del numList[0]
            if i==num-1:
                outList.append(n)
            else:
                numList.append(n)
    return numList[0]

def queue2(count,num,outList):
    numList = []
    for i in range(count):
        numList.append(i+1)
    while len(numList)>1:
        for i in range(num):
            n=numList[0]
            del numList[0]
            if i==num-1:
                outList.append(n)
            else:
                numList.append(n)
    return numList[0]

outList=[]
rstNum = queue(300000,30,outList)
print("[1]最后的胜利者编号是：",rstNum)
# print("[1]淘汰顺序：",outList)
# outList.clear()
# rstNum = queue2(30000,30,outList)
# print("[2]最后的胜利者编号是：",rstNum)
# print("[2]淘汰顺序：",outList)
