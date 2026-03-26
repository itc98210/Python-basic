dict1 = {"電視":15000, "冰箱":23000, "冷氣":28000}
name = input("輸入電器名稱:")
if name in dict1:  
    print(name + "的價格為 " + str(dict1[name]))
else:  
    price = input("輸入電器價格：")
    dict1[name] = price
    print("字典內容：" + str(dict1))