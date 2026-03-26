innum = 0
list1 = []
for i in range(0,4):
    innum = int(input("請輸入第 " + str(i+1) + " 個月的支出金額："))
    list1.append(innum)
print("支出最多的金額為：%d" % max(list1))
print("支出最少的金額為：%d" % min(list1))
print("支出的總額為：%d" % sum(list1))
print("支出金額由小到大排序為：{}".format(sorted(list1)))