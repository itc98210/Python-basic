filename = input("請輸入圖片檔案名稱：")
if filename.endswith(".jpg") or filename.endswith(".JPG"):
    print("圖片格式是 JPG！")
else:
    print("圖片格式不是 JPG！")