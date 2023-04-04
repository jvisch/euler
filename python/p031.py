# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

def count(c, i, a):
    if a == 0:
        return 1
    if a < 0:
        return 0
    if i <= 0 and a >= 1:
        return 0
    # count is sum of solutions (i) including S[m-1] (ii) excluding S[m-1]
    return count(c, i - 1, a) + count(c, i, a - c[i - 1])


coinsx = [200, 50, 100, 20, 10, 5, 2, 1]
print(count(coinsx, len(coinsx), 200))
