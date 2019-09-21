import turtle
import zmail
carter = turtle.Pen()
carter.hideturtle()
carter.speed(0)
sspp=['VIP电影破解器','数学助理','黑客模拟器','弹瓶盖']
turtle.screensize(canvwidth = 800,canvheight = 1000,bg = None )

def chushi():
    a = 0
    carter.penup()
    carter.goto(-300,399)
    carter.write('-'*45,font=('宋体',20))
    carter.goto(-160,360)
    carter.write('卡特软件 官方网站',font=('宋体',30))
    carter.goto(-300, 335)
    carter.write('-' * 45, font=('宋体', 20))
    for i in range(5):
        carter.goto(-300+a, 325)
        carter.write('|', font=('宋体', 20))
        a += 149
    a = 0
    for i in range(5):
        carter.goto(-300+a, 300)
        carter.write('|', font=('宋体', 20))
        a += 149
    carter.goto(-300, 280)
    carter.write('-' * 45, font=('宋体', 20))
    carter.goto(-300,300)
    carter.write(' a.团队介绍 b.官方码库 c.商品列表 d.联系我们', font=('宋体', 20))
    a = 300
    for i in range(50):
        carter.write('|\n',font=('宋体',20))
        carter.goto(-300,a)
        a+=-10
    carter.goto(320,300)

    a=300
    for i in range(50):
        carter.write('|\n',font=('宋体',20))
        carter.goto(320,a)
        a+=-10
    carter.goto(-300,-150)
    carter.write('-' * 45, font=('宋体', 20))
    carter.goto(20,50)
    carter.pendown()
    carter.pencolor('yellow')
    carter.dot(340)
    carter.goto(-130,-50)
    carter.penup()
    carter.pencolor('black')
    carter.write('C.T.', font=('宋体', 130))
chushi()
while True:
    a=turtle.textinput('命令','a.团队介绍 b.官方码库 c.商品列表 d.联系我们,r=返回主页,e=退出网页')
    if a=='a':
        carter.clear()
        carter.goto(0, 310)
        carter.write('卡特软件，原名大嘴鱼。', font=('宋体', 30), align='center')
        carter.goto(0,270)
        carter.write('是一个进行手工软件销售的平台。', font=('宋体', 30), align='center')
        carter.goto(0,230)
        carter.write('希望大家都能支持我们！', font=('宋体', 30), align='center')
        carter.goto(0,40)
        carter.pendown()
        carter.pencolor('yellow')
        carter.dot(340)
        carter.goto(-130, -50)
        carter.penup()
        carter.pencolor('black')
        carter.write('C.T.', font=('宋体', 130))
    elif a=='b':
        carter.clear()
        carter.goto(0,310)
        carter.write('官方软件源码下载：', font=('宋体', 30), align='center')
        carter.goto(0,270)
        carter.write('https://github.com/Carter-china/Python-Box', font=('宋体', 15), align='center')
        carter.goto(0, 40)
        carter.pendown()
        carter.pencolor('yellow')
        carter.dot(340)
        carter.goto(-130, -50)
        carter.penup()
        carter.pencolor('black')
        carter.write('C.T.', font=('宋体', 130))
        '''vvv'''
    elif a=='c':
        carter.goto(0, 40)
        carter.pendown()
        carter.pencolor('yellow')
        carter.dot(340)
        carter.goto(-130, -50)
        carter.penup()
        carter.pencolor('black')
        carter.write('C.T.', font=('宋体', 130))
        while True:
            sp=turtle.textinput('下单','请输入商品(0=VIP电影破解器，1=数学助理，2=黑客模拟器，3=弹瓶盖，4=退出):')
            sp=int(sp)
            if sp == 4:
                break
            elif sp != 4:
                em = turtle.textinput('下单', '请输入收货邮箱(请打开你邮箱的SMTP):')

                na=em+' 购买了 '+sspp[sp]

                mail = {
                    'subject': '订单',  # Anything you want.
                    'content_text': na,  # Anything you want.
                    #'attachments': ['/Users/zyh/Documents/example.zip', '/root/1.jpg'],  # Absolute path will be better.
                }

                server = zmail.server('15842352280@163.com','****')

                server.send_mail('15842352280@163.com',mail)
                server.send_mail(em,mail)
                carter.clear()
                carter.goto(0, 0)
                carter.write('已提交！', font=('宋体', 130), align='center')


    elif a=='d':

        bz=turtle.textinput('帮助','请输入你要询问的内容')
        mail = {
            'subject': '问题',  # Anything you want.
            'content_text': bz,  # Anything you want.
            # 'attachments': ['/Users/zyh/Documents/example.zip', '/root/1.jpg'],  # Absolute path will be better.
        }

        server = zmail.server('15842352280@163.com', 'snxsj8h')
        while True:
            if mail['content_text'] != '':

                server.send_mail('15842352280@163.com', mail)
                carter.clear()
                carter.goto(0, 0)
                carter.write('已提交！', font=('宋体', 130), align='center')
                break

            else:

                carter.clear()
                carter.write('无效内容', font=('宋体', 130), align='center')
                bz = turtle.textinput('帮助', '请输入你要询问的内容')
                mail = {
                    'subject': '问题',  # Anything you want.
                    'content_text': bz,  # Anything you want.
                    # 'attachments': ['/Users/zyh/Documents/example.zip', '/root/1.jpg'],  # Absolute path will be better.
                }


    elif a=='r':
        carter.clear()
        chushi()
    elif a=='e':
        break
    else:
        carter.clear()
        carter.goto(0,0)
        carter.write('无效', font=('宋体', 130), align='center')
print('\n已退出网页')

turtle.done()
