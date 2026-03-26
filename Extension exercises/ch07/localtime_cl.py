import time as t

time1 = t.localtime()
show = "今天是今年的第 " + str(time1.tm_yday) + " 天，屬於"
if time1.tm_yday < 184 : show += "上半年。"
else :  show += "下半年。"
print(show)