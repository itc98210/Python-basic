def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=[3,5,2,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):      
        print("i=%d j=%d" %(i,j))
        if (datas[j]>datas[j+1]): # 由大到小排序
            print("%d,%d 互換後" %(datas[j],datas[j+1]) ,end="：")
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換
        print(datas)

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 