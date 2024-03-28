# 1 
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

row = 5
col = 5

for r in range(1,6):
    for j in range(r,r+r):
        print(j,end=' ')
    print()