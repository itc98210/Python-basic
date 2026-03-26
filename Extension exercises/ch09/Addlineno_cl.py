file = "file2_cl.txt"
with open(file,'r') as f:
    content=f.read()
    print("共有",len(content),"個字元") 