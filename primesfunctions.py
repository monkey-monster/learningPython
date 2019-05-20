def is_prime(n):            # 定义 is_prime()，接收一个参数
    if n < 2:              # 开始使用接收到的那个参数（值）开始计算……
        return False       # 不再是返回给人，而是返回给调用它的代码……
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

for i in range(80, 110):
    if is_prime(i):          # 调用 is_prime() 函数，
        print(i)            # 如果返回值为 True，则向屏幕输出 i