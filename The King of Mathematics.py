import random

s = 0

print('   ')
print('欢迎来到出题国，现在开始挑战!')
print('   ')
c = input('请选择关卡（a=加，b=减，c=乘，d=除）：')

if c == 'a':
    while True:

        f = random.randint(1, 101)
        f = str(f)
        g = random.randint(1, 101)
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
            elif s > 60 and s < 90:
                print('你得了银牌！')
            elif s > 90:
                print('你得了金牌！')
            else:
                print('你得了纸牌！')
            print('   ')
            s = str(s)

elif c == 'b':
    while True:

        f = random.randint(1, 101)
        f = str(f)
        g = random.randint(1, 101)
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
            if s > 30 and s < 60:
                print('你得了铜牌！')
            elif s > 60 and s < 90:
                print('你得了银牌！')
            elif s > 90:
                print('你得了金牌！')
            else:
                print('你得了纸牌！')
            s = str(s)
            print('   ')
elif c == 'c':
    while True:

        f = random.randint(1, 101)
        f = str(f)
        g = random.randint(1, 101)
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
            if s > 30 and s < 60:
                print('你得了铜牌！')
            elif s > 60 and s < 90:
                print('你得了银牌！')
            elif s > 90:
                print('你得了金牌！')
            else:
                print('你得了纸牌！')
            s = str(s)
            print('   ')


elif c == 'd':
    while True:

        f = random.randint(1, 101)
        f = str(f)
        g = random.randint(1, 101)
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
            if s > 30 and s < 60:
                print('你得了铜牌！')
            elif s > 60 and s < 90:
                print('你得了银牌！')
            elif s > 90:
                print('你得了金牌！')
            else:
                print('你得了纸牌！')
            s = str(s)
            print('   ')


else:
    print('输入无效')   