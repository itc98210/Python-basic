num=[67,12,9,52,91,3]

while True:     
    no = input("請輸入中獎者的編號(Enter結束)：")
    if (no==""):
        break
    
    n=len(num)-1 # 串列長度-1
    IsFound=False
    min=0
    max=n
    no=int(no)
    
    for i in range(0,n): 
        for j in range(0,n-i):         
            if (num[j]>num[j+1]): # 由小到大排序
                num[j],num[j+1]=num[j+1],num[j]     # 兩數互換     
   
    while(min<=max):
        mid=int((min+max)/2)
        if (num[mid]==no):  #號碼相符 
            IsFound=True
            break
    
        if (num[mid]>no): #如果中間值大於輸入值 
           max=mid-1      #使用較小的一半區域繼續比對 
        else:             #如果中間值不大於輸入值 
           min=mid+1      #使用較大的一半區域繼續比對 
           
    if (IsFound==True):
        print("恭喜您，號碼",no,"中獎了!")
    else:
        print("號碼",no,"未中獎！")               