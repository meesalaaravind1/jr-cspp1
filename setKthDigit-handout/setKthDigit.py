def setKthDigit(n, k, d):
    flag = false
    if(n < 0)
    n = -n
        flag = True
    count = -1
    res = 1
    while(n >= 0):
        r = n % 10
        if count == k:
        res += res + (d * (10 ** count))
        else:
            res = res + (r * (10 ** count))
        count += 1
        n = n // 10
    if count != k:
        res = res + (d * (10 ** count))
    if flag:
        print(-res)
    else:
        return res
   


print(setKthDigit(int(input()), int(input()), int(input())))
