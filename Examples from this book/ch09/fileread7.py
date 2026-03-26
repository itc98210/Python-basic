f=open('file2.txt','r')
print(f.readline())  # 123中文字\n
print(f.readline())  # abcde\n
print(f.readline(1)) # h
print(f.readline(3)) # ell
f.close()