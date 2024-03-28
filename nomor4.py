# 1 3 5 7 9
# 2 4 6 8 10
# 3 5 7 9 11
# 4 6 8 10 12
# 5 7 9 11 13

row = 5
col = 5

for r in range (1, row +1):
    k = r
    for j in range (col):
        print (r, end=' ')
        r += 2 
    print()