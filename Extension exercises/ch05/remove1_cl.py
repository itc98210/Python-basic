colors = ["紅","橙","黃","綠","藍"]
while True:
    print("顏色有：",colors)
    color = input("請輸入要刪除的顏色(Enter 結束)：")
    if (color==""):
        break
    n = colors.count(color) 
    if (n>0):  # 串列元素存在
        colors.remove(color)
    else:
        print(color,"不在串列中!")