import random as r

sum = 0
print("你三次擲骰子的點數為", end=" ")
for i in range(0,3):
     num = r.randint(1,6)
     sum += num
     print(str(num), end=" ")
print("，總點數為：" + str(sum)) 