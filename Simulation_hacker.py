import random

a = 'open'
b = 'run'
c = 'download'
d = 'back'
n = ['PyCharm.exe', 'PC KING.exe', 'PhpStorm.exe', 'LEGO Backstage.exe', 'Pentagon File Manager.exe']
o = random.randint(0, 4)

# 欢迎语
print('-' * 37)
print('\t欢迎来到C.T.黑客软件!')
print('-' * 37)
# 邮件/打开

mail = '您好，我是MRX:\n\t我是一名黑客。我要把我的\n\t技术传授给你!现在已经把本人\n\t秘藏的《黑客软件V5》安装在了\n\t你的系统里。\n加油吧!\n--MRX'
print('\n你有一封新邮件,输入open打开查看。\n')
while True:
    h = input('--＞')
    if h == a:
        print(mail)
        print('\n输入run运行程序')

        # 打开“软件”
        while True:

            h = input('--＞')
            if h == b:

                # 伪字符画
                print('-' * 15 + 'Sign in' + '-' * 15)
                # 问用户名/密码
                h = input('Username:')
                h2 = input('Password:')
                print('-' * 9 + 'sign in suceesfully' + '-' * 9)
                # 伪 下载软件
                print('\n输入dir查看当前文件目录')
                while True:
                    h = input('--＞')
                    if h == 'dir':
                        print('app〈DIR〉\nlog〈DIR〉\nuser〈DIR〉\nresource〈DIR〉\n')
                        print('输入“app”查看此目录下的文件')
                        while True:
                            h = input('--＞')
                            if h == 'app':
                                print(n[o])
                                print('\n输入download极速下载！\n')
                                while True:
                                    h = input('-->')
                                    if h == c:
                                        print('0%')
                                        print('50%')
                                        print('100%')
                                        print('下载成功!')
                                        print('\n东西到手了，输入back快走\n')
                                        while True:
                                            h = input('-->')
                                            if h == d:
                                                exit()
                                            else:
                                                print('无效')

                                    else:
                                        print('无效')
                            else:
                                print('请输入app。')
                    else:
                        print('无效')
            else:
                print('无效')
        # 伪 退出被黑用户

        else:
            print('无效')
    else:
        print('无效')