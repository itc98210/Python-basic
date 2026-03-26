import random as r

list1 = r.sample(range(0,10), 4)
list1.sort()
print("本期四星彩中獎號碼為：", end="")
for i in range(0,4):
    if i == 3:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")
