import pygame
import sys
import math

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((600, 600))

# 设置颜色
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# 设置球的初始数字
numbers = [8, 8, 8]

# 记录每个回合开始时球的数字
start_numbers = numbers[:]

# 设置当前回合中被点击的球
clicked_ball = None

# 设置球的半径
RADIUS = 50

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(3):
                # 计算鼠标点击位置和球心的距离
                distance = math.sqrt((x - (100+200*i))**2 + (y - 300)**2)
                # 如果距离小于球的半径，那么就认为球被点击了
                if distance < RADIUS and numbers[i] > 0 and (clicked_ball is None or clicked_ball == i):
                    if clicked_ball is None and start_numbers[i] > 5 and numbers[i] > 1:
                        numbers[i] -= 1
                    elif clicked_ball is not None and (start_numbers[clicked_ball] <= 5 or numbers[i] > 1):
                        numbers[i] -= 1
                    clicked_ball = i
            if 250 < x < 350 and 500 < y < 550:
                clicked_ball = None
                start_numbers = numbers[:]
            # 检查游戏是否结束，如果结束则检查是否点击了"你输了"，如果点击则重新开始游戏
            if sum(numbers) == 0 and 250 < x < 350 and 200 < y < 250:
                numbers = [8, 8, 8]
                start_numbers = numbers[:]
                clicked_ball = None

    # 清屏
    screen.fill(BLUE)

    # 绘制球和数字
    for i in range(3):
        pygame.draw.circle(screen, YELLOW, (100+200*i, 300), RADIUS)
        font = pygame.font.Font(None, 50)
        text = font.render(str(numbers[i]), True, (0, 0, 0))
        screen.blit(text, (90+200*i, 280))

    # 绘制换回合按钮
    pygame.draw.rect(screen, RED, (250, 500, 100, 50))
    font = pygame.font.Font(None, 30)
    text = font.render("turn", True, (0, 0, 0))
    screen.blit(text, (260, 510))

    # 检查游戏是否结束
    if sum(numbers) == 0:
        font = pygame.font.Font(None, 50)
        text = font.render("you lost", True, (0, 0, 0))
        screen.blit(text, (250, 200))

    # 更新屏幕
    pygame.display.flip()

#                                  ||
#                         ||       ||||
#                         |||       |||                  |||||                           ||          ||||                                               ||
#                         |||| |||  |||                  |||||                           |||  || |||||||||               |||      ||||                 ||||
#                         |||  |||  |||                   |||||                          |||  |||||   |||||               |||      ||||                ||||
#                        ||||   ||  |||||||                 ||       ||||               ||||  |||    |||||                |||      ||||                ||||
#                        |||    ||||||||||||                    ||||||||||              |||    ||    ||||                ||||      ||||                ||||
#                       |||  |||||||||| ||||                    ||||  |||||             |||    || ||||||                 |||       |||                 ||||
#                       |||     ||  ||| ||||             ||||    ||   ||||             |||     |||||||||                 |||       |||                 ||||
#                      ||||     || ||||||||           ||||||||   ||   ||||             |||     |||||||||                |||        |||  ||||||         ||||
#                      ||||     ||||||||||         ||||||||||    || ||||||            ||||      |||||                   |||       |||||||||||||        ||||
#                     |||||     ||||||||||         ||||| |||     |||||||||            ||||        |||  ||||||          |||| |||||||||||||||||||        ||||
#                    ||| |||||||||||||||||          ||  ||||     |||||||||           |||||        |||||||||||          |||| |||||||||                   |||
#                   |||  || ||||||  |||                 |||      ||   ||||          ||| ||  |||||||||||||||||         |||||  ||  |||                    |||
#                  |||   || ||  ||  |||||||||          ||||||    ||   |||           ||| || ||||||||||                ||| ||      |||                    |||
#                  |     || ||  ||||||||||||||         ||||||||  ||||||||          |||  ||  |||  |||||              |||  ||      |||                    |||
#                        |||||||||| |||    |||        |||||||||  ||||||||          |    ||      |||||||            ||||  ||    ||||   |||||             ||
#                        |||||||||  |||    |||       ||| || |||  |||| |||               ||      |||||||||          |||   ||    |||||||||||||            ||
#                        ||||  |||  |||   |||       |||| ||      ||   |||               ||     ||| || ||||         |     ||    |||||   |||||            ||
#                       |||    |||  || ||||||      ||||  ||      ||   |||               ||    |||  ||  ||||||            ||   ||||     |||||
#                       |||   |||   ||  |||||     ||||   ||      ||   |||               ||   |||  |||   ||||||||         ||   ||||     ||||            ||||
#                       |||   |||   ||  ||||      ||     ||      || ||||||||||          || ||||   |||    |||||||         ||  ||||||    |||             ||||
#                       |||  |||    ||   ||       |     ||| |||||||||||||||||||        ||| ||     |||     |||           ||| ||| ||| |||||||            ||||
#                       ||| |||     ||                  ||| ||||||                     |||        |||                   ||||||  |||||||||||            ||||
#                       ||||||      ||                  |||                            |||        |||                   |||||   ||||||||||
#                                  |||                  |||                             ||        |||                   |||      ||
#                                  |||                  |||                                        ||                    |       |
#                                   ||
#                                   |