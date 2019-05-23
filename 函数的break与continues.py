# for n in range(2, 100):
#     if n == 2:
#         print(n)
#         continue
#     for i in range(2, n):
#         if (n % i) == 0:
#             break
#     print(n)

from random import randrange

coin_user, coin_bot = 10, 10  # 可以用一个赋值符号分别为多个变量赋值
rounds_of_game = 0


def bet(dice, wager):  # 接收两个参数，一个是骰子点数，另一个用户的输入
    if dice == 7:
        print(f'The dice is {dice};\nDRAW!\n')  # \n 是换行符号
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
        else:
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
    elif dice > 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
        else:
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1


while True:  # 除 for 之外的另外一个循环语句
    print(f'You: {coin_user}\t Bot: {coin_bot}')
    dice = randrange(2, 13)  # 生成一个 2 到 12 的随机数
    wager = input("What's your bet? ")
    if wager == 'q':
        break
    elif wager in 'bs':  # 只有当用户输入的是 b 或者 s 得时候，才 “掷骰子”……
        result = bet(dice, wager)
        coin_user += result  # coin_user += result 相当于 coin_user = coin_user + result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print("Woops, you've LOST ALL, and game over!")
        break
    elif coin_bot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break

print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user} coins now.\nBye!")
