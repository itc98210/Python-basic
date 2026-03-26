for i in range(1,6): #外部迴圈，共執行5次
    print("外部第",i,"次迴圈,內部執行",i,"次迴圈： ",end="")
    for j in range(1,i+1): #內部迴圈
        print("#", end="")
    print()  # 換行