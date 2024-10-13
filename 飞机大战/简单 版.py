import time
import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,1500,640)

CRTATE_ENEMT_EVENT = pygame.USEREVENT
CRTATE_SOUL = pygame.USEREVENT + 1
CRTATE_ENEMT_EVENT1 = pygame.USEREVENT+2
CRTATE_ENEMT_EVENT2 = pygame.USEREVENT+3
CRTATE_ENEMT_EVENT3 = pygame.USEREVENT+4


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name,WZ=0,speed=1):
        super(GameSprite, self).__init__()  # 需要主动调用父类代码
        # 定义图像属性
        self.image = image_name
        self.rect = self.image.get_rect()  # 和图像大小一致
        self.speed = speed
        self.WZ = WZ

    # def update(self):
    #     self.rect.x -= self.speed

class Background(GameSprite):
    def update(self):
        # super().update()
        pass

class Enemy(GameSprite):
    def __init__(self):
        # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
        super().__init__(pygame.image.load("./植物大战僵尸素材/鬼蜡烛.gif"))
        self.WZ = random.randint(0, 4)
        self.speed = random.randint(1,2)
        # 敌机位置 bottom（顶部） right(最右边)
        self.rect.x = SCREEN_RECT.width
        # max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = 20+self.WZ*110

    def update(self):
        self.rect.x -= self.speed
        # 保持飞行水平
        if self.rect.x <= 200:
            print('游戏结束')
            pygame.quit()
            print('你的得分是%s' % pygame.time.get_ticks())
            time.sleep(5)
            exit()

            # 移除精灵组
            # self.kill()

    def __del__(self):
        pass

class Enemy1(GameSprite):
    def __init__(self):
        # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
        super().__init__(pygame.image.load("./植物大战僵尸素材/黑龙.gif"))
        self.WZ = random.randint(0,4)
        self.speed = random.randint(4,10)
        # 敌机位置 bottom（顶部） right(最右边)
        self.rect.x = SCREEN_RECT.width
        # max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = 20+self.WZ*110

    def update(self):
        self.rect.x -= self.speed
        # 保持飞行水平
        if self.rect.x <= 200:
            print('游戏结束')
            pygame.quit()
            print('你的得分是%s' % pygame.time.get_ticks())
            time.sleep(5)
            exit()

            # 移除精灵组
            # self.kill()

    def __del__(self):
        pass

class Enemy2(GameSprite):
    def __init__(self):
        # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
        super().__init__(pygame.image.load("./植物大战僵尸素材/黑幽灵.gif"))
        self.WZ = random.randint(0,4)
        self.speed = 4
        # 敌机位置 bottom（顶部） right(最右边)
        self.rect.x = SCREEN_RECT.width
        # max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = 20+self.WZ*110

    def update(self):
        self.rect.x -= self.speed
        # 保持飞行水平
        if self.rect.x <= 200:
            print('游戏结束')
            pygame.quit()
            print('你的得分是%s' % pygame.time.get_ticks())
            time.sleep(5)
            exit()

            # 移除精灵组
            # self.kill()

    def __del__(self):
        pass

class Enemy3(GameSprite):
    def __init__(self):
        # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
        super().__init__(pygame.image.load("./植物大战僵尸素材/普通僵尸.gif"))
        self.WZ = random.randint(0,4)
        self.speed = 1
        # 敌机位置 bottom（顶部） right(最右边)
        self.rect.x = SCREEN_RECT.width
        # max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = 20+self.WZ*110

    def update(self):
        self.rect.x -= self.speed
        # 保持飞行水平
        if self.rect.x <= 200:
            print('游戏结束')
            pygame.quit()
            print('你的得分是%s' % pygame.time.get_ticks())
            time.sleep(5)
            exit()

            # 移除精灵组
            # self.kill()

    def __del__(self):
        pass

class Soul(GameSprite):
    def __init__(self):
        # 创造敌机精灵 指定敌机图片  # 指定敌机初始速度
        super().__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
        self.speed = random.randint(1,8)
        # 敌机位置 bottom（顶部） right(最右边)
        self.rect.x = SCREEN_RECT.width
        # max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = random.randint(0,640)

    def update(self):
        self.rect.x -= self.speed
        # 保持飞行水平
        if self.rect.x <= 0:
            self.kill()

    def __del__(self):
        pass

class Hero(GameSprite):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"))
        self.rect.centerx = SCREEN_RECT.centerx-200
        self.rect.bottom = SCREEN_RECT.bottom-250

        # 创建子弹精灵组 因为子弹发射属于hero
        self.bullets = pygame.sprite.Group()


    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 975:
            self.rect.x = 975
        elif self.rect.x < 250:
            self.rect.x = 250
        elif self.rect.y > 540:
            self.rect.y = 540

    def fire(self):
        # 创建子弹精灵
        bullet = Bullet()
        # 设置精灵位置
        bullet.rect.centerx = self.rect.centerx + 25
        bullet.rect.centery = self.rect.centery - 22


        # 添加到精灵族
        self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/子弹.png"))
        self.speed = 10
        pass

    def update(self):
        super().update()
        self.rect.x += self.speed
        # 判断子弹飞出屏幕
        if self.rect.x < 0:
            self.kill()

        pass

    def __del__(self):
        pass

class Plants_vs_Zombies(object):


    def __init__(self):
        print("初始化")

        # 1.创造游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size) # size为元组
        # bj = pygame.image.load("./植物大战僵尸素材/地图(2).jpg")
        # self.screen.blit(bj, (0, 0))
        # 2.创造游戏时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 设置定时器事件
        pygame.time.set_timer(CRTATE_ENEMT_EVENT, 1000) # 定时器常量＋毫秒
        pygame.time.set_timer(CRTATE_ENEMT_EVENT1, 10000)
        pygame.time.set_timer(CRTATE_ENEMT_EVENT2, 3000)
        pygame.time.set_timer(CRTATE_ENEMT_EVENT3, 800)
        pygame.time.set_timer(CRTATE_SOUL, 2000)

    def __create_sprites(self):
        BJ = Background(pygame.image.load("./植物大战僵尸素材/地图(2).jpg"))
        self.back_group = pygame.sprite.Group(BJ)
        self.enemy_group = pygame.sprite.Group()
        self.soul_group = pygame.sprite.Group()

        self.enemy_group1 = pygame.sprite.Group()
        self.enemy_group2 = pygame.sprite.Group()
        self.enemy_group3 = pygame.sprite.Group()
        # 创造豌豆精灵和精灵族
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        pass


    def start_game(self):
        print("游戏开始>>>>>>")
        while True:
            # 1，设置刷新
            self.clock.tick(60)
            # 2，事件监听
            self.__event_handler()
            # 3，碰撞测试
            self.__check_collide()
            # 4，更新绘制精灵
            self.__update_sprites()
            # 5，更新显示
            pygame.display.update()

            pass

    def __event_handler(self):# 2，事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Plants_vs_Zombies.__game_over()
            elif event.type == CRTATE_ENEMT_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == CRTATE_ENEMT_EVENT1:
                enemy1 = Enemy1()
                self.enemy_group1.add(enemy1)
            elif event.type == CRTATE_ENEMT_EVENT2:
                enemy2 = Enemy2()
                self.enemy_group2.add(enemy2)
            elif event.type == CRTATE_ENEMT_EVENT3:
                enemy3 = Enemy3()
                self.enemy_group3.add(enemy3)
            elif event.type == CRTATE_SOUL:
                soul = Soul()
                self.soul_group.add(soul)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            #     print("www") # 这样子只能记录单次按下 不能记录长按
        pass
        key_operation = pygame.key.get_pressed() #返回元组
        if key_operation[pygame.K_w]: # 索引为1 表示按下
            self.hero.rect.y -= 5
        elif key_operation[pygame.K_s]:
            self.hero.rect.y += 5
        elif key_operation[pygame.K_d]:
            self.hero.rect.x += 5
        elif key_operation[pygame.K_a]:
            self.hero.rect.x -= 5


    def __check_collide(self):# 3，碰撞测试
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group1, True, True)
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group2, True, True)
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group3, True, True)
        # 子弹和僵尸 True代表俩者都会被消除
        if ((pygame.sprite.spritecollide(self.hero,self.enemy_group,True) or
            (pygame.sprite.spritecollide(self.hero,self.enemy_group1,True)) or
            (pygame.sprite.spritecollide(self.hero, self.enemy_group2, True)) or
            (pygame.sprite.spritecollide(self.hero, self.enemy_group3, True)) or
            (pygame.sprite.spritecollide(self.hero, self.soul_group, True)))):
            print('游戏结束')
            pygame.quit()
            print('你的得分是%s' % pygame.time.get_ticks())
            time.sleep(5)
            exit()


        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.soul_group.update()
        self.soul_group.draw(self.screen)

        self.enemy_group1.update()
        self.enemy_group1.draw(self.screen)

        self.enemy_group2.update()
        self.enemy_group2.draw(self.screen)

        self.enemy_group3.update()
        self.enemy_group3.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)
        pass


    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        print('你的得分是%s' % pygame.time.get_ticks())
        time.sleep(5)
        exit()



if __name__ == '__main__':


    game = Plants_vs_Zombies()
    game.start_game()


