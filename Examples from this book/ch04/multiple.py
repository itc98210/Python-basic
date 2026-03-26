a = int(input("請輸入 a 的值："))
b = int(input("請輸入 b 的值："))
maxno = a * b
for i in range(1, maxno + 1):
    if(i % a == 0 and i % b == 0):
        break
print("%d 和 %d 的最小公倍數=%d"  % (a, b, i))  