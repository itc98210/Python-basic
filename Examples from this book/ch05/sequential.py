num=[256,731,943,389,142,645,829,945]
name=["林小虎","王中森","邵木淼","李大同","陳子孔","鄭美麗","曾溫柔","錢來多"]
no = int(input("請輸入中獎者的編號："))
 
Isfound=False
for i in range(len(name)):  #逐一比對搜尋 
    if (num[i]==no):        #號碼相符 
        Isfound=True        #設旗標為 True
        break               #結束比對

if (Isfound==True):
    print("中獎者的姓名為：",name[i])
else:
    print("無此中獎號碼！")
print("共比對 %d次 " %(i+1))        