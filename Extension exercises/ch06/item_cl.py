dict1 = {"水瓶座":"活潑善變", "雙魚座":"迷人保守", "白羊座":"天生勇者", "金牛座":"熱情敏感"}
item1 = dict1.items()
for name, nature in item1:
    print("%s 的性格特癥為 %s" % (name, nature))