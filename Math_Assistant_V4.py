import random
i=0
def jsq():
    print('\nHello!我是你的私人计算小助手（六代）\n!')
    print('注:输入次数时输入n退出\n')
    while True:
        a = input('请输入模式（a=加法，b=减法，c=乘法，d=除法，e=判断大小，f=平方，g=立方，h=自定义平方）：')
        b = input('请输入次数:')
        if b=='n' or b=='N':
            break
        else:
            b = int(b)

        if a == 'a':
            for i in range(b):
                c = input('请输入数1:')
                c1 = float(c)
                d = input('请输入数2:')
                d1 = float(d)
                print(c1 + d1)
                print('\n')
        elif a == 'b':
            for i in range(b):
                c = input('请输入数1:')
                c1 = float(c)
                d = input('请输入数2:')
                d1 = float(d)
                print(c1 - d1)
                print('\n')
        elif a == 'c':
            for i in range(b):
                c = input('请输入数1:')
                c1 = float(c)
                d = input('请输入数2:')
                d1 = float(d)
                print(c1 * d1)
                print('\n')
        elif a == 'd':
            for i in range(b):
                c = input('请输入数1:')
                c1 = float(c)
                d = input('请输入数2:')
                d1 = float(d)
                print(c1 / d1)
                print('\n')
        elif a == 'e':
            for i in range(b):
                c = input('请输入数1:')
                c1 = float(c)
                d = input('请输入数2:')
                d1 = float(d)
                if c1 < d1:
                    c1 = str(c1)
                    d1 = str(d1)
                    print(c1 + '<' + d1)
                    print('\n')

                elif c1 > d1:
                    c1 = str(c1)
                    d1 = str(d1)
                    print(c1 + '>' + d1)
                    print('\n')


                elif c1 == d1:
                    c1 = str(c1)
                    d1 = str(d1)
                    print(c1 + '=' + d1)
                    print('\n')

        elif a == 'f':
            c = input('请输入数字：')
            c1 = float(c)
            print(c ** 2)
            print('\n')

        elif a == 'g':
            c = input('请输入数字：')
            c1 = float(c)
            print(c ** 3)
            print('\n')

        elif a == 'h':
            c = input('请输入数字：')
            c1 = float(c)
            d = input('请输入次方数:')
            d1 = float(d)
            print(c ** d)
            print('\n')

        else:
            print('输入无效\n')

def jsd():
    class point():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.available = []
            self.value = 0

    # 该空格所在行有哪
    def rowNum(p, sudoku):
        # set用于去重，因为0不止一个！
        row = set(sudoku[p.y * 9: (p.y + 1) * 9])
        row.remove(0)
        return row

    # 该空格所在列有哪些数
    def colNum(p, sudoku):
        col = []
        length = len(sudoku)
        for j in range(p.x, length, 9):
            col.append(sudoku[j])
        col = set(col)
        col.remove(0)
        return col

    # 该空格所在小九宫有哪些数
    def blockNum(p, sudoku):
        block_x = p.x // 3
        block_y = p.y // 3
        block = []
        start_point = block_y * 3 * 9 + block_x * 3
        for j in range(start_point, start_point + 3):
            block.append(sudoku[j])
        for j in range(start_point + 9, start_point + 9 + 3):
            block.append(sudoku[j])
        for j in range(start_point + 9 + 9, start_point + 9 + 9 + 3):
            block.append(sudoku[j])
        block = set(block)
        block.remove(0)
        return block

    # 初始化，作用为：
    # 把每个空格可能的点先列举出来
    # 比如空格所在的行和列还有小九宫内有数字1、2、3
    # 那么空格只能填入4、5、6、7、8、9中的某个数
    def initialize(sudoku):
        sudokuList = []
        length = len(sudoku)
        for index in range(length):
            # 找到需要填入的单元，即空格
            if sudoku[index] == 0:
                p = point(index % 9, index // 9)
                for i in range(1, 10):
                    # 如果行、列、小九宫中均没有i这个数
                    if (i not in rowNum(p, sudoku)) and (i not in colNum(p, sudoku)) and (i not in blockNum(p, sudoku)):
                        p.available.append(i)
                sudokuList.append(p)
        return sudokuList

    # 检验该数填入空格后是否满足数独规则
    def check(p, sudoku):
        if p.value == 0:
            return False
        if (p.value not in rowNum(p, sudoku)) and (p.value not in colNum(p, sudoku)) and (
                p.value not in blockNum(p, sudoku)):
            return True
        else:
            return False

    # 展示数独结果
    def showResult(sudoku):
        for r in range(9):
            for c in range(9):
                print('%d ' % (sudoku[r * 9 + c]), end='')
            print('')

    # 深搜来解数独
    def solve(p, sudoku):
        available_Num = p.available
        for ava in available_Num:
            p.value = ava
            if check(p, sudoku):
                sudoku[p.y * 9 + p.x] = p.value
                if len(sudokuList) < 1:
                    showResult(sudoku)
                    return
                p_next = sudokuList.pop()
                solve(p_next, sudoku)
                sudoku[p_next.y * 9 + p_next.x] = 0
                sudoku[p.y * 9 + p.x] = 0
                p_next.value = 0
                sudokuList.append(p_next)
            else:
                pass

    if __name__ == '__main__':
        # 0代表需要填入的单元，即空格
        print('\n嗨！我是你的数独解题助手！')

        # 之后 加缩进的
        sudoku = []
        print("\n请一次输入一行的9个数字,之间以空格间隔,数字0代替空白格。\n")
        n = 1
        while True:
            print("现在是第%s行" % n)
            lis = input().strip().split(" ")
            lis = list(map(int, lis))
            if len(lis) == 9:
                sudoku.extend(lis)
                n += 1
                if n >= 10:
                    break
            else:
                print("本行有误请重新输入")

        sudokuList = initialize(sudoku)
        print('\n数独题目为：\n')
        showResult(sudoku)
        print('\n开始解题…… \n')
        print('\n数独的解为：\n')
        p_first = sudokuList.pop()
        solve(p_first, sudoku)

def sxcg():

    s = 0

    print('\n欢迎来到出题国，现在开始挑战!')
    c = input('\n请选择关卡（a=加，b=减，c=乘，d=除）：')

    if c == 'a':
        while True:

            f = random.randint(1, 100)
            f = str(f)
            g = random.randint(1, 100)
            g = str(g)
            h = input(f + '+' + g + '=?:')
            h = float(h)
            f = float(f)
            g = float(g)
            i = f + g
            if h == i:
                print('挑战成功!开始下一关!')
                s = int(s)
                s = s + 1

            elif h != i:
                i = str(i)
                print('错误!正确为' + i)
                s = str(s)
                print('你共得了' + s + '分')
                s = int(s)
                if s > 30 and s < 60:
                    print('你得了铜牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 60 and s < 90:
                    print('你得了银牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 90:
                    print('你得了金牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                else:
                    print('你得了纸牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                print('   ')
                s = str(s)

    elif c == 'b':
        while True:

            f = random.randint(1, 100)
            f = str(f)
            g = random.randint(1, 100)
            g = str(g)
            h = input(g + '-' + f + '=?:')
            h = float(h)
            f = float(f)
            g = float(g)
            i = g - f
            if h == i:
                print('挑战成功!开始下一关!')
                s = int(s)
                s = s + 1
            elif h != i:
                i = str(i)
                print('错误!正确为' + i)
                s = str(s)
                print('你共得了' + s + '分')
                s=int(s)
                if s > 30 and s < 60:
                    print('你得了铜牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 60 and s < 90:
                    print('你得了银牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 90:
                    print('你得了金牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                else:
                    print('你得了纸牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                s = str(s)
                print('   ')
    elif c == 'c':
        while True:

            f = random.randint(1, 100)
            f = str(f)
            g = random.randint(1, 100)
            g = str(g)
            h = input(g + '×' + f + '=?:')
            h = float(h)
            f = float(f)
            g = float(g)
            i = g * f
            if h == i:
                print('挑战成功!开始下一关!')
                s = int(s)
                s = s + 1
            elif h != i:
                i = str(i)
                print('错误!正确为' + i)
                s = str(s)
                print('你共得了' + s + '分')
                s=int(s)
                if s > 30 and s < 60:
                    print('你得了铜牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 60 and s < 90:
                    print('你得了银牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 90:
                    print('你得了金牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                else:
                    print('你得了纸牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                s = str(s)
                print('   ')


    elif c == 'd':
        while True:

            f = random.randint(1, 100)
            f = str(f)
            g = random.randint(1, 100)
            g = str(g)
            h = input(g + '÷' + f + '=?:')
            h = float(h)
            f = float(f)
            g = float(g)
            i = g / f
            if h == i:
                print('挑战成功!开始下一关!')
                s = int(s)
                s = s + 1
            elif h != i:
                i = str(i)
                print('错误!正确为' + i)
                s = str(s)
                print('你共得了' + s + '分')
                s=int(s)
                if s > 30 and s < 60:
                    print('你得了铜牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 60 and s < 90:
                    print('你得了银牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                elif s > 90:
                    print('你得了金牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                else:
                    print('你得了纸牌！')
                    n = input('还要玩吗（y/n）？:')
                    if n == 'y' or n == 'Y':
                        pass
                    elif n == 'N' or n == 'n':
                        break
                s = str(s)
                print('   ')


    else:
        print('输入无效')

def qys():
    while True:
        c = []
        # d=0
        a = input('请输入数字(输入n退出):')
        if a=='n' or a=='N':
            break
        else:
            a=int(a)
            b = list(range(1, a))
        for i in b:
            x = b[i - 1]
            if a % x == 0:
                c.append(i)
            # d=d+1
        # d=0
        c.append(a)
        print(c)

def zbs():
    
    c = 1
    d = []
    b = int(input('请输入数字:'))
    a = int(input('请输入个数:'))
    for i in range(a):
        e = c * b
        d.append(e)
        c += 1
    print(d)

def csz():

    a = random.randint(1, 100)
    b = 5

    while True:
        print('   ')
        c = input('我在1到100之间选了一个数，它是多少呢？:')
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
                n = input('还要玩吗（y/n）？:')
                if n == 'y' or n == 'Y':
                    pass
                elif n == 'N' or n == 'n':
                    break
                else:
                    print('输入无效，默认为退出。')
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
                n = input('还要玩吗（y/n）？:')
                if n == 'y' or n == 'Y':
                    pass
                elif n == 'N' or n == 'n':
                    break
                else:
                    print('输入无效，默认为退出。')
                    break
                a = int(a)
                b = 5
            elif b == '1':
                if a % 2 == 0:
                    print('提示:那个数是偶数。')
                else:
                    print('提示:那个数是奇数。')

            b = int(b)


while True:
    a = input('\n请输入模式（a=计算器，b=解数独，c=数学闯关，d=求因数，e=找倍数，f=猜数字):')
    if a == 'a':
        jsq()
    # 该空格所在行有哪
    elif a == 'b':
        jsd()
    elif a == 'c':
        sxcg()
    elif a == 'd':
        qys()
    elif a == 'e':
        zbs()
    elif a == 'f':
        csz()
    else:
        print('无效')
