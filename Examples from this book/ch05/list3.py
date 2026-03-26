subjects=["國文","數學","英文"]
scores = [85, 79, 93]
for i in range(len(scores)): # 即 for i in range(3):
    print("%s成績：%d 分" % (subjects[i],scores[i]))