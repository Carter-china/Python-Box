#初始
import time
import random

print(37*'-')
print('\t\t弹瓶盖大赛！')
print(37*'-')
a=1

me='A'
you='B'
x=['出界了。','击中了！','没过网。','没击中。']
f1=10
f2=10
fqs=0

#游戏开始
print('大家好！欢迎来到时间为：',time.ctime(),'的弹瓶盖大赛！')
print('我是你的裁判——Carter Ron!')
while True:

    print('现在我宣布，第',a,'场比赛开始！\n')
    b=input('争球，你是A方，请输入正面或反面(1=正，2=反)：')
    c=random.randint(0,1)

    if b == '1' or b == '2':
        if c == 0:
            time.sleep(1)
            print('结果为：',me)
            fq=me
        else:
            time.sleep(1)
            print('结果为：',you)
            fq=you
    else:
        b = input('请重新争球，你是A方，请输入正面或反面(1=正，2=反)：')
        if b == '1' or b == '2':
            if c == 0:
                time.sleep(1)
                print('结果为：',me)
                fq=me
            else:
                time.sleep(1)
                print('结果为：',you)
                fq=you
    for i in range(400):

        if f1<=0 or f2<=0:
            if f1 <= 0:
                print('你输了')
                yn=input('是否再来一局(Y/n)')
                if yn=='n' or yn=='N':
                    exit()
                elif yn=='y' or yn=='Y':
                    a+=1
                    f1=10
                    f2=10
                    break
                else:
                    print('无效')

            elif f2 <= 0:
                print('你赢了！')
                yn = input('是否再来一局(Y/n)')
                if yn == 'n' or yn == 'N':
                    exit()
                elif yn == 'y' or yn == 'Y':
                    a += 1
                    f1 = 10
                    f2 = 10
                    break
                else:
                    print('无效')

        print(me, '还有', f1, '分')
        print(you, '还有', f2, '分\n')
        print('现在由',fq,'方发球。\n')
        '''a'''
        if fq == me:
            q=input('请输入任意内容:')
            q=random.randint(0,3)
            time.sleep(1)
            print(fq,'方',x[q])
            if x[q] == '击中了！':
                if fq == me:
                    fqs = f2
                    fqs -= 1
                    f2 = fqs
                elif fq == you:
                    fqs = f1
                    fqs -= 1
                    f1 = fqs

            elif x[q] == '出界了。' or x[q] == '没过网。':
                if fq == me:
                    fqs=f1
                    fqs-=1
                    f1=fqs
                elif fq == you:
                    fqs=f2
                    fqs-=1
                    f2=fqs
        elif fq==you:
            time.sleep(3)
            q = random.randint(0, 3)
            time.sleep(1)
            print(fq, '方', x[q])
            if x[q] == '击中了！':
                if fq == me:
                    fqs = f2
                    fqs -= 1
                    f2 = fqs
                elif fq == you:
                    fqs = f1
                    fqs -= 1
                    f1 = fqs
            elif x[q] == '出界了。' or x[q] == '没过网。':
                if fq == me:
                    fqs = f1
                    fqs -= 1
                    f1 = fqs
                elif fq == you:
                    fqs = f2
                    fqs -= 1
                    f2 = fqs
                '''b'''

        if fq == you:
            fq=me
        else:
            fq=you