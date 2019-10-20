import pygame
from pygame.locals import *
from sys import exit
from random import randint


def text_image(name, size, text, color):
    # 创建新的系统字体对象
    font = pygame.font.SysFont(name, size)
    # 文本渲染
    image = font.render(text, True, color)
    return image


# 变量
path = 'resources/images/'
color = (100, 200, 0)
index = 0
y = 300
score = 0
flag = False
# 生成矩形
rects1 = []
rects2 = []


def layout():
    left = 200
    top = 0
    width = 60
    x_distance = 300
    y_distance = 150
    for i in range(20):
        height = randint(200, 400)
        rects1.append([left, top, width, height])
        rects2.append([left, height + y_distance,
                       width, 600 - height - y_distance])
        left = left + x_distance
        x_distance = x_distance - 5
        y_distance = y_distance - 3


layout()

# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('flappy bird')
bg = pygame.image.load(path + 'bg_day.png')
bg = pygame.transform.smoothscale(bg, (800, 600))
birds = [
    pygame.image.load(
        path + '0.png'),
    pygame.image.load(
        path + '1.png'),
    pygame.image.load(
        path + '2.png')]
over = pygame.image.load(path + 'over.png')
pygame.key.set_repeat(1, 1)
clock = pygame.time.Clock()
# 主循环
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_SPACE:
                y = y - 5
            if key == K_r:
                if flag:
                    flag = False
                    layout()
                    y = 300
                    score = 0
    screen.blit(bg, (0, 0))
    # 结束画面
    if flag or score == 20:
        flag = True
        birds_y = 200
        rects1 = []
        rects2 = []
        screen.blit(over, (300, 270))
        for i in range(score):
            screen.blit(birds[0], (i * 40, birds_y))
        author = text_image("simhei", 35, "本游戏由Carter Ron制作", (255, 105, 180))
        screen.blit(author, (230, 330))
        pygame.display.update()
        continue
    # 绘制矩形
    for i in range(len(rects1)):
        pygame.draw.rect(screen, color, rects1[i])
        pygame.draw.rect(screen, color, rects2[i])
        rects1[i][0] = rects1[i][0] - 6
        rects2[i][0] = rects2[i][0] - 6
    # 绘制飞翔的小鸟
    screen.blit(birds[index], (0, y))
    if index < 2:
        index = index + 1
    else:
        index = 0
    y = y + 2
    # 判断矩形障碍列表是否为空 并且刚好移出游戏窗口就将上下的矩形障碍移出 分数加一
    if rects1 and rects1[0][0] <= -60:
        rects1.pop(0)
        rects2.pop(0)
        score = score + 1
    # 碰撞检测
    if rects1:
        if (rects1[0][0] < 48 and rects1[0][3] > y) or (
                rects2[0][0] < 48 and rects2[0][1] < y + 48):
            flag = True
    # 绘制分数

    img = text_image("simhei", 50, str(score), (255, 255, 255))
    screen.blit(img, (20, 20))
    pygame.display.update()