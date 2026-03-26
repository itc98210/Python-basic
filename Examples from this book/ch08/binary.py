num=[256,731,943,389,142,645,829,945,371,418]
name=["林小虎","王中森","邵木淼","李大同","陳子孔","鄭美麗","曾溫柔","錢來多","賈天良","吳水品"] 

n=len(num)-1 # 串列長度-1
IsFound=False
min=0
max=n
c=0 #計算比對次數 

for i in range(0,n): 
    for j in range(0,n-i):         
        if (num[j]>num[j+1]): # 由小到大排序
            num[j],num[j+1]=num[j+1],num[j]     # 兩數互換
            name[j],name[j+1]=name[j+1],name[j] # 姓名互換
 
no = int(input("請輸入中獎者的編號："))

while(min<=max):
    mid=int((min+max)/2)
    c+=1  #比對次數加 1
    if (num[mid]==no):  #號碼相符 
        IsFound=True
        break

    if (num[mid]>no):  #如果中間值大於輸入值 
       max=mid-1      #使用較小的一半區域繼續比對 
    else:             #如果中間值不大於輸入值 
       min=mid+1      #使用較大的一半區域繼續比對 
       
if (IsFound==True):
    print("中獎者的姓名為：",name[mid])
else:
    print("無此中獎號碼！")
print("共比對 ", c ," 次")              