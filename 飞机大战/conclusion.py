
import time
import random
import pygame

jishiqi = pygame.USEREVENT + 5

SCREEN_RECT = pygame.Rect(0, 0, 1500, 920)


class Game(pygame.sprite.Sprite):

    def __init__(self, image, life=0, speed=0):
        super(Game, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.life = life
        self.speed = speed


class Background1(Game):
    def __init__(self):
        super(Background1, self).__init__(pygame.image.load("./植物大战僵尸素材/战地背景1.png"))

    def update(self):
        pass


class User1_Big_blood(Game):
    def __init__(self):
        super(User1_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
        self.rect.x = SCREEN_RECT.x + 30
        self.rect.y = SCREEN_RECT.y

    def update(self):
        pass


class User2_Big_blood(Game):
    def __init__(self):
        super(User2_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
        self.rect.x = SCREEN_RECT.x + 1350
        self.rect.y = SCREEN_RECT.y

    def update(self):
        pass


class User1_small_blood(Game):
    def __init__(self):
        super(User1_small_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/半管血.png"))
        self.rect.x = SCREEN_RECT.x + 30
        self.rect.y = SCREEN_RECT.y

    def update(self):
        pass


class User2_small_blood(Game):
    def __init__(self):
        super(User2_small_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/半管血.png"))
        self.rect.x = SCREEN_RECT.x + 1350
        self.rect.y = SCREEN_RECT.y

    def update(self):
        pass


class User1(Game):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/暴龙.png"))
        self.rect.centerx = SCREEN_RECT.centerx - 200
        self.rect.bottom = SCREEN_RECT.bottom - 200
        self.life = 2
        self.bullet = 2

        self.bullets1 = pygame.sprite.Group()

    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 1400:
            self.rect.x = 1400
        elif self.rect.x < 100:
            self.rect.x = 100
        elif self.rect.y > 850:
            self.rect.y = 850
        pass

    def fire(self):
        bullet1 = Bullet1()

        bullet1.rect.centerx = self.rect.centerx + 28
        bullet1.rect.centery = self.rect.centery + 2

        self.bullets1.add(bullet1)
        pass


class User2(Game):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/超级豌豆射手.png"))
        self.rect.centerx = SCREEN_RECT.centerx + 200
        self.rect.bottom = SCREEN_RECT.bottom - 200
        self.life = 2
        self.bullet = 2

        self.bullets2 = pygame.sprite.Group()

    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 1400:
            self.rect.x = 1400
        elif self.rect.x < 100:
            self.rect.x = 100
        elif self.rect.y > 850:
            self.rect.y = 850
        pass

    def fire(self):
        bullet2 = Bullet2()
        # 设置精灵位置
        bullet2.rect.centerx = self.rect.centerx + 20
        bullet2.rect.centery = self.rect.centery - 12

        # 添加到精灵族
        self.bullets2.add(bullet2)
        pass


class Bullet1(Game):
    def __init__(self):
        super().__init__(pygame.image.load("./植物大战僵尸素材/蓝色子弹.png"))
        self.speed = 10

        pass

    def update(self):
        super().update()
        self.rect.x += self.speed
        # 判断子弹飞出屏幕
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


class Main(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(jishiqi, 2000)

    def __create_sprites(self):  # 精灵组的创造
        bk = Background1()
        self.background_group = pygame.sprite.Group(bk)

        user1blood = User1_Big_blood()
        self.user1blood = pygame.sprite.Group(user1blood)

        user2blood = User2_Big_blood()
        self.user2blood = pygame.sprite.Group(user2blood)

        user1_small_blood = User1_small_blood()
        self.user1_small = pygame.sprite.Group(user1_small_blood)

        user2_small_blood = User2_small_blood()
        self.user2_small = pygame.sprite.Group(user2_small_blood)

        self.user1 = User1()
        self.user1_group = pygame.sprite.Group(self.user1)

        self.user2 = User2()
        self.user2_group = pygame.sprite.Group(self.user2)
        pass

    def __event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main.__game_over()

            elif event.type == jishiqi:
                self.user2.bullet = 2
                self.user1.bullet = 2

            elif self.user1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j:
                self.user1.fire()
                self.user1.bullet -= 1

            elif self.user2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
                self.user2.fire()
                self.user2.bullet -= 1

            pass
        key_operation = pygame.key.get_pressed()  # 返回元组
        if key_operation[pygame.K_w]:  # 索引为1 表示按下
            self.user1.rect.y -= 6
        elif key_operation[pygame.K_s]:
            self.user1.rect.y += 6
        elif key_operation[pygame.K_d]:
            self.user1.rect.x += 6
        elif key_operation[pygame.K_a]:
            self.user1.rect.x -= 6
        key_operation2 = pygame.key.get_pressed()
        if key_operation2[pygame.K_UP]:
            self.user2.rect.y -= 6
        elif key_operation2[pygame.K_DOWN]:
            self.user2.rect.y += 6
        elif key_operation2[pygame.K_RIGHT]:
            self.user2.rect.x += 6
        elif key_operation2[pygame.K_LEFT]:
            self.user2.rect.x -= 6

    def draw(self):

        self.background_group.update()
        self.background_group.draw(self.screen)

        if self.user1.life == 2:
            self.user1blood.update()
            self.user1blood.draw(self.screen)
        else:
            self.user1_small.update()
            self.user1_small.draw(self.screen)

        if self.user2.life == 2:
            self.user2blood.update()
            self.user2blood.draw(self.screen)
        else:
            self.user2_small.update()
            self.user2_small.draw(self.screen)

        self.user2.bullets2.update()
        self.user2.bullets2.draw(self.screen)

        self.user2_group.update()
        self.user2_group.draw(self.screen)

        self.user1.bullets1.update()
        self.user1.bullets1.draw(self.screen)

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
        pygame.sprite.groupcollide(self.user2.bullets2, self.user1.bullets1, True, True)
        if pygame.sprite.spritecollide(self.user1, self.user2.bullets2, True):
            if self.user1.life > 1:
                self.user1.life -= 1
            else:
                pygame.quit()
                print('豌豆胜!')
                time.sleep(3)
                exit()


        elif pygame.sprite.spritecollide(self.user2, self.user1.bullets1, True):
            if self.user2.life > 1:
                self.user2.life -= 1
            else:
                print('黑龙胜!')
                pygame.quit()
                time.sleep(3)
                exit()

            # if Main.colliseion_check(self.user1,self.user2.bullets2):
            pass

    def start_game(self):
        print("开始啦")
        while True:
            self.clock.tick(60)
            self.draw()
            self.__event()
            self.crash()
            pygame.display.update()

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()








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
        self.WZ = random.randint(0,4)
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
        pygame.time.set_timer(CRTATE_ENEMT_EVENT,1000) # 定时器常量＋毫秒
        pygame.time.set_timer(CRTATE_ENEMT_EVENT1,10000)
        pygame.time.set_timer(CRTATE_ENEMT_EVENT2,3000)
        pygame.time.set_timer(CRTATE_ENEMT_EVENT3,800)
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
    pygame.init()
    # test =
    a = int(input('选择你的游戏 1为双人小游戏 2为植物大战僵尸：'))
    # screen1 = pygame.display.set_mode(SCREEN_RECT.size)
    # choose = pygame.image.load('./植物大战僵尸素材/地图(2).jpg').convert()
    # def main():
    #     while 1:
    #         screen1.blit(choose,(0,0))
    #         pygame.display.update()
    #         for events in pygame.event.get():
    #             if events.type == pygame.QUIT:
    #                 sys.exit()
    #             elif events.type == pygame.MOUSEBUTTONDOWN:
    #                 a = pygame.mouse.get_pressed()
    #                 if
    #
    # main()
    try:
        if a == 1:
            game1 = Main()
            game1.start_game()
        elif a == 2:
            game2 = Plants_vs_Zombies()
            game2.start_game()
    except Exception as result:
        print('输入错了噢')
