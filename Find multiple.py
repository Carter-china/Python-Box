#Find multiple
while True:
    c=1
    d=[]
    b=int(input('请输入数字:'))
    a=int(input('请输入个数:'))
    for i in range(a):
        e=c*b
        d.append(e)
        c+=1
    print(d)    