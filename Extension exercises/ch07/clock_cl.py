import time as t

timestart = t.perf_counter()
for i in range (0,1000):
    for j in range (0,1000):
        n = float(i) * float(j)
timeend = t.perf_counter()
print("執行一百萬次浮點數運算的時間：" + str(timeend-timestart) + " 秒")