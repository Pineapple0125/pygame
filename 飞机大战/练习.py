# # import pygame
#
# # pygame.init()#初始化
# #
# # class GameSprite(pygame.sprite.Sprite):
# #     def __init__(self, image_name, speed):
# #         super(GameSprite, self).__init__() # 需要主动调用父类代码
# #         # 定义图像属性
# #         self.image = image_name
# #         self.rect = self.image.get_rect()  # 和图像大小一致
# #         self.speed = speed
# #     def update(self):
# #         self.rect.x += self.speed
# #
# #
# #
# # # 创造游戏窗口 要用变量记录
# # screen = pygame.display.set_mode((1500,788))# 返回窗口((长，高)，(是否需要全屏)，(颜色的位数)) 后两个一般不用输入
# #
# # # 使用pygame.Rect 记录豌豆位置
# # Wandou = pygame.Rect(390,500,113,100)# 坐标加大小
# #
# # # 图像的加载
# # BJ = pygame.image.load("./植物大战僵尸素材/背景板.jpg")# 加载图像数据
# # screen.blit(BJ,(0,0))# 加载图像与窗口数据 设置位置
# #
# #
# # WD = pygame.image.load("./植物大战僵尸素材/豌豆.png")# 加载图像数据
# #
# #
# # enemy = GameSprite(pygame.image.load("./植物大战僵尸素材/路障僵尸.png"),1)
# # enemy1 = GameSprite(pygame.image.load("./植物大战僵尸素材/僵尸.jpg"),2)
# #
# # # 创造敌机的精灵组
# # enemy_group = pygame.sprite.Group(enemy,enemy1)
# #
# #
# # clock = pygame.time.Clock() # 设置刷新
# #
# # while True: # 游戏无限循环 ——> 游戏正式开始
# #     clock.tick(144) # ？祯噢
# #
# #     # 捕获事件
# #     for event in pygame.event.get():
# #         if event.type ==pygame.QUIT:
# #             print("游戏退出")
# #             pygame.quit()
# #             exit() # 终止所有程序
# #         events = pygame.event.get()
# #         if len(events)> 0:
# #             print(events)
# #
# #     # 修改飞机的位置
# #     Wandou.y -= 1
# #
# #     # 调用blit方法绘制图像
# #     screen.blit(BJ, (0, 0))# 覆盖原来的飞机 并绘制新的飞机
# #     screen.blit(WD,Wandou)
# #
# #     # 让精灵组调用两个方法
# #     enemy_group.update()
# #     enemy_group.draw(screen)
# #
# #
# #
# #     # 调用update更新显示
# #     pygame.display.update()
# #
# #     pass
# #
# # import random
# # import pygame
# #
# #
# # SCREEN_RECT = pygame.Rect(0,0,1500,640)
# #
# #
# # CRTATE_ENEMT_EVENT = pygame.USEREVENT
# #
# # class GameSprite(pygame.sprite.Sprite):
# #     def __init__(self, image_name,WZ,speed):
# #         super(GameSprite, self).__init__()  # 需要主动调用父类代码
# #         # 定义图像属性
# #         self.image = image_name
# #         self.rect = self.image.get_rect()  # 和图像大小一致
# #         self.speed = speed
# #         self.WZ = WZ
# #
# #
# #
# #     # def update(self):
# #     #     self.rect.x -= self.speed
# #
# # class Background(GameSprite):
# #     def update(self):
# #         # super().update()
# #         pass
# #
# # class Enemy(GameSprite):
# #     def __init__(self,image_name,WZ,speed,life):
# #         # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
# #         super().__init__(image_name,WZ,speed)
# #         self.WZ = random.randint(0,4)
# #         self.speed = random.randint(1,2)
# #         self.life = life
# #         # 敌机位置 bottom（顶部） right(最右边)
# #         self.rect.x = SCREEN_RECT.width
# #         # max_y = SCREEN_RECT.height - self.rect.height
# #         self.rect.y = 10+self.WZ*120
# #
# #     def update(self):
# #         self.rect.x -= self.speed
# #         # 保持飞行水平
# #         if self.rect.x <= 0:
# #             print('游戏结束')
# #             exit()
# #             # 移除精灵组
# #             # self.kill()
# #
# #     def __del__(self):
# #         pass
# #
# # class Hero(GameSprite):
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"),WZ=0,speed=0)
# #         self.rect.centerx = SCREEN_RECT.centerx-200
# #         self.rect.bottom = SCREEN_RECT.bottom-250
# #
# #         # 创建子弹精灵组 因为子弹发射属于hero
# #         self.bullets = pygame.sprite.Group()
# #
# #
# #     def update(self):
# #         if self.rect.y < 0:
# #             self.rect.y = 0
# #         elif self.rect.right > SCREEN_RECT.right:
# #             self.rect.right = SCREEN_RECT.right
# #         elif self.rect.left < SCREEN_RECT.left:
# #             self.rect.left = SCREEN_RECT.left
# #         elif self.rect.y > 540:
# #             self.rect.y = 540
# #
# #     def fire(self):
# #         # 创建子弹精灵
# #         bullet = Bullet()
# #         # 设置精灵位置
# #         bullet.rect.centerx = self.rect.centerx + 25
# #         bullet.rect.centery = self.rect.centery - 22
# #
# #
# #         # 添加到精灵族
# #         self.bullets.add(bullet)
# #
# # class Bullet(GameSprite):
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"),WZ=0,speed=0)
# #         self.speed = 10
# #         pass
# #
# #
# #     def update(self):
# #         super().update()
# #         self.rect.x += self.speed
# #         # 判断子弹飞出屏幕
# #         if self.rect.bottom < 0:
# #             self.kill()
# #
# #         pass
# #
# #     def __del__(self):
# #         pass
# #
# # class Plants_vs_Zombies(object):
# #
# #     def __init__(self):
# #         print("初始化")
# #
# #         # 1.创造游戏窗口
# #         self.screen = pygame.display.set_mode(SCREEN_RECT.size) # size为元组
# #         # bj = pygame.image.load("./植物大战僵尸素材/地图(2).jpg")
# #         # self.screen.blit(bj, (0, 0))
# #         # 2.创造游戏时钟
# #         self.clock = pygame.time.Clock()
# #         # 3.调用私有方法，精灵和精灵组的创建
# #         self.__create_sprites()
# #
# #         # 设置定时器事件
# #         pygame.time.set_timer(CRTATE_ENEMT_EVENT,1000) # 定时器常量＋毫秒
# #
# #     def __create_sprites(self):
# #         BJ = Background(pygame.image.load("./植物大战僵尸素材/地图(2).jpg"),WZ=0,speed=0)
# #         self.back_group = pygame.sprite.Group(BJ)
# #
# #         self.enemy = Enemy((pygame.image.load("./植物大战僵尸素材/普通僵尸.gif")), 0, 0, 1)
# #         self.enemy_group = pygame.sprite.Group(self.enemy)
# #
# #         # 创造豌豆精灵和精灵族
# #         self.hero = Hero()
# #         self.hero_group = pygame.sprite.Group(self.hero)
# #         pass
# #
# #
# #     def start_game(self):
# #         print("游戏开始>>>>>>")
# #         while True:
# #             # 1，设置刷新
# #             self.clock.tick(60)
# #             # 2，事件监听
# #             self.__event_handler()
# #             # 3，碰撞测试
# #             self.__check_collide()
# #             # 4，更新绘制精灵
# #             self.__update_sprites()
# #             # 5，更新显示
# #             pygame.display.update()
# #
# #             pass
# #
# #     def __event_handler(self):# 2，事件监听
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 Plants_vs_Zombies.__game_over()
# #             elif event.type == CRTATE_ENEMT_EVENT:
# #                 enemy = Enemy((pygame.image.load("./植物大战僵尸素材/普通僵尸.gif")),0,0,1)
# #                 self.enemy_group.add(enemy)
# #             elif event.type == pygame.MOUSEBUTTONDOWN:
# #                 self.hero.fire()
# #             # elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
# #             #     print("www") # 这样子只能记录单次按下 不能记录长按
# #             pass
# #
# #         key_operation = pygame.key.get_pressed() #返回元组
# #         if key_operation[pygame.K_w]: # 索引为1 表示按下
# #             self.hero.rect.y -= 3
# #         elif key_operation[pygame.K_s]:
# #             self.hero.rect.y += 3
# #         elif key_operation[pygame.K_d]:
# #             self.hero.rect.x += 3
# #         elif key_operation[pygame.K_a]:
# #             self.hero.rect.x -= 3
# #
# #
# #     def __check_collide(self):# 3，碰撞测试
# #         if self.enemy.life < 5:
# #             pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,False)
# #             self.enemy.life += 1
# #         if self.enemy.life == 5:
# #             pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
# #         # 子弹和僵尸 True代表俩者都会被消除
# #         pass
# #
# #     def __update_sprites(self):
# #
# #         self.back_group.update()
# #         self.back_group.draw(self.screen)
# #
# #         self.enemy_group.update()
# #         self.enemy_group.draw(self.screen)
# #
# #         self.hero.bullets.update()
# #         self.hero.bullets.draw(self.screen)
# #
# #         self.hero_group.update()
# #         self.hero_group.draw(self.screen)
# #         pass
# #
# #
# #     @staticmethod
# #     def __game_over():
# #         print("游戏结束")
# #
# #         pygame.quit()
# #         exit()
# #
# #
# #
# #
# #
# # if __name__ == '__main__':
# #
# #
# #     game = Plants_vs_Zombies()
# #     game.start_game()
# # import random
# # import pygame
# #
# #
# # SCREEN_RECT = pygame.Rect(0,0,1500,640)
# #
# #
# # CRTATE_ENEMT_EVENT = pygame.USEREVENT
# #
# # class GameSprite(pygame.sprite.Sprite):
# #     def __init__(self, image_name,WZ=0,speed=1):
# #         super(GameSprite, self).__init__()  # 需要主动调用父类代码
# #         # 定义图像属性
# #         self.image = image_name
# #         self.rect = self.image.get_rect()  # 和图像大小一致
# #         self.speed = speed
# #         self.WZ = WZ
# #
# #
# #     # def update(self):
# #     #     self.rect.x -= self.speed
# #
# # class Background(GameSprite):
# #     def update(self):
# #         # super().update()
# #         pass
# #
# # class Enemy(GameSprite):
# #     def __init__(self):
# #         # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/幽灵.png"))
# #         self.WZ =random.randint(0,4)
# #         self.speed = random.randint(1,2)
# #         # 敌机位置 bottom（顶部） right(最右边)
# #         self.rect.x = SCREEN_RECT.width
# #         # max_y = SCREEN_RECT.height - self.rect.height
# #         self.rect.y = 10+self.WZ*120
# #         self.soulbullets = pygame.sprite.Group()
# #
# #
# #     def update(self):
# #         self.rect.x -= self.speed
# #         # 保持飞行水平
# #         if self.rect.x <= 0:
# #             print('游戏结束')
# #             exit()
# #             # 移除精灵组
# #             # self.kill()
# #
# #     def fire(self):
# #         # 创建子弹精灵
# #         soulbullet = SoulBullet()
# #         # 设置精灵位置
# #         soulbullet.rect.centerx = self.rect.centerx
# #         soulbullet.rect.centery = self.rect.centery
# #
# #
# #         # 添加到精灵族
# #         self.soulbullets.add(soulbullet)
# #
# #     def __del__(self):
# #         pass
# #
# # class Hero(GameSprite):
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"))
# #         self.rect.centerx = SCREEN_RECT.centerx-200
# #         self.rect.bottom = SCREEN_RECT.bottom-250
# #
# #         # 创建子弹精灵组 因为子弹发射属于hero
# #         self.bullets = pygame.sprite.Group()
# #
# #
# #     def update(self):
# #         if self.rect.y < 0:
# #             self.rect.y = 0
# #         elif self.rect.right > SCREEN_RECT.right:
# #             self.rect.right = SCREEN_RECT.right
# #         elif self.rect.left < SCREEN_RECT.left:
# #             self.rect.left = SCREEN_RECT.left
# #         elif self.rect.y > 540:
# #             self.rect.y = 540
# #
# #     def fire(self):
# #         # 创建子弹精灵
# #         bullet = Bullet()
# #         # 设置精灵位置
# #         bullet.rect.centerx = self.rect.centerx + 25
# #         bullet.rect.centery = self.rect.centery - 22
# #
# #
# #         # 添加到精灵族
# #         self.bullets.add(bullet)
# #
# # class Bullet(GameSprite):
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
# #         self.speed = 10
# #         pass
# #
# #
# #     def update(self):
# #         super().update()
# #         self.rect.x += self.speed
# #         # 判断子弹飞出屏幕
# #         if self.rect.x > 1500:
# #             self.kill()
# #
# #         pass
# #
# #     def __del__(self):
# #         pass
# #
# # class SoulBullet(GameSprite):
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
# #         self.speed = 10
# #         pass
# #
# #
# #     def update(self):
# #         super().update()
# #         self.rect.x -= self.speed
# #         # 判断子弹飞出屏幕
# #         if self.rect.x < 0:
# #             self.kill()
# #
# #         pass
# #
# #     def __del__(self):
# #         pass
# #
# # class Plants_vs_Zombies(object):
# #
# #     def __init__(self):
# #         print("初始化")
# #
# #         # 1.创造游戏窗口
# #         self.screen = pygame.display.set_mode(SCREEN_RECT.size) # size为元组
# #         # bj = pygame.image.load("./植物大战僵尸素材/地图(2).jpg")
# #         # self.screen.blit(bj, (0, 0))
# #         # 2.创造游戏时钟
# #         self.clock = pygame.time.Clock()
# #         # 3.调用私有方法，精灵和精灵组的创建
# #         self.__create_sprites()
# #
# #         # 设置定时器事件
# #         pygame.time.set_timer(CRTATE_ENEMT_EVENT,1000) # 定时器常量＋毫秒
# #
# #     def __create_sprites(self):
# #         BJ = Background(pygame.image.load("./植物大战僵尸素材/地图(2).jpg"))
# #         self.back_group = pygame.sprite.Group(BJ)
# #         self.enemy_group = pygame.sprite.Group()
# #         self.
# #         # 创造豌豆精灵和精灵族
# #         self.hero = Hero()
# #         self.hero_group = pygame.sprite.Group(self.hero)
# #         pass
# #
# #
# #     def start_game(self):
# #         print("游戏开始>>>>>>")
# #         while True:
# #             # 1，设置刷新
# #             self.clock.tick(60)
# #             # 2，事件监听
# #             self.__event_handler()
# #             # 3，碰撞测试
# #             self.__check_collide()
# #             # 4，更新绘制精灵
# #             self.__update_sprites()
# #             # 5，更新显示
# #             pygame.display.update()
# #
# #             pass
# #
# #     def __event_handler(self):# 2，事件监听
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 Plants_vs_Zombies.__game_over()
# #             elif event.type == CRTATE_ENEMT_EVENT:
# #                 enemy = Enemy()
# #                 self.enemy_group.add(enemy)
# #                 enemy.fire()
# #             elif event.type == pygame.MOUSEBUTTONDOWN:
# #                 self.hero.fire()
# #             # elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
# #             #     print("www") # 这样子只能记录单次按下 不能记录长按
# #         pass
# #         key_operation = pygame.key.get_pressed() #返回元组
# #         if key_operation[pygame.K_w]: # 索引为1 表示按下
# #             self.hero.rect.y -= 3
# #         elif key_operation[pygame.K_s]:
# #             self.hero.rect.y += 3
# #         elif key_operation[pygame.K_d]:
# #             self.hero.rect.x += 3
# #         elif key_operation[pygame.K_a]:
# #             self.hero.rect.x -= 3
# #
# #
# #     def __check_collide(self):# 3，碰撞测试
# #
# #         pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
# #         # 子弹和僵尸 True代表俩者都会被消除
# #         pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
# #         pass
# #
# #     def __update_sprites(self):
# #
# #         self.back_group.update()
# #         self.back_group.draw(self.screen)
# #
# #         self.enemy_group.update()
# #         self.enemy_group.draw(self.screen)
# #
# #         self.
# #
# #         self.hero.bullets.update()
# #         self.hero.bullets.draw(self.screen)
# #
# #         self.hero_group.update()
# #         self.hero_group.draw(self.screen)
# #         pass
# #
# #
# #     @staticmethod
# #     def __game_over():
# #         print("游戏结束")
# #
# #         pygame.quit()
# #         exit()
# #
# #
# #
# #
# #
# # if __name__ == '__main__':
# #
# #
# #     game = Plants_vs_Zombies()
# #     game.start_game()
# #
# # import random
# # import pygame
# #
# #
# # SCREEN_RECT = pygame.Rect(0,0,1500,640)
# #
# #
# # CRTATE_ENEMT_EVENT = pygame.USEREVENT
# #
# # CRTATE_SOUL = pygame.USEREVENT + 1
# #
# # create_jump = pygame.USEREVENT + 2
# #
# # class GameSprite(pygame.sprite.Sprite):
# #     def __init__(self, image_name,WZ=0,speed=1):
# #         super(GameSprite, self).__init__()  # 需要主动调用父类代码
# #         # 定义图像属性
# #         self.image = image_name
# #         self.rect = self.image.get_rect()  # 和图像大小一致
# #         self.speed = speed
# #         self.WZ = WZ
# #
# #
# #     # def update(self):
# #     #     self.rect.x -= self.speed
# #
# # class Background(GameSprite):
# #     def update(self):
# #         pass
# #
# # class Enemy(GameSprite):
# #     def __init__(self):
# #         # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/鬼蜡烛.gif"))
# #         self.WZ = random.randint(0,4)
# #         self.speed = random.randint(1,2)
# #         # 敌机位置 bottom（顶部） right(最右边)
# #         self.rect.x = SCREEN_RECT.width
# #         # max_y = SCREEN_RECT.height - self.rect.height
# #         self.rect.y = 20+self.WZ*110
# #
# #     def update(self):
# #         self.rect.x -= self.speed
# #         # 保持飞行水平
# #         if self.rect.x <= 0:
# #             print('游戏结束')
# #             print(pygame.time.get_ticks())
# #             exit()
# #             # 移除精灵组
# #             # self.kill()
# #
# #     def __del__(self):
# #         pass
# #
# # class Soul(GameSprite):
# #     def __init__(self):
# #         # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
# #         self.speed = random.randint(1,5)
# #         # 敌机位置 bottom（顶部） right(最右边)
# #         self.rect.x = SCREEN_RECT.width
# #         # max_y = SCREEN_RECT.height - self.rect.height
# #         self.rect.y = random.randint(0,640)
# #
# #     def update(self):
# #         self.rect.x -= self.speed
# #         # 保持飞行水平
# #         if self.rect.x <= 0:
# #             self.kill()
# #
# #     def __del__(self):
# #         pass
# #
# # class Hero(GameSprite):
# #     power = 10
# #
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"))
# #         self.rect.centerx = SCREEN_RECT.centerx-200
# #         self.rect.bottom = SCREEN_RECT.bottom-250
# #
# #         self.vel_y = 0
# #         # self.jumped = False
# #         # 创建子弹精灵组 因为子弹发射属于hero
# #         self.bullets = pygame.sprite.Group()
# #
# #
# #     def update(self):
# #         self.rect.y += 8
# #         if self.rect.y < 0:
# #             self.rect.y = 0
# #         elif self.rect.right > SCREEN_RECT.right:
# #             self.rect.right = SCREEN_RECT.right
# #         elif self.rect.left < SCREEN_RECT.left:
# #             self.rect.left = SCREEN_RECT.left
# #         elif self.rect.y > 540:
# #             self.rect.y = 540
# #
# #         y_move = 0
# #
# #         # 获取按键，并进行相应的移动
# #         key = pygame.key.get_pressed()
# #         if key[pygame.K_k] and Hero.power >= 1:
# #             self.vel_y = -25
# #             Hero.power -= 1
# #             print(Hero.power)
# #             # self.jumped = True
# #         if self.rect.y == 540:
# #             # self.jumped = False
# #             Hero.power = 10
# #
# #
# #         # 添加角色重力（跳跃之后自然下落）
# #         self.vel_y += 1.2
# #         if self.vel_y > 10:
# #             self.vel_y = 10
# #         y_move += self.vel_y
# #
# #
# #         self.rect.y += y_move
# #
# #     def fire(self):
# #         # 创建子弹精灵
# #         bullet = Bullet()
# #         # 设置精灵位置
# #         bullet.rect.centerx = self.rect.centerx + 25
# #         bullet.rect.centery = self.rect.centery - 22
# #
# #
# #         # 添加到精灵族
# #         self.bullets.add(bullet)
# #
# # class Bullet(GameSprite):
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
# #         self.speed = 10
# #         pass
# #
# #     def update(self):
# #         super().update()
# #         self.rect.x += self.speed
# #         # 判断子弹飞出屏幕
# #         if self.rect.x < 0:
# #             self.kill()
# #
# #         pass
# #
# #     def __del__(self):
# #         pass
# #
# # class Plants_vs_Zombies(object):
# #
# #     def __init__(self):
# #         print("初始化")
# #
# #         # 1.创造游戏窗口
# #         self.screen = pygame.display.set_mode(SCREEN_RECT.size) # size为元组
# #         # bj = pygame.image.load("./植物大战僵尸素材/地图(2).jpg")
# #         # self.screen.blit(bj, (0, 0))
# #         # 2.创造游戏时钟
# #         self.clock = pygame.time.Clock()
# #         # 3.调用私有方法，精灵和精灵组的创建
# #         self.__create_sprites()
# #
# #         # 设置定时器事件
# #         pygame.time.set_timer(CRTATE_ENEMT_EVENT,1000) # 定时器常量＋毫秒
# #
# #         pygame.time.set_timer(CRTATE_SOUL, 2000)
# #     def __create_sprites(self):
# #         BJ = Background(pygame.image.load("./植物大战僵尸素材/地图(2).jpg"))
# #         self.back_group = pygame.sprite.Group(BJ)
# #         self.enemy_group = pygame.sprite.Group()
# #         self.soul_group = pygame.sprite.Group()
# #         # 创造豌豆精灵和精灵族
# #         self.hero = Hero()
# #         self.hero_group = pygame.sprite.Group(self.hero)
# #         pass
# #
# #
# #     def start_game(self):
# #         print("游戏开始>>>>>>")
# #         while True:
# #             # 1，设置刷新
# #             self.clock.tick(60)
# #             # 2，事件监听
# #             self.__event_handler()
# #             # 3，碰撞测试
# #             self.__check_collide()
# #             # 4，更新绘制精灵
# #             self.__update_sprites()
# #             # 5，更新显示
# #             pygame.display.update()
# #
# #             pass
# #
# #     def __event_handler(self):# 2，事件监听
# #         if self.hero.rect.y == 540:
# #             self.hero.power = 1
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 Plants_vs_Zombies.__game_over()
# #             elif event.type == CRTATE_ENEMT_EVENT:
# #                 enemy = Enemy()
# #                 self.enemy_group.add(enemy)
# #             elif event.type == CRTATE_SOUL:
# #                 soul = Soul()
# #                 self.soul_group.add(soul)
# #             elif event.type == pygame.KEYDOWN and event.key == pygame.K_j:
# #                 self.hero.fire()
# #             # elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
# #             #     print("www") # 这样子只能记录单次按下 不能记录长按
# #         pass
# #         key_operation = pygame.key.get_pressed() #返回元组
# #         if key_operation[pygame.K_w]: # 索引为1 表示按下
# #             self.hero.rect.y -= 3
# #         elif key_operation[pygame.K_s]:
# #             self.hero.rect.y += 3
# #         elif key_operation[pygame.K_d]:
# #             self.hero.rect.x += 3
# #         elif key_operation[pygame.K_a]:
# #             self.hero.rect.x -= 3
# #         key = pygame.key.get_pressed()
# #         if key[pygame.K_SPACE] and self.hero.power >= 0:
# #             self.vel_y = -25
# #             self.hero.power -= 1
# #             # self.jumped = True
# #         if not key[pygame.K_SPACE] and self.hero.rect.y == 540:
# #             # self.jumped = False
# #             self.power = 2
# #
# #
# #     def __check_collide(self):# 3，碰撞测试
# #         pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
# #         # 子弹和僵尸 True代表俩者都会被消除
# #         if (pygame.sprite.spritecollide(self.hero,self.enemy_group,True) or
# #             pygame.sprite.spritecollide(self.hero,self.soul_group,True)):
# #             print('游戏结束')
# #             print(pygame.time.get_ticks())
# #             exit()
# #         pass
# #
# #     def __update_sprites(self):
# #
# #         self.back_group.update()
# #         self.back_group.draw(self.screen)
# #
# #         self.enemy_group.update()
# #         self.enemy_group.draw(self.screen)
# #
# #         self.soul_group.update()
# #         self.soul_group.draw(self.screen)
# #
# #         self.hero.bullets.update()
# #         self.hero.bullets.draw(self.screen)
# #
# #         self.hero_group.update()
# #         self.hero_group.draw(self.screen)
# #         pass
# #
# #
# #     @staticmethod
# #     def __game_over():
# #         print("游戏结束")
# #         print(pygame.time.get_ticks())
# #
# #         pygame.quit()
# #         exit()
# #
# #
# #
# #
# #
# # if __name__ == '__main__':
# #
# #
# #     game = Plants_vs_Zombies()
# #     game.start_game()
#
#
#
# #
# #
# #
# #
# #
# #
# # import pygame
# #
# #
# # class Player(object):
# #     """
# #     player对象
# #     """
# #     def __init__(self):
# #         self.image = pygame.image.load("./植物大战僵尸素材/豌豆.png").convert_alpha()
# #         self.rect = self.image.get_rect()
# #         self.rect.midbottom = (100, screen_height - 130)
# #         self.vel_y = 0
# #         self.jumped = False
# #
# #     def update(self):
# #         x_move = 0
# #         y_move = 0
# #
# #         # 获取按键，并进行相应的移动
# #         key = pygame.key.get_pressed()
# #         if key[pygame.K_SPACE] and self.jumped is False:
# #             self.vel_y = -18
# #             self.jumped = True
# #         if not key[pygame.K_SPACE]:
# #             self.jumped = False
# #         if key[pygame.K_LEFT]:
# #             x_move -= 5
# #         if key[pygame.K_RIGHT]:
# #             x_move += 5
# #
# #         # 添加角色重力（跳跃之后自然下落）
# #         self.vel_y += 1.2
# #         if self.vel_y > 10:
# #             self.vel_y = 10
# #         y_move += self.vel_y
# #
# #         self.rect.x += x_move
# #         self.rect.y += y_move
# #
# #         # 控制人物的最低位置
# #         if self.rect.bottom > screen_height - 130:
# #             self.rect.bottom = screen_height - 130
# #
# #         # 绘制人物
# #         screen.blit(self.image, self.rect)
# #
# #
# # class Cloud(object):
# #     """
# #     云层对象
# #     """
# #     def __init__(self, x, y):
# #         self.image = pygame.image.load("./植物大战僵尸素材/).convert_alpha()
# #         self.rect = self.image.get_rect()
# #         self.rect.topleft = (x, y)
# #
# #     def update(self):
# #         self.rect.x -= 1  # 云层移动
# #         screen.blit(self.image, self.rect)
# #         if self.rect.x < -1400:  # 超出边界后重新在屏幕最右边绘制云层
# #             self.rect.x = 1400
# #
# #
# # # --------------------------------加载基本的窗口和时钟----------------------------
# # pygame.init()
# # screen_width = 1400
# # screen_height = 700
# # screen = pygame.display.set_mode((screen_width, screen_height))
# # pygame.display.set_caption('player_control')
# # clock = pygame.time.Clock()  # 设置时钟
# # # -------------------------------- 加载对象 ----------------------------------
# # bg = pygame.image.load("bg.png").convert()
# # player = Player()
# # cloud1 = Cloud(0, 0)
# # cloud2 = Cloud(1400, 0)
# #
# # # -------------------------------- 游戏主循环 ----------------------------------
# # run = True
# # while run:
# #     clock.tick(60)
# #     screen.blit(bg, (0, 0))
# #     # -------------------------------- 角色更新 ----------------------------------
# #     cloud1.update()
# #     cloud2.update()
# #     player.update()
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False
# #     # ------------------------------- 窗口更新并绘制 ------------------------------
# #     pygame.display.update()
# # pygame.quit()
#
#
# # import pygame
# #
# # jishiqi1 = pygame.USEREVENT
# # jishiqi2 = pygame.USEREVENT + 1
# # jishiqi3 = pygame.USEREVENT + 2
# # jishiqi4 = pygame.USEREVENT + 3
# #
# # SCREEN_RECT = pygame.Rect(0, 0, 1500, 920)
# #
# #
# # class Game(pygame.sprite.Sprite):
# #
# #     def __init__(self, image, life=0, speed=0):
# #         super(Game, self).__init__()
# #         self.image = image
# #         self.rect = self.image.get_rect()
# #         self.life = life
# #         self.speed = speed
# #
# #
# # class Background(Game):
# #
# #     # def __init__(self):
# #     #     super(Background, self).__init__(pygame.image.load("./植物大战僵尸素材/云端.png"))
# #
# #     def update(self):
# #         pass
# #
# # class User1(Game):
# #     power = 10
# #     fly_power = 200
# #     a = 0
# #
# #     def __init__(self):
# #         super().__init__(pygame.image.load("./植物大战僵尸素材/微信图片_20220220204424.jpg"))
# #         pygame.time.set_timer(jishiqi1, 1000)
# #         for event in pygame.event.get():
# #             if event.type == jishiqi1:
# #                 if User1.a == 4:
# #                     User1.a = 1
# #                 else:
# #                     User1.a += 1
# #         print(User1.a)
# #         if User1.a == 1:
# #             super().__init__(pygame.image.load("./植物大战僵尸素材/暴徒龙1.png"))
# #
# #         elif User1.a == 2:
# #             super().__init__(pygame.image.load("./植物大战僵尸素材/暴徒龙2.png"))
# #
# #         elif User1.a == 3:
# #             super().__init__(pygame.image.load("./植物大战僵尸素材/暴徒龙1.png"))
# #
# #         elif User1.a == 4:
# #             super().__init__(pygame.image.load("./植物大战僵尸素材/暴徒龙3.png"))
# #
# #         self.rect.centerx = SCREEN_RECT.centerx - 200
# #         self.rect.bottom = SCREEN_RECT.bottom - 200
# #         self.life = 2
# #         self.bullet = 2
# #         self.vel_y = 0
# #         self.bullets1 = pygame.sprite.Group()
# #
# #
# #
# #
# # class Main(object):
# #     def __init__(self):
# #         self.screen = pygame.display.set_mode(SCREEN_RECT.size)
# #         self.clock = pygame.time.Clock()
# #         self.__create_sprites()
# #
# #
# #     def __create_sprites(self): # 精灵组的创造
# #         bk = Background(pygame.image.load("./植物大战僵尸素材/云端.png"))
# #         self.background_group = pygame.sprite.Group(bk)
# #
# #
# #         self.user1 = User1()
# #         self.user1_group = pygame.sprite.Group(self.user1)
# #
# #         pass
# #
# #     def draw(self):
# #
# #         self.background_group.update()
# #         self.background_group.draw(self.screen)
# #
# #
# #         self.user1.bullets1.update()
# #         self.user1.bullets1.draw(self.screen)
# #
# #         self.user1_group.update()
# #         self.user1_group.draw(self.screen)
# #
# #     def start_game(self):
# #         print("开始啦")
# #         while True:
# #             self.clock.tick(60)
# #             self.draw()
# #             self.__event()
# #             pygame.display.update()
# #
# #
# #
# #     def __event(self):
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 Main.__game_over()
# #
# #
# #     @staticmethod
# #     def __game_over():
# #         print("游戏结束")
# #         pygame.quit()
# #         exit()
# #
# # if __name__ == '__main__':
# #     game = Main()
# #     game.start_game()
# #
#
# # a = open('./植物大战僵尸素材/暴徒龙1.png', 'r')
# # print(a)
# # a.close()
# #
# # def spritecollide(sprite, group, dokill, collided=None):
# #
# #     if dokill:
# #         crashed = []
# #         append = crashed.append
# #
# #         if collided:
# #             for s in group.sprites():
# #                 if collided(sprite, s):
# #                     s.kill()
# #                     append(s)
# #         else:
# #             spritecollide = sprite.rect.colliderect
# #             for s in group.sprites():
# #                 if spritecollide(s.rect):
# #                     s.kill()
# #                     append(s)
# #         return crashed
# #     elif collided:
# #         return [s for s in group if collided(sprite, s)]
# #     else:
# #         spritecollide = sprite.rect.colliderect
# #         return [s for s in group if spritecollide(s.rect)]
# #
# #
# #
# #
# # hero_crash_enemys = pygame.sprite.spritecollide(
# #             self.hero, self.enemy_sprite, True)
#
# #
# import time
# import pygame
#
# jishiqi = pygame.USEREVENT
# jishiqi2 = pygame.USEREVENT + 1
#
# SCREEN_RECT = pygame.Rect(0, 0, 1500, 920)
#
#
# class Game(pygame.sprite.Sprite):
#
#     def __init__(self, image, life=0, speed=0):
#         super(Game, self).__init__()
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.life = life
#         self.speed = speed
#
#
# class Background(Game):
#     # def __init__(self):
#     #     super(Background, self).__init__(pygame.image.load("./植物大战僵尸素材/云端.png"))
#
#     def update(self):
#         pass
#
#
# class User1_Big_blood(Game):
#     def __init__(self):
#         super(User1_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
#         self.rect.x = SCREEN_RECT.x + 30
#         self.rect.y = SCREEN_RECT.y
#
#     def update(self):
#         pass
#
#
# class User2_Big_blood(Game):
#     def __init__(self):
#         super(User2_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
#         self.rect.x = SCREEN_RECT.x + 1350
#         self.rect.y = SCREEN_RECT.y
#
#     def update(self):
#         pass
#
#
# class User1energy(Game):
#     def __init__(self):
#         super(User1energy, self).__init__(pygame.image.load("./植物大战僵尸素材/阳光.png"))
#         self.rect.x = SCREEN_RECT.x + 20
#         self.rect.y = SCREEN_RECT.y + 48
#
#     def update(self):
#         pass
#
#
# class User1energy_small(Game):
#     def __init__(self):
#         super(User1energy_small, self).__init__(pygame.image.load("./植物大战僵尸素材/小太阳.png"))
#         self.rect.x = SCREEN_RECT.x + 60
#         self.rect.y = SCREEN_RECT.y + 50
#
#     def update(self):
#         pass
#
#
# class User2energy(Game):
#     def __init__(self):
#         super(User2energy, self).__init__(pygame.image.load("./植物大战僵尸素材/大能量.png"))
#         self.rect.x = SCREEN_RECT.x + 1420
#         self.rect.y = SCREEN_RECT.y + 50
#
#     def update(self):
#         pass
#
#
# class User2energy_small(Game):
#     def __init__(self):
#         super(User2energy_small, self).__init__(pygame.image.load("./植物大战僵尸素材/小能量.png"))
#         self.rect.x = SCREEN_RECT.x + 1380
#         self.rect.y = SCREEN_RECT.y + 50
#
#     def update(self):
#         pass
#
#
# class User1_small_blood(Game):
#     def __init__(self):
#         super(User1_small_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/半管血.png"))
#         self.rect.x = SCREEN_RECT.x + 30
#         self.rect.y = SCREEN_RECT.y
#
#     def update(self):
#         pass
#
#
# class User2_small_blood(Game):
#     def __init__(self):
#         super(User2_small_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/半管血.png"))
#         self.rect.x = SCREEN_RECT.x + 1350
#         self.rect.y = SCREEN_RECT.y
#
#     def update(self):
#         pass
#
#
# class Nut(Game):
#     def __init__(self):
#         super(Nut, self).__init__(pygame.image.load("./植物大战僵尸素材/小坚果.gif"))
#         pass
#
#     def update(self):
#         super(Nut, self).update()
#         self.rect.y += 10
#         if self.rect.y >= 820:
#             self.rect.y = 820
#         if self.rect.y < 0:
#             self.rect.y = 0
#         elif self.rect.x > 1400:
#             self.rect.x = 1400
#         elif self.rect.x < 0:
#             self.rect.x = 0
#         elif 370 <= self.rect.y <= 450 and 200 <= self.rect.x <= 450:
#             self.rect.y = 390
#         elif 250 <= self.rect.y <= 300 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 270
#         pass
#
# class Fire_tree_bullet(Game):
#     def __init__(self):
#         super(Fire_tree_bullet, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬树子弹.gif"))
#         self.speed = 15
#         pass
#
#     def update(self):
#         super().update()
#         self.rect.x += self.speed
#         # 判断子弹飞出屏幕
#         if self.rect.x < 0 or self.rect.x > 1500:
#             self.kill()
#
# class DD_bullet1(Game):
#     def __init__(self):
#         super(DD_bullet1, self).__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
#         self.speed = 10
#         pass
#
#     def update(self):
#         super().update()
#         self.rect.x += self.speed
#         # 判断子弹飞出屏幕
#         if self.rect.x < 0 or self.rect.x > 1500:
#             self.kill()
#
# class DD_bullet2(Game):
#     def __init__(self):
#         super(DD_bullet2, self).__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
#         self.speed = 10
#         pass
#
#     def update(self):
#         super().update()
#         self.rect.x -= self.speed
#         # 判断子弹飞出屏幕
#         if self.rect.x < 0 or self.rect.x > 1500:
#             self.kill()
#
# class Fire_tree(Game):
#     def __init__(self):
#         super(Fire_tree, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬.gif"))
#         pass
#
#     def update(self):
#         super(Fire_tree, self).update()
#         self.rect.y += 10
#         if self.rect.y >= 820:
#             self.rect.y = 820
#         if self.rect.y < 0:
#             self.rect.y = 0
#         elif self.rect.x > 1400:
#             self.rect.x = 1400
#         elif self.rect.x < 0:
#             self.rect.x = 0
#         elif 370 <= self.rect.y <= 450 and 200 <= self.rect.x <= 450:
#             self.rect.y = 390
#         elif 250 <= self.rect.y <= 300 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 270
#         pass
#
# class Trigger1(Game):
#     def __init__(self):
#         super(Trigger1, self).__init__(pygame.image.load("./植物大战僵尸素材/透明画布.png"))
#         pass
#
#     def update(self):
#         pass
#
# class Trigger2(Game):
#     def __init__(self):
#         super(Trigger2, self).__init__(pygame.image.load("./植物大战僵尸素材/透明画布.png"))
#         pass
#
#     def update(self):
#         pass
#
# class User1(Game):
#     power = 0
#     fly_power = 200
#     power1 = 1
#     power2 = 1
#     fire_tree = Fire_tree()
#     trigger1 = Trigger1()
#     trigger2 = Trigger2()
#     aim = 0
#
#     def __init__(self):
#         super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"))
#         self.rect.centerx = SCREEN_RECT.centerx - 200
#         self.rect.bottom = SCREEN_RECT.bottom - 200
#         self.life = 2
#         self.bullet = 2
#         self.vel_y = 0
#         self.bullets1 = pygame.sprite.Group()
#         self.fire_trees = pygame.sprite.Group()
#         self.triggers1 = pygame.sprite.Group()
#         self.triggers2 = pygame.sprite.Group()
#         self.fire_bullets = pygame.sprite.Group()
#         self.nuts = pygame.sprite.Group()
#         self.ices = pygame.sprite.Group()
#         self.DD_bullets1 = pygame.sprite.Group()
#         self.DD_bullets2 = pygame.sprite.Group()
#
#     def update(self):
#
#         key = pygame.key.get_pressed()
#         if key[pygame.K_w] and User1.power >= 1:
#             self.vel_y = -22
#             User1.power -= 1
#
#         # 添加角色重力（跳跃之后自然下落）
#         # if key[pygame.K_k] and User1.fly_power >= 0:
#         #     # self.vel_y -= 0.1
#         #     # User1.fly_power -= 1
#         #     print(User1.fly_power)
#         #     pass
#         # if self.rect.y == 800:
#         #     pass
#         self.vel_y += 1
#         self.rect.y += self.vel_y
#         if self.rect.y >= 810:
#             self.rect.y = 810
#             self.vel_y = 0
#             User1.power = 10
#         if self.rect.y < 0:
#             self.rect.y = 0
#         elif self.rect.x > 1400:
#             self.rect.x = 1400
#         elif self.rect.x < 0:
#             self.rect.x = 0
#         elif 400 <= self.rect.y <= 420 and 200 <= self.rect.x <= 420:
#             self.rect.y = 400
#             self.vel_y = 0
#             User1.power = 7
#         elif 250 <= self.rect.y <= 280 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 250
#             self.vel_y = 0
#             User1.power = 7
#
#         key_operation = pygame.key.get_pressed()  # 返回元组
#         if key_operation[pygame.K_d]:
#             self.rect.x += 6
#             self.image = (pygame.image.load("./植物大战僵尸素材/豌豆.png"))
#             User1.aim = 0
#         elif key_operation[pygame.K_a]:
#             self.rect.x -= 6
#             self.image = (pygame.image.load("./植物大战僵尸素材/豌豆left.png"))
#             User1.aim = 1
#
#         pass
#
#     def fire(self):
#         bullet1 = Bullet1()
#         if User1.aim == 0:
#             bullet1.rect.centerx = self.rect.centerx + 28
#             bullet1.rect.centery = self.rect.centery - 20
#         elif User1.aim == 1:
#             bullet1.rect.centerx = self.rect.centerx + 28
#             bullet1.rect.centery = self.rect.centery - 20
#
#         self.bullets1.add(bullet1)
#         pass
#
#     def explosion(self):
#         User1.fire_tree.rect.centerx = self.rect.centerx + 80
#         User1.fire_tree.rect.centery = self.rect.centery
#         self.fire_trees.add(User1.fire_tree)
#
#     def tree_fire(self):
#         tree_bullet = Fire_tree_bullet()
#         tree_bullet.rect.centerx = User1.fire_tree.rect.centerx
#         tree_bullet.rect.centery = User1.fire_tree.rect.centery - 20
#         self.fire_bullets.add(tree_bullet)
#
#     def trigger_create1(self):
#         User1.trigger1.rect.centerx = self.rect.centerx
#         User1.trigger1.rect.centery = self.rect.centery - 20
#         self.triggers1.add(User1.trigger1)
#
#     def trigger_create2(self):
#         User1.trigger2.rect.centerx = self.rect.centerx
#         User1.trigger2.rect.centery = self.rect.centery - 20
#         self.triggers2.add(User1.trigger2)
#
#     def DD_bullet1(self):
#         dd_billet1 = DD_bullet1()
#         dd_billet1.rect.centery = User1.trigger1.rect.centery
#         dd_billet1.rect.centerx = User1.trigger1.rect.centerx
#         self.DD_bullets1.add(dd_billet1)
#
#     def DD_bullet2(self):
#         dd_billet2 = DD_bullet2()
#         dd_billet2.rect.centery = User1.trigger2.rect.centery
#         dd_billet2.rect.centerx = User1.trigger2.rect.centerx
#         self.DD_bullets2.add(dd_billet2)
#
#     def defence(self):
#         nut = Nut()
#         nut.rect.centerx = self.rect.centerx + 28
#         nut.rect.centery = self.rect.centery + 2
#         self.nuts.add(nut)
#
#     def attacked(self):
#         ice = Ice()
#         ice.rect.x = self.rect.centerx
#         ice.rect.y = -100
#         self.ices.add(ice)
#
#
# class User2(Game):
#     power = 0
#     power1 = 1
#     power2 = 3
#
#     # fly_power = 50
#
#     def __init__(self):
#         super().__init__(pygame.image.load("./植物大战僵尸素材//暴鲤鱼.png"))
#         self.rect.centerx = SCREEN_RECT.centerx + 200
#         self.rect.bottom = SCREEN_RECT.bottom - 200
#         self.life = 2
#         self.bullet = 2
#         self.vel_y = 0
#         self.bullets2 = pygame.sprite.Group()
#         self.energies = pygame.sprite.Group()
#
#     def update(self):
#         key1 = pygame.key.get_pressed()
#         if key1[pygame.K_UP] and User2.power >= 1:
#             self.vel_y = -22
#             User2.power -= 1
#
#         self.vel_y += 1
#         self.rect.y += self.vel_y
#         if self.rect.y >= 780:
#             self.rect.y = 780
#             self.vel_y = 0
#             User2.power = 10
#         if self.rect.y < 0:
#             self.rect.y = 0
#         elif self.rect.x > 1350:
#             self.rect.x = 1350
#         elif self.rect.x < 0:
#             self.rect.x = 0
#         elif 370 <= self.rect.y <= 400 and 200 <= self.rect.x <= 420:
#             self.rect.y = 370
#             self.vel_y = 0
#             User2.power = 7
#         elif 250 <= self.rect.y <= 280 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 250
#             self.vel_y = 0
#             User2.power = 7
#
#         key_operation2 = pygame.key.get_pressed()
#         if key_operation2[pygame.K_RIGHT]:
#             self.rect.x += 6
#         elif key_operation2[pygame.K_LEFT]:
#             self.rect.x -= 6
#
#     def fire(self):
#         bullet2 = Bullet2()
#         # 设置精灵位置
#         bullet2.rect.centerx = self.rect.centerx + 20
#         bullet2.rect.centery = self.rect.centery + 10
#
#         # 添加到精灵族
#         self.bullets2.add(bullet2)
#         pass
#
#     def attack(self):
#         energy = Attack()
#         energy.rect.centerx = self.rect.centerx + 20
#         energy.rect.centery = self.rect.centery + 10
#         self.energies.add(energy)
#         print(self.rect.x - energy.rect.x)
#         if self.rect.x - energy.rect.x >= 100:
#             energy.kill()
#
#
# class Ice(Game):
#     def __init__(self):
#         super(Ice, self).__init__(pygame.image.load("./植物大战僵尸素材//能量波.png"))
#         pass
#
#     def update(self):
#         super(Ice, self).update()
#         self.rect.y += 10
#         if self.rect.y >= 1000:
#             self.kill()
#
#
# class Attack(Game):
#     def __init__(self):
#         super(Attack, self).__init__(pygame.image.load("./植物大战僵尸素材//攻击波.png"))
#
#     def update(self):
#         super(Attack, self).update()
#         self.rect.x -= 20
#         pass
#
#
# class Bullet1(Game):
#     def __init__(self):
#         super().__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
#         self.speed = 10
#         pass
#
#     def update(self):
#         super().update()
#         # 判断子弹飞出屏幕
#         if User1.aim == 0:
#             self.rect.x += self.speed
#         else:
#             self.rect.x -= 10
#         if self.rect.x < 0 or self.rect.x > 1500:
#             self.kill()
#
#     def __del__(self):
#         pass
#
#
# class Bullet2(Game):
#     def __init__(self):
#         super().__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
#         self.speed = 10
#
#         pass
#
#     def update(self):
#         super().update()
#         self.rect.x -= self.speed
#         # 判断子弹飞出屏幕
#         if self.rect.x < 0 or self.rect.x > 1500:
#             self.kill()
#
#     def __del__(self):
#         pass
#
#
# class Main(object):
#     def __init__(self):
#         self.screen = pygame.display.set_mode(SCREEN_RECT.size)
#         self.clock = pygame.time.Clock()
#         self.__create_sprites()
#         pygame.display.set_caption("MyGame")
#         pygame.time.set_timer(jishiqi, 5000)
#         pygame.time.set_timer(jishiqi2, 50)
#         pass
#
#     def __create_sprites(self):  # 精灵组的创造
#         bk = Background(pygame.image.load("./植物大战僵尸素材/云端.png"))
#         self.background_group = pygame.sprite.Group(bk)
#
#         user1blood = User1_Big_blood()
#         self.user1blood = pygame.sprite.Group(user1blood)
#
#         user2blood = User2_Big_blood()
#         self.user2blood = pygame.sprite.Group(user2blood)
#
#         user1_small_blood = User1_small_blood()
#         self.user1_small = pygame.sprite.Group(user1_small_blood)
#
#         user2_small_blood = User2_small_blood()
#         self.user2_small = pygame.sprite.Group(user2_small_blood)
#
#         use1_energy = User1energy()
#         self.user1_energy = pygame.sprite.Group(use1_energy)
#
#         use2_energy = User2energy()
#         self.user2_energy = pygame.sprite.Group(use2_energy)
#
#         use1_energy_small = User1energy_small()
#         self.user1_energy_small = pygame.sprite.Group(use1_energy_small)
#
#         use2_energy_small = User2energy_small()
#         self.user2_energy_small = pygame.sprite.Group(use2_energy_small)
#
#         self.user1 = User1()
#         self.user1_group = pygame.sprite.Group(self.user1)
#
#         self.user2 = User2()
#         self.user2_group = pygame.sprite.Group(self.user2)
#
#         pass
#
#     def __event(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 Main.__game_over()
#
#             elif event.type == jishiqi:
#                 self.user1.bullet = 2
#                 self.user1.power1 = 1
#                 self.user1.power2 = 1
#
#                 self.user2.bullet = 2
#                 self.user2.power1 = 1
#                 self.user2.power2 = 3
#
#
#             elif self.user1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j and User1.aim == 0:
#                 self.user1.trigger_create1()
#                 self.user1.fire()
#                 self.user1.bullet -= 1
#
#             elif self.user1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j and User1.aim == 1:
#                 self.user1.trigger_create2()
#                 self.user1.fire()
#                 self.user1.bullet -= 1
#
#
#
#             elif self.user1.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_i:
#                 self.user1.explosion()
#                 self.user1.power1 -= 1
#
#             elif self.user1.power2 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_u:
#                 self.user1.power2 -= 1
#                 self.user1.defence()
#
#             elif self.user2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
#                 self.user2.fire()
#                 self.user2.bullet -= 1
#             elif self.user2.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP4:
#                 self.user1.attacked()
#                 self.user2.power1 -= 1
#             #
#             # elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP5:
#             #     self.user2.attack()
#
#         key2 = pygame.key.get_pressed()
#         if key2[pygame.K_KP5] and self.user2.power2 != 0:
#             self.user2.fire()
#             self.user2.power2 -= 1
#
#             pass
#
#     def draw(self):
#
#         self.background_group.update()
#         self.background_group.draw(self.screen)
#
#         if self.user1.life == 2:
#             self.user1blood.update()
#             self.user1blood.draw(self.screen)
#         else:
#             self.user1_small.update()
#             self.user1_small.draw(self.screen)
#
#         if self.user2.life == 2:
#             self.user2blood.update()
#             self.user2blood.draw(self.screen)
#         else:
#             self.user2_small.update()
#             self.user2_small.draw(self.screen)
#
#         if self.user1.power1 != 0:
#             self.user1_energy.update()
#             self.user1_energy.draw(self.screen)
#
#         if self.user1.power2 != 0:
#             self.user1_energy_small.update()
#             self.user1_energy_small.draw(self.screen)
#
#         if self.user2.power2 != 0:
#             self.user2_energy.update()
#             self.user2_energy.draw(self.screen)
#
#         if self.user2.power1 != 0:
#             self.user2_energy_small.update()
#             self.user2_energy_small.draw(self.screen)
#
#         self.user1.nuts.update()
#         self.user1.nuts.draw(self.screen)
#
#         self.user1.fire_trees.update()
#         self.user1.fire_trees.draw(self.screen)
#
#         self.user1.triggers1.update()
#         self.user1.triggers1.draw(self.screen)
#
#         self.user1.triggers2.update()
#         self.user1.triggers2.draw(self.screen)
#
#         self.user1.DD_bullets1.update()
#         self.user1.DD_bullets1.draw(self.screen)
#
#         self.user1.DD_bullets2.update()
#         self.user1.DD_bullets2.draw(self.screen)
#
#         self.user2.bullets2.update()
#         self.user2.bullets2.draw(self.screen)
#
#         self.user2.energies.update()
#         self.user2.energies.draw(self.screen)
#
#         self.user1.bullets1.update()
#         self.user1.bullets1.draw(self.screen)
#
#         self.user1.fire_bullets.update()
#         self.user1.fire_bullets.draw(self.screen)
#
#         self.user1.ices.update()
#         self.user1.ices.draw(self.screen)
#
#         self.user2_group.update()
#         self.user2_group.draw(self.screen)
#
#         self.user1_group.update()
#         self.user1_group.draw(self.screen)
#
#     # @staticmethod
#     # def colliseion_check(a, b):  # 碰撞检测
#     #     temp1 = (b.rect.x <= a.rect.centerx + 10 <= b.x + 10)
#     #     temp2 = (b.rect.y <= a.rect.centerx + 10 <= b.y + 10)
#
#     # def remark(self):
#     #     self.user2.life -= 1
#     #     pass
#
#     def crash(self):
#         pygame.sprite.groupcollide(self.user2.bullets2, self.user1.bullets1, True, True)
#         pygame.sprite.groupcollide(self.user1.fire_trees, self.user2.bullets2, True, True)
#         pygame.sprite.groupcollide(self.user1.nuts, self.user2.bullets2, True, True)
#
#         if pygame.sprite.spritecollide(self.user1, self.user2.bullets2, True):
#             if self.user1.life > 1:
#                 self.user1.life -= 1
#             else:
#                 time.sleep(1)
#                 pygame.quit()
#                 print('蓝龙胜!')
#                 time.sleep(3)
#                 exit()
#         elif pygame.sprite.spritecollide(self.user1, self.user1.ices, True):
#             if self.user1.life > 1:
#                 self.user1.life -= 1
#             else:
#                 time.sleep(1)
#                 pygame.quit()
#                 print('蓝龙胜!')
#                 time.sleep(3)
#                 exit()
#
#
#         elif pygame.sprite.spritecollide(self.user2, self.user1.bullets1, True):
#             if self.user2.life > 1:
#                 self.user2.life -= 1
#             else:
#                 print('豌豆胜!')
#                 time.sleep(1)
#                 pygame.quit()
#                 time.sleep(3)
#                 exit()
#         elif pygame.sprite.groupcollide(self.user1.fire_trees, self.user1.bullets1, False, True):
#             self.user1.tree_fire()
#
#         elif pygame.sprite.groupcollide(self.user1.triggers1, self.user1.bullets1, False, True):
#             self.user1.DD_bullet1()
#
#         elif pygame.sprite.groupcollide(self.user1.triggers2, self.user1.bullets1, False, True):
#             self.user1.DD_bullet2()
#
#
#         elif pygame.sprite.spritecollide(self.user2, self.user1.fire_bullets, True):
#             if self.user2.life > 1:
#                 self.user2.life -= 1
#             else:
#                 print('豌豆胜!')
#                 time.sleep(1)
#                 pygame.quit()
#                 time.sleep(3)
#                 exit()
#
#             pass
#
#     def start_game(self):
#         print("开始啦")
#         while True:
#             self.clock.tick(60)
#             self.draw()
#             self.__event()
#             self.crash()
#             pygame.display.update()
#
#     @staticmethod
#     def __game_over():
#         print("游戏结束")
#         pygame.quit()
#         exit()
#
#
# if __name__ == '__main__':
#     game = Main()
#     game.start_game()



# pygame.init()  # 初始化pygame类
# screen = pygame.display.set_mode((600, 800))  # 设置窗口大小
# pygame.display.set_caption('动画测试')  # 设置窗口标题
# image = pygame.image.load("./植物大战僵尸素材//豌豆.png")  # 加载图片，这里一定要正确填写图片路径，如果和py文件在同目录下则直接写文件名（带上文件类型）
# tick = pygame.time.Clock()
# frameNumber = 2 # 设置帧数，示例图片有6帧
# frameRect = image.get_rect()  # 获取全图的框体数据，以此计算单帧框体
# frameRect.width //= frameNumber  # 获取每一帧的边框数据，实例图片之只有一行，所以单帧高度和整体图片高度相等
# fps = 2  # 设置刷新率，数字越大刷新率越高，但因为示例图片只有6帧所以建议设低一点 否则闪的太凶。
# fcclock = pygame.time.Clock()
# n = 0  # 这算是一个magic number吧，是为了计算框体位置所引用的一个计算变量，实在懒得想名字了。
#
# while True:
#
#     for event in pygame.event.get():  # 事件检测，如果点击右上角X，则程序退出，没有这个循环的话，窗口可能会在打开时闪退。
#         if event.type == pygame.QUIT:
#             exit()
#     if n < frameNumber:
#         frameRect.x = frameRect.width * n  # 这里通过移动单帧矿体的x轴坐标实现单帧框体位移
#         n += 1
#     else:
#         n = 0
#
#     screen.fill((255, 255, 255))  # 设置背景为白色
#     screen.blit(image, (0, 0), frameRect)  # 这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
#     fcclock.tick(fps)  # 设置图像刷新率，如果刷新率太高，图像闪的太厉害
#     pygame.display.flip()  # 刷新窗口

# import pygame

# screen = pygame.display.set_mode(0, 0, 1500, 640)
# clock = pygame.time.Clock()
#
# while

#
# import pygame
#
# pygame.init()  # 初始化pygame类
# screen = pygame.display.set_mode((600, 800))  # 设置窗口大小
# pygame.display.set_caption('动画测试')  # 设置窗口标题
# image = pygame.image.load('./植物大战僵尸素材/少女转身.png')  # 加载图片，这里一定要正确填写图片路径，如果和py文件在同目录下则直接写文件名（带上文件类型）
# tick = pygame.time.Clock()
# frameNumber = 6  # 设置帧数，示例图片有6帧
# frameRect = image.get_rect()  # 获取全图的框体数据，以此计算单帧框体
# frameRect.width = frameRect.width//frameNumber  # 获取每一帧的边框数据，实例图片之只有一行，所以单帧高度和整体图片高度相等
# print(frameRect.width)
# fps = 6  # 设置刷新率，数字越大刷新率越高，但因为示例图片只有6帧所以建议设低一点 否则闪的太凶。
# fc_clock = pygame.time.Clock()
# n = 0  # 这算是一个magic number吧，是为了计算框体位置所引用的一个计算变量，实在懒得想名字了。
#
# while True:
#
#     for event in pygame.event.get():  # 事件检测，如果点击右上角X，则程序退出，没有这个循环的话，窗口可能会在打开时闪退。
#         if event.type == pygame.QUIT:
#             exit()
#     if n < frameNumber:
#         frameRect.x = frameRect.width * n  # 这里通过移动单帧矿体的x轴坐标实现单帧框体位移
#         n += 1
#     else:
#         n = 0
#
#     screen.fill((255, 255, 255))  # 设置背景为白色
#     screen.blit(image, (200, 200), frameRect)  # 这里给了3个实参，(分别是图像，绘制的位置，绘制的截面框)
#     fc_clock.tick(fps)  # 设置图像刷新率，如果刷新率太高，图像闪的太厉害
#     pygame.display.update() # 刷新窗口


import random
import sys
import pygame

jishiqi = pygame.USEREVENT
jishiqi2 = pygame.USEREVENT + 1

SCREEN_RECT = pygame.Rect(0, 0, 1500, 920)

class Game(pygame.sprite.Sprite):

    def __init__(self, image, life=0, speed=0):
        super(Game, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.life = life
        self.speed = speed

class Background(Game):
    def __init__(self):
        super(Background, self).__init__(pygame.image.load("./植物大战僵尸素材/云端.png"))

    def update(self):
        pass

class User1energy(Game):
    def __init__(self):
        super(User1energy, self).__init__(pygame.image.load("./植物大战僵尸素材/阳光.png"))
        self.rect.x = SCREEN_RECT.x + 20
        self.rect.y = SCREEN_RECT.y + 48

    def update(self):
        pass

class User1energy_small(Game):
    def __init__(self):
        super(User1energy_small, self).__init__(pygame.image.load("./植物大战僵尸素材/小太阳.png"))
        self.rect.x = SCREEN_RECT.x + 60
        self.rect.y = SCREEN_RECT.y + 50

    def update(self):
        pass

class User2energy(Game):
    def __init__(self):
        super(User2energy, self).__init__(pygame.image.load("./植物大战僵尸素材/大能量.png"))
        self.rect.x = SCREEN_RECT.x + 1420
        self.rect.y = SCREEN_RECT.y + 50

    def update(self):
        pass

class User2energy_small(Game):
    def __init__(self):
        super(User2energy_small, self).__init__(pygame.image.load("./植物大战僵尸素材/小能量.png"))
        self.rect.x = SCREEN_RECT.x + 1380
        self.rect.y = SCREEN_RECT.y + 50

    def update(self):
        pass

class User1_Big_blood(Game):
    def __init__(self):
        super(User1_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
        self.rect.x = SCREEN_RECT.x + 30
        self.rect.y = SCREEN_RECT.y

    def update(self):
        if User1.life == 5:
            self.image = pygame.image.load("./植物大战僵尸素材/一管血.png")
        elif User1.life == 4:
            self.image = pygame.image.load("./植物大战僵尸素材/四分之三管血.png")
        elif User1.life == 3:
            self.image = pygame.image.load("./植物大战僵尸素材/半管血.png")
        elif User1.life == 2:
            self.image = pygame.image.load("./植物大战僵尸素材/四分之一管血.png")
        elif User1.life == 1:
            self.image = pygame.image.load("./植物大战僵尸素材/一丝血.png")

        pass

class User2_Big_blood(Game):
    def __init__(self):
        super(User2_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
        self.rect.x = SCREEN_RECT.x + 1350
        self.rect.y = SCREEN_RECT.y

    def update(self):
        if User2.life == 5:
            self.image = pygame.image.load("./植物大战僵尸素材/一管血.png")
        elif User2.life == 4:
            self.image = pygame.image.load("./植物大战僵尸素材/四分之三管血.png")
        elif User2.life == 3:
            self.image = pygame.image.load("./植物大战僵尸素材/半管血.png")
        elif User2.life == 2:
            self.image = pygame.image.load("./植物大战僵尸素材/四分之一管血.png")
        elif User2.life == 1:
            self.image = pygame.image.load("./植物大战僵尸素材/一丝血.png")
        pass

class Nut(Game):
    def __init__(self):
        super(Nut, self).__init__(pygame.image.load("./植物大战僵尸素材/小坚果.gif"))
        pass

    def update(self):
        super(Nut, self).update()
        self.rect.y += 10
        if self.rect.y >= 830:
            self.rect.y = 830
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 1400:
            self.rect.x = 1400
        elif self.rect.x < 0:
            self.rect.x = 0
        elif 400 <= self.rect.y <= 430 and 200 <= self.rect.x <= 470:
            self.rect.y = 400
        elif 250 <= self.rect.y <= 300 and 1100 <= self.rect.x <= 1300:
            self.rect.y = 270
        pass

class Fire_tree_bullet1(Game):
    def __init__(self):
        super(Fire_tree_bullet1, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬树子弹.gif"))
        self.speed = 15
        pass

    def update(self):
        super().update()
        self.rect.x += self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

class Fire_tree_bullet2(Game):
    def __init__(self):
        super(Fire_tree_bullet2, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬树子弹1.png"))
        self.speed = 15
        pass

    def update(self):
        super().update()
        self.rect.x -= self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

class DD_bullet1(Game):
    def __init__(self):
        super(DD_bullet1, self).__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
        self.speed = 10
        pass

    def update(self):
        super().update()
        self.rect.x += self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

class DD_bullet2(Game):
    def __init__(self):
        super(DD_bullet2, self).__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
        self.speed = 10
        pass

    def update(self):
        super().update()
        self.rect.x -= self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

class LL_bullet1(Game):
    def __init__(self):
        super(LL_bullet1, self).__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
        self.speed = 10
        pass

    def update(self):
        super().update()
        self.rect.x += self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

class LL_bullet2(Game):
    def __init__(self):
        super(LL_bullet2, self).__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
        self.speed = 10
        pass

    def update(self):
        super().update()
        self.rect.x -= self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

class Fire_tree(Game):
    def __init__(self):
        super(Fire_tree, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬.gif"))
        pass

    def update(self):
        super(Fire_tree, self).update()
        self.rect.y += 10
        if self.rect.y >= 820:
            self.rect.y = 820
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 1400:
            self.rect.x = 1400
        elif self.rect.x < 0:
            self.rect.x = 0
        elif 400 <= self.rect.y <= 420 and 200 <= self.rect.x <= 450:
            self.rect.y = 400
        elif 260 <= self.rect.y <= 290 and 1100 <= self.rect.x <= 1300:
            self.rect.y = 260
        pass

class Trigger1(Game):
    def __init__(self):
        super(Trigger1, self).__init__(pygame.image.load("./植物大战僵尸素材/透明画布.png"))
        pass

    def update(self):
        pass

class Trigger2(Game):
    def __init__(self):
        super(Trigger2, self).__init__(pygame.image.load("./植物大战僵尸素材/透明画布.png"))
        pass

    def update(self):
        pass

class User1(Game):
    power = 0
    fly_power = 2
    bullet = 2
    power1 = 1
    power2 = 1
    fire_tree = Fire_tree()
    trigger1 = Trigger1()
    trigger2 = Trigger2()
    aim = 0
    life = 5

    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"))
        self.rect.centerx = SCREEN_RECT.centerx - 200
        self.rect.bottom = SCREEN_RECT.bottom - 200
        self.vel_y = 0
        self.bullets1 = pygame.sprite.Group()
        self.fire_trees = pygame.sprite.Group()
        self.triggers1 = pygame.sprite.Group()
        self.triggers2 = pygame.sprite.Group()
        self.fire_bullets = pygame.sprite.Group()
        self.nuts = pygame.sprite.Group()
        self.ices = pygame.sprite.Group()
        self.DD_bullets1 = pygame.sprite.Group()
        self.DD_bullets2 = pygame.sprite.Group()

    def update(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and User1.power >= 1:
            self.vel_y = -22
            User1.power -= 1
        self.vel_y += 1
        self.rect.y += self.vel_y
        if self.rect.y >= 810:
            self.rect.y = 810
            self.vel_y = 0
            User1.power = 10
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 1400:
            self.rect.x = 1400
        elif self.rect.x < 0:
            self.rect.x = 0
        elif 400 <= self.rect.y <= 430 and 200 <= self.rect.x <= 450:
            self.rect.y = 400
            self.vel_y = 0
            User1.power = 7
        elif 250 <= self.rect.y <= 280 and 1100 <= self.rect.x <= 1300:
            self.rect.y = 250
            self.vel_y = 0
            User1.power = 7

        pass

    def fire(self):
        bullet1 = Bullet1()
        bullet1.rect.centerx = self.rect.centerx
        bullet1.rect.centery = self.rect.centery - 20

        self.bullets1.add(bullet1)
        pass

    def explosion(self):
        if User1.aim == 0:
            User1.fire_tree.rect.centerx = self.rect.centerx + 80
            User1.fire_tree.rect.centery = self.rect.centery
        else:
            User1.fire_tree.rect.centerx = self.rect.centerx - 80
            User1.fire_tree.rect.centery = self.rect.centery
        self.fire_trees.add(User1.fire_tree)

    def tree_fire1(self):
        tree_bullet1 = Fire_tree_bullet1()
        tree_bullet1.rect.centerx = User1.fire_tree.rect.centerx
        tree_bullet1.rect.centery = User1.fire_tree.rect.centery - 20
        self.fire_bullets.add(tree_bullet1)

    def tree_fire2(self):
        tree_bullet2 = Fire_tree_bullet2()
        tree_bullet2.rect.centerx = User1.fire_tree.rect.centerx
        tree_bullet2.rect.centery = User1.fire_tree.rect.centery - 20
        self.fire_bullets.add(tree_bullet2)

    def trigger_create1(self):
        User1.trigger1.rect.centerx = self.rect.centerx
        User1.trigger1.rect.centery = self.rect.centery - 20
        self.triggers1.add(User1.trigger1)

    def trigger_create2(self):
        User1.trigger2.rect.centerx = self.rect.centerx
        User1.trigger2.rect.centery = self.rect.centery - 20
        self.triggers2.add(User1.trigger2)

    def DD_bullet1(self):
        dd_billet1 = DD_bullet1()
        dd_billet1.rect.centery = User1.trigger1.rect.centery
        dd_billet1.rect.centerx = User1.trigger1.rect.centerx
        self.DD_bullets1.add(dd_billet1)

    def DD_bullet2(self):
        dd_billet2 = DD_bullet2()
        dd_billet2.rect.centery = User1.trigger2.rect.centery
        dd_billet2.rect.centerx = User1.trigger2.rect.centerx
        self.DD_bullets2.add(dd_billet2)

    def defence(self):
        nut = Nut()
        if User1.aim == 0:
            nut.rect.centerx = self.rect.centerx + 42
            nut.rect.centery = self.rect.centery + 2
        else:
            nut.rect.centerx = self.rect.centerx - 42
            nut.rect.centery = self.rect.centery + 2
        self.nuts.add(nut)

    def attacked(self):
        ice = Ice()
        ice.rect.x = self.rect.centerx
        ice.rect.y = -100
        self.ices.add(ice)

class User2(Game):
    power = 0
    power1 = 1
    power2 = 3
    aim = 0
    bullet = 2
    trigger1 = Trigger1()
    trigger2 = Trigger2()
    life = 5
    fly_power = 2

    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材//暴鲤鱼.png"))
        self.rect.centerx = SCREEN_RECT.centerx + 200
        self.rect.bottom = SCREEN_RECT.bottom - 200
        self.vel_y = 0
        self.bullets2 = pygame.sprite.Group()
        self.energies = pygame.sprite.Group()
        self.triggers1 = pygame.sprite.Group()
        self.triggers2 = pygame.sprite.Group()
        self.LL_bullets1 = pygame.sprite.Group()
        self.LL_bullets2 = pygame.sprite.Group()

    def update(self):
        key1 = pygame.key.get_pressed()
        if key1[pygame.K_UP] and User2.power >= 1:
            self.vel_y = -22
            User2.power -= 1

        self.vel_y += 1
        self.rect.y += self.vel_y
        if self.rect.y >= 780:
            self.rect.y = 780
            self.vel_y = 0
            User2.power = 10
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 1350:
            self.rect.x = 1350
        elif self.rect.x < 0:
            self.rect.x = 0
        elif 370 <= self.rect.y <= 400 and 200 <= self.rect.x <= 420:
            self.rect.y = 370
            self.vel_y = 0
            User2.power = 7
        elif 250 <= self.rect.y <= 280 and 1100 <= self.rect.x <= 1300:
            self.rect.y = 250
            self.vel_y = 0
            User2.power = 7

    def fire(self):
        bullet2 = Bullet2()
        # 设置精灵位置
        bullet2.rect.centerx = self.rect.centerx
        bullet2.rect.centery = self.rect.centery
        # 添加到精灵族
        self.bullets2.add(bullet2)
        pass

    def attack(self):
        energy = Attack()
        energy.rect.centerx = self.rect.centerx + 20
        energy.rect.centery = self.rect.centery + 10
        self.energies.add(energy)
        print(self.rect.x - energy.rect.x)
        if self.rect.x - energy.rect.x >= 100:
            energy.kill()


    def trigger_create1(self):
        User2.trigger1.rect.centerx = self.rect.centerx
        User2.trigger1.rect.centery = self.rect.centery + 10
        self.triggers1.add(User2.trigger1)

    def trigger_create2(self):
        User2.trigger2.rect.centerx = self.rect.centerx
        User2.trigger2.rect.centery = self.rect.centery + 10
        self.triggers2.add(User2.trigger2)

    def LL_bullet1(self):
        ll_billet1 = LL_bullet1()
        ll_billet1.rect.centery = User2.trigger1.rect.centery
        ll_billet1.rect.centerx = User2.trigger1.rect.centerx
        self.LL_bullets1.add(ll_billet1)

    def LL_bullet2(self):
        ll_billet2 = LL_bullet2()
        ll_billet2.rect.centery = User2.trigger2.rect.centery
        ll_billet2.rect.centerx = User2.trigger2.rect.centerx
        self.LL_bullets2.add(ll_billet2)

class Ice(Game):
    def __init__(self):
        super(Ice, self).__init__(pygame.image.load("./植物大战僵尸素材//能量波.png"))
        pass

    def update(self):
        super(Ice, self).update()
        self.rect.y += 10
        if self.rect.y >= 1000:
            self.kill()

class Attack(Game):
    def __init__(self):
        super(Attack, self).__init__(pygame.image.load("./植物大战僵尸素材//攻击波.png"))

    def update(self):
        super(Attack, self).update()
        self.rect.x -= 20
        pass

class Bullet1(Game):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
        self.speed = 10
        pass

    def update(self):
        super().update()
        # 判断子弹飞出屏幕
        if User1.aim == 0:
            self.rect.x += self.speed
        else:
            self.rect.x -= 10
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

    def __del__(self):
        pass

class Bullet2(Game):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
        self.speed = 10

        pass

    def update(self):
        super().update()
        self.rect.x -= self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0 or self.rect.x > 1500:
            self.kill()

    def __del__(self):
        pass

class Drug(Game):
    def __init__(self):
        super(Drug, self).__init__(pygame.image.load("./植物大战僵尸素材/医药箱翅膀.png"))
        self.rect.x = random.randint(50, 1350)
        self.rect.y = 0
        pass

    def update(self):
        self.rect.y += 5
        if self.rect.y >= 1000:
            self.kill()

class Clear(Game):
    def __init__(self):
        super(Clear, self).__init__(pygame.image.load("./植物大战僵尸素材/清空画布.png"))
        self.rect.y = 0
        self.rect.x = 0
    def update(self):
        pass

class Main(object):
    begin = True

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.display.set_caption("MyGame")
        pygame.time.set_timer(jishiqi, 5000)
        pygame.time.set_timer(jishiqi2, 20000)
        pass

    def __create_sprites(self):  # 精灵组的创造
        bk = Background()
        self.background_group = pygame.sprite.Group(bk)

        self.clear_group = pygame.sprite.Group()

        user1blood = User1_Big_blood()
        self.user1blood = pygame.sprite.Group(user1blood)

        user2blood = User2_Big_blood()
        self.user2blood = pygame.sprite.Group(user2blood)

        self.drugs = pygame.sprite.Group()

        use1_energy = User1energy()
        self.user1_energy = pygame.sprite.Group(use1_energy)

        use2_energy = User2energy()
        self.user2_energy = pygame.sprite.Group(use2_energy)

        use1_energy_small = User1energy_small()
        self.user1_energy_small = pygame.sprite.Group(use1_energy_small)

        use2_energy_small = User2energy_small()
        self.user2_energy_small = pygame.sprite.Group(use2_energy_small)

        self.user1 = User1()
        self.user1_group = pygame.sprite.Group(self.user1)

        self.user2 = User2()
        self.user2_group = pygame.sprite.Group(self.user2)

        pass

    def __event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main.__game_over()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                User1.life = 5
                self.user1.power1 = 1
                self.user1.power2 = 1
                User2.life = 5
                self.user2.power1 = 1
                self.user2.power2 = 3
                self.user1.rect.x = 500
                self.user1.rect.y = 500
                self.user2.rect.x = 900
                self.user2.rect.y = 500
                clear = Clear()
                self.clear_group.add(clear)

                self.clear_group.update()
                self.clear_group.draw(self.screen)
                pygame.sprite.groupcollide(self.clear_group, self.user1.DD_bullets1, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user1.DD_bullets2, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user2.LL_bullets1, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user2.LL_bullets2, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user1.nuts, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user1.fire_trees, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user1.fire_bullets, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.drugs, False, True)
                pygame.sprite.groupcollide(self.clear_group, self.user1.ices, False, True)
                clear.kill()
                Main.begin = True

            elif event.type == jishiqi:
                self.user1.bullet = 2
                self.user1.power1 = 1
                self.user1.power2 = 1

                self.user2.bullet = 2
                self.user2.power1 = 1
                self.user2.power2 = 3

            elif event.type == jishiqi2:
                drug = Drug()
                self.drugs.add(drug)

            elif self.user1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j and User1.aim == 0:
                self.user1.trigger_create1()
                self.user1.fire()
                self.user1.bullet -= 1

            elif self.user1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j and User1.aim == 1:
                self.user1.trigger_create2()
                self.user1.fire()
                self.user1.bullet -= 1

            elif self.user1.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.user1.explosion()
                self.user1.power1 -= 1

            elif self.user1.power2 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                self.user1.power2 -= 1
                self.user1.defence()

            elif self.user2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 and User2.aim == 1:
                self.user2.trigger_create1()
                self.user2.fire()
                self.user2.bullet -= 1

            elif self.user2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 and User2.aim == 0:
                self.user2.trigger_create2()
                self.user2.fire()
                self.user2.bullet -= 1

            elif self.user2.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP4:
                self.user1.attacked()
                self.user2.power1 -= 1

        key2 = pygame.key.get_pressed()
        if key2[pygame.K_KP5] and self.user2.power2 != 0 and User2.aim == 0:
            self.user2.trigger_create2()
            self.user2.fire()
            self.user2.power2 -= 1

        elif key2[pygame.K_KP5] and self.user2.power2 != 0 and User2.aim == 1:
            self.user2.trigger_create1()
            self.user2.fire()
            self.user2.power2 -= 1

        key_operation = pygame.key.get_pressed()  # 返回元组
        if key_operation[pygame.K_d]:
            self.user1.rect.x += 6
            self.user1.image = (pygame.image.load("./植物大战僵尸素材/豌豆.png"))
            User1.aim = 0
        elif key_operation[pygame.K_a]:
            self.user1.rect.x -= 6
            self.user1.image = (pygame.image.load("./植物大战僵尸素材/豌豆left.png"))
            User1.aim = 1

        key_operation2 = pygame.key.get_pressed()
        if key_operation2[pygame.K_RIGHT]:
            self.user2.rect.x += 6
            self.user2.image = pygame.image.load("./植物大战僵尸素材//暴鲤鱼left.png")
            User2.aim = 1
        elif key_operation2[pygame.K_LEFT]:
            self.user2.rect.x -= 6
            self.user2.image = pygame.image.load("./植物大战僵尸素材//暴鲤鱼.png")
            User2.aim = 0

            pass

    def draw(self):

        self.background_group.update()
        self.background_group.draw(self.screen)

        # if self.user1.life == 2:
        self.user1blood.update()
        self.user1blood.draw(self.screen)

        self.user2blood.update()
        self.user2blood.draw(self.screen)

        if self.user1.power1 != 0:
            self.user1_energy.update()
            self.user1_energy.draw(self.screen)

        if self.user1.power2 != 0:
            self.user1_energy_small.update()
            self.user1_energy_small.draw(self.screen)

        if self.user2.power2 != 0:
            self.user2_energy.update()
            self.user2_energy.draw(self.screen)

        if self.user2.power1 != 0:
            self.user2_energy_small.update()
            self.user2_energy_small.draw(self.screen)

        self.user1.nuts.update()
        self.user1.nuts.draw(self.screen)

        self.user1.fire_trees.update()
        self.user1.fire_trees.draw(self.screen)

        self.user1.triggers1.update()
        self.user1.triggers1.draw(self.screen)

        self.user1.triggers2.update()
        self.user1.triggers2.draw(self.screen)

        self.user1.DD_bullets1.update()
        self.user1.DD_bullets1.draw(self.screen)

        self.user1.DD_bullets2.update()
        self.user1.DD_bullets2.draw(self.screen)

        self.user2.triggers1.update()
        self.user1.triggers1.draw(self.screen)

        self.user2.triggers2.update()
        self.user1.triggers2.draw(self.screen)

        self.drugs.update()
        self.drugs.draw(self.screen)

        self.user2.LL_bullets1.update()
        self.user2.LL_bullets1.draw(self.screen)

        self.user2.LL_bullets2.update()
        self.user2.LL_bullets2.draw(self.screen)


        self.user2.bullets2.update()
        self.user2.bullets2.draw(self.screen)

        self.user2.energies.update()
        self.user2.energies.draw(self.screen)

        self.user1.bullets1.update()
        self.user1.bullets1.draw(self.screen)

        self.user1.fire_bullets.update()
        self.user1.fire_bullets.draw(self.screen)

        self.user1.ices.update()
        self.user1.ices.draw(self.screen)

        self.user2_group.update()
        self.user2_group.draw(self.screen)

        self.user1_group.update()
        self.user1_group.draw(self.screen)


    # @staticmethod
    # def colliseion_check(a, b):  # 碰撞检测
    #     temp1 = (b.rect.x <= a.rect.centerx + 10 <= b.x + 10)
    #     temp2 = (b.rect.y <= a.rect.centerx + 10 <= b.y + 10)

    # def remark(self):
    #     self.user2.life -= 1
    #     pass

    def crash(self):
        pygame.sprite.groupcollide(self.user2.LL_bullets2, self.user1.DD_bullets1, True, True)
        pygame.sprite.groupcollide(self.user2.LL_bullets1, self.user1.DD_bullets1, True, True)
        pygame.sprite.groupcollide(self.user2.LL_bullets2, self.user1.DD_bullets2, True, True)
        pygame.sprite.groupcollide(self.user2.LL_bullets1, self.user1.DD_bullets2, True, True)
        pygame.sprite.groupcollide(self.user1.fire_trees, self.user2.LL_bullets1, True, True)
        pygame.sprite.groupcollide(self.user1.nuts, self.user2.LL_bullets1, True, True)
        pygame.sprite.groupcollide(self.user1.fire_trees, self.user2.LL_bullets2, True, True)
        pygame.sprite.groupcollide(self.user1.nuts, self.user2.LL_bullets2, True, True)


        if pygame.sprite.spritecollide(self.user1, self.user2.LL_bullets1, True):
            if User1.life > 1:
                User1.life -= 1
            else:
                font_name = pygame.font.match_font('fangsong')
                font = pygame.font.Font(font_name, 62)
                text = font.render('蓝龙WIN!', True, 'black')
                self.screen.blit(text, (650, 400))
                pygame.display.update()
                Main.begin = False
        elif pygame.sprite.spritecollide(self.user1, self.user2.LL_bullets2, True):
            if User1.life > 1:
                User1.life -= 1
            else:
                font_name = pygame.font.match_font('fangsong')
                font = pygame.font.Font(font_name, 62)
                text = font.render('蓝龙WIN!', True, 'black')
                self.screen.blit(text, (650, 400))
                pygame.display.update()
                Main.begin = False
        elif pygame.sprite.spritecollide(self.user1, self.user1.ices, True):
            if User1.life > 1:
                User1.life -= 1
            else:
                font_name = pygame.font.match_font('fangsong')
                font = pygame.font.Font(font_name, 62)
                text = font.render('蓝龙WIN!', True, 'black')
                self.screen.blit(text, (650, 400))
                pygame.display.update()
                Main.begin = False
        elif pygame.sprite.spritecollide(self.user2, self.user1.DD_bullets1, True) or pygame.sprite.spritecollide(self.user2, self.user1.DD_bullets2, True):
            if User2.life > 1:
                User2.life -= 1
            else:
                font_name = pygame.font.match_font('fangsong')
                font = pygame.font.Font(font_name, 62)
                text = font.render('豌豆WIN!', True, 'black')
                self.screen.blit(text, (650, 400))
                pygame.display.update()
                Main.begin = False
        elif pygame.sprite.groupcollide(self.user1.fire_trees, self.user1.DD_bullets1, False, True):
            self.user1.tree_fire1()

        elif pygame.sprite.groupcollide(self.user1.fire_trees, self.user1.DD_bullets2, False, True):
            self.user1.tree_fire2()

        elif pygame.sprite.groupcollide(self.user1.triggers1, self.user1.bullets1, False, True):
            self.user1.DD_bullet1()
            self.user1.trigger1.kill()

        elif pygame.sprite.groupcollide(self.user1.triggers2, self.user1.bullets1, False, True):
            self.user1.DD_bullet2()
            self.user1.trigger2.kill()

        elif pygame.sprite.groupcollide(self.user2.triggers1, self.user2.bullets2, False, True):
            self.user2.LL_bullet1()
            self.user2.trigger1.kill()


        elif pygame.sprite.groupcollide(self.user2.triggers2, self.user2.bullets2, False, True):
            self.user2.LL_bullet2()
            self.user2.trigger2.kill()

        elif pygame.sprite.spritecollide(self.user2, self.user1.fire_bullets, True):
            if User2.life > 1:
                User2.life -= 1
            else:
                font_name = pygame.font.match_font('fangsong')
                font = pygame.font.Font(font_name, 62)
                text = font.render('豌豆WIN!', True, 'black')
                self.screen.blit(text, (650, 400))
                pygame.display.update()
                Main.begin = False
        elif pygame.sprite.spritecollide(self.user2, self.drugs, True):
            if User2.life < 4:
                User2.life += 2
            elif User2.life == 4:
                User2.life += 1

        elif pygame.sprite.spritecollide(self.user1, self.drugs, True):
            if User1.life < 4:
                User1.life += 2
            elif User1.life == 4:
                User1.life += 1
            pass

    def start_game(self):
        print("开始啦")
        pygame.init()
        while True:
            self.clock.tick(60)
            self.draw()
            self.__event()
            self.crash()
            if Main.begin is True:
                pygame.display.update()
            # else:a
            #     pass


    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Main()
    game.start_game()





