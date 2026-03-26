num=[67,12,9,52,91,3]

while True:     
    no = input("請輸入中獎者的編號(Enter結束)：")
    if (no==""):
        break
 
    IsFound=False
    for i in range(len(num)):   #逐一比對搜尋 
        if (num[i]==int(no)):   #號碼相符 
            IsFound=True        #設旗標為 True
            break               #結束比對

    if (IsFound==True):
        print("恭喜您，號碼",no,"中獎了!")
    else:
        print("號碼",no,"未中獎！")    