dict1 = {"水瓶座":"活潑善變", "雙魚座":"迷人保守", "白羊座":"天生勇者", "金牛座":"熱情敏感"}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的性格特癥為 %s" % (listkey[i], listvalue[i]))