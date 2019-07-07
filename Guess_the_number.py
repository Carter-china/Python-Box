import random

a = random.randint(1, 100)
b = 5

while True:
    print('   ')
    c = input( '我在1到100之间选了一个数，它是多少呢？:')
    c = float(c)
    if c == a:
        print('猜对了！')
        break
    elif c < a:

        print('小了')
        b = b - 1
        b = str(b)
        print('还剩' + b + '次')
        if b == '0':
            a = str(a)
            print('正确的数为' + a)
            n = input( '还要玩吗（y/n）？:')
            if n == 'y' or n == 'Y':
                pass
            elif n == 'n' or n == 'N':
                break
            a = int(a)
            b = 5
        elif b == '1':
            if a % 2 == 0:
                print('提示:那个数是偶数。')
            else:
                print('提示:那个数是奇数。')
        b = int(b)
    elif c > a:
        print('大了')
        b = b - 1
        b = str(b)
        print('还剩' + b + '次')
        if b == '0':
            a = str(a)
            print('正确的数为' + a)
            n = input( '还要玩吗（y/n）？:')
            if n != 'y' and n != 'Y':
                break
            a = int(a)
            b = 5
        elif b == '1':
            if a % 2 == 0:
                print('提示:那个数是偶数。')
            else:
                print('提示:那个数是奇数。')

        b = int(b)