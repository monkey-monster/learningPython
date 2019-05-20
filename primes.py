for n in range(2, 100): #range(2,100)表示含左侧 2，不含右侧 100，是不是第三次看到这个说法了？
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:                  # 这里目前你可能看不懂…… 但先关注结果吧。
        print(n)