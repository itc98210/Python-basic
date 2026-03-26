time1 = "10:23:41"
time1 = time1.replace(":", " 點 ", 1)
time1 = time1.replace(":", " 分 ", 1)
time1 += " 秒"
print(time1)