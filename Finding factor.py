while True:
    c=[]
    #d=0
    a=int(input('请输入数字:'))
    b=list(range(1,a))
    for i in b:
        x=b[i-1]
        if a % x == 0:
            c.append(i)
        #d=d+1
    #d=0
    c.append(a)
    print(c)    