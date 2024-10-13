# import random
# import sys
# import pygame
#
# jishiqi = pygame.USEREVENT
# jishiqi2 = pygame.USEREVENT + 1
#
# SCREEN_RECT = pygame.Rect(0, 0, 1500, 920)
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
# class Background(Game):
#     def __init__(self):
#         super(Background, self).__init__(pygame.image.load("./植物大战僵尸素材/云端2.png"))
#
#     def update(self):
#         pass
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
# class User1energy_small(Game):
#     def __init__(self):
#         super(User1energy_small, self).__init__(pygame.image.load("./植物大战僵尸素材/小太阳.png"))
#         self.rect.x = SCREEN_RECT.x + 60
#         self.rect.y = SCREEN_RECT.y + 50
#
#     def update(self):
#         pass
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
# class User2energy_small(Game):
#     def __init__(self):
#         super(User2energy_small, self).__init__(pygame.image.load("./植物大战僵尸素材/小能量.png"))
#         self.rect.x = SCREEN_RECT.x + 1380
#         self.rect.y = SCREEN_RECT.y + 50
#
#     def update(self):
#         pass
#
# class User1_Big_blood(Game):
#     def __init__(self):
#         super(User1_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
#         self.rect.x = SCREEN_RECT.x + 30
#         self.rect.y = SCREEN_RECT.y
#
#     def update(self):
#         if User1.life == 5:
#             self.image = pygame.image.load("./植物大战僵尸素材/一管血.png")
#         elif User1.life == 4:
#             self.image = pygame.image.load("./植物大战僵尸素材/四分之三管血.png")
#         elif User1.life == 3:
#             self.image = pygame.image.load("./植物大战僵尸素材/半管血.png")
#         elif User1.life == 2:
#             self.image = pygame.image.load("./植物大战僵尸素材/四分之一管血.png")
#         elif User1.life == 1:
#             self.image = pygame.image.load("./植物大战僵尸素材/一丝血.png")
#
#         pass
#
# class User2_Big_blood(Game):
#     def __init__(self):
#         super(User2_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
#         self.rect.x = SCREEN_RECT.x + 1350
#         self.rect.y = SCREEN_RECT.y
#
#     def update(self):
#         if User2.life == 5:
#             self.image = pygame.image.load("./植物大战僵尸素材/一管血.png")
#         elif User2.life == 4:
#             self.image = pygame.image.load("./植物大战僵尸素材/四分之三管血.png")
#         elif User2.life == 3:
#             self.image = pygame.image.load("./植物大战僵尸素材/半管血.png")
#         elif User2.life == 2:
#             self.image = pygame.image.load("./植物大战僵尸素材/四分之一管血.png")
#         elif User2.life == 1:
#             self.image = pygame.image.load("./植物大战僵尸素材/一丝血.png")
#         pass
#
# class Nut(Game):
#     def __init__(self):
#         super(Nut, self).__init__(pygame.image.load("./植物大战僵尸素材/小坚果.gif"))
#         pass
#
#     def update(self):
#         super(Nut, self).update()
#         self.rect.y += 10
#         if self.rect.y >= 830:
#             self.rect.y = 830
#         if self.rect.y < 0:
#             self.rect.y = 0
#         elif self.rect.x > 1400:
#             self.rect.x = 1400
#         elif self.rect.x < 0:
#             self.rect.x = 0
#         elif 400 <= self.rect.y <= 430 and 200 <= self.rect.x <= 470:
#             self.rect.y = 400
#         elif 250 <= self.rect.y <= 300 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 270
#         pass
#
# class Fire_tree_bullet1(Game):
#     def __init__(self):
#         super(Fire_tree_bullet1, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬树子弹.gif"))
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
# class Fire_tree_bullet2(Game):
#     def __init__(self):
#         super(Fire_tree_bullet2, self).__init__(pygame.image.load("./植物大战僵尸素材/火炬树子弹1.png"))
#         self.speed = 15
#         pass
#
#     def update(self):
#         super().update()
#         self.rect.x -= self.speed
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
# class LL_bullet1(Game):
#     def __init__(self):
#         super(LL_bullet1, self).__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
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
# class LL_bullet2(Game):
#     def __init__(self):
#         super(LL_bullet2, self).__init__(pygame.image.load("./植物大战僵尸素材/幽灵子弹.png"))
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
#         elif 400 <= self.rect.y <= 420 and 200 <= self.rect.x <= 450:
#             self.rect.y = 400
#         elif 260 <= self.rect.y <= 290 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 260
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
#     fly_power = 2
#     bullet = 2
#     power1 = 1
#     power2 = 1
#     fire_tree = Fire_tree()
#     trigger1 = Trigger1()
#     trigger2 = Trigger2()
#     aim = 0
#     life = 5
#
#     def __init__(self):
#         super().__init__(pygame.image.load("./植物大战僵尸素材/豌豆.png"))
#         self.rect.centerx = SCREEN_RECT.centerx - 200
#         self.rect.bottom = SCREEN_RECT.bottom - 200
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
#         elif 400 <= self.rect.y <= 430 and 200 <= self.rect.x <= 450:
#             self.rect.y = 400
#             self.vel_y = 0
#             User1.power = 7
#         elif 250 <= self.rect.y <= 280 and 1100 <= self.rect.x <= 1300:
#             self.rect.y = 250
#             self.vel_y = 0
#             User1.power = 7
#
#         pass
#
#     def fire(self):
#         bullet1 = Bullet1()
#         bullet1.rect.centerx = self.rect.centerx
#         bullet1.rect.centery = self.rect.centery - 20
#
#         self.bullets1.add(bullet1)
#         pass
#
#     def explosion(self):
#         if User1.aim == 0:
#             User1.fire_tree.rect.centerx = self.rect.centerx + 80
#             User1.fire_tree.rect.centery = self.rect.centery
#         else:
#             User1.fire_tree.rect.centerx = self.rect.centerx - 80
#             User1.fire_tree.rect.centery = self.rect.centery
#         self.fire_trees.add(User1.fire_tree)
#
#     def tree_fire1(self):
#         tree_bullet1 = Fire_tree_bullet1()
#         tree_bullet1.rect.centerx = User1.fire_tree.rect.centerx
#         tree_bullet1.rect.centery = User1.fire_tree.rect.centery - 20
#         self.fire_bullets.add(tree_bullet1)
#
#     def tree_fire2(self):
#         tree_bullet2 = Fire_tree_bullet2()
#         tree_bullet2.rect.centerx = User1.fire_tree.rect.centerx
#         tree_bullet2.rect.centery = User1.fire_tree.rect.centery - 20
#         self.fire_bullets.add(tree_bullet2)
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
#         if User1.aim == 0:
#             nut.rect.centerx = self.rect.centerx + 42
#             nut.rect.centery = self.rect.centery + 2
#         else:
#             nut.rect.centerx = self.rect.centerx - 42
#             nut.rect.centery = self.rect.centery + 2
#         self.nuts.add(nut)
#
#     def attacked(self):
#         ice = Ice()
#         ice.rect.x = self.rect.centerx
#         ice.rect.y = -100
#         self.ices.add(ice)
#
# class User2(Game):
#     power = 0
#     power1 = 1
#     power2 = 3
#     aim = 0
#     bullet = 2
#     trigger1 = Trigger1()
#     trigger2 = Trigger2()
#     life = 5
#     fly_power = 2
#
#     def __init__(self):
#         super().__init__(pygame.image.load("./植物大战僵尸素材//暴鲤鱼.png"))
#         self.rect.centerx = SCREEN_RECT.centerx + 200
#         self.rect.bottom = SCREEN_RECT.bottom - 200
#         self.vel_y = 0
#         self.bullets2 = pygame.sprite.Group()
#         self.energies = pygame.sprite.Group()
#         self.triggers1 = pygame.sprite.Group()
#         self.triggers2 = pygame.sprite.Group()
#         self.LL_bullets1 = pygame.sprite.Group()
#         self.LL_bullets2 = pygame.sprite.Group()
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
#     def fire(self):
#         bullet2 = Bullet2()
#         # 设置精灵位置
#         bullet2.rect.centerx = self.rect.centerx
#         bullet2.rect.centery = self.rect.centery
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
#     def trigger_create1(self):
#         User2.trigger1.rect.centerx = self.rect.centerx
#         User2.trigger1.rect.centery = self.rect.centery + 10
#         self.triggers1.add(User2.trigger1)
#
#     def trigger_create2(self):
#         User2.trigger2.rect.centerx = self.rect.centerx
#         User2.trigger2.rect.centery = self.rect.centery + 10
#         self.triggers2.add(User2.trigger2)
#
#     def LL_bullet1(self):
#         ll_billet1 = LL_bullet1()
#         ll_billet1.rect.centery = User2.trigger1.rect.centery
#         ll_billet1.rect.centerx = User2.trigger1.rect.centerx
#         self.LL_bullets1.add(ll_billet1)
#
#     def LL_bullet2(self):
#         ll_billet2 = LL_bullet2()
#         ll_billet2.rect.centery = User2.trigger2.rect.centery
#         ll_billet2.rect.centerx = User2.trigger2.rect.centerx
#         self.LL_bullets2.add(ll_billet2)
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
# class Attack(Game):
#     def __init__(self):
#         super(Attack, self).__init__(pygame.image.load("./植物大战僵尸素材//攻击波.png"))
#
#     def update(self):
#         super(Attack, self).update()
#         self.rect.x -= 20
#         pass
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
# class Drug(Game):
#     def __init__(self):
#         super(Drug, self).__init__(pygame.image.load("./植物大战僵尸素材/医药箱翅膀.png"))
#         self.rect.x = random.randint(50, 1350)
#         self.rect.y = 0
#         pass
#
#     def update(self):
#         self.rect.y += 5
#         if self.rect.y >= 1000:
#             self.kill()
#
# class Clear(Game):
#     def __init__(self):
#         super(Clear, self).__init__(pygame.image.load("./植物大战僵尸素材/清空画布.png"))
#         self.rect.y = 0
#         self.rect.x = 0
#     def update(self):
#         pass
#
# class Main(object):
#     begin = True
#
#     def __init__(self):
#         self.screen = pygame.display.set_mode(SCREEN_RECT.size)
#         self.clock = pygame.time.Clock()
#         self.__create_sprites()
#         pygame.display.set_caption("MyGame")
#         pygame.time.set_timer(jishiqi, 5000)
#         pygame.time.set_timer(jishiqi2, 20000)
#         pass
#
#     def __create_sprites(self):  # 精灵组的创造
#         bk = Background()
#         self.background_group = pygame.sprite.Group(bk)
#
#         self.clear_group = pygame.sprite.Group()
#
#         user1blood = User1_Big_blood()
#         self.user1blood = pygame.sprite.Group(user1blood)
#
#         user2blood = User2_Big_blood()
#         self.user2blood = pygame.sprite.Group(user2blood)
#
#         self.drugs = pygame.sprite.Group()
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
#             elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                 User1.life = 5
#                 self.user1.power1 = 1
#                 self.user1.power2 = 1
#                 User2.life = 5
#                 self.user2.power1 = 1
#                 self.user2.power2 = 3
#                 self.user1.rect.x = 500
#                 self.user1.rect.y = 500
#                 self.user2.rect.x = 900
#                 self.user2.rect.y = 500
#                 clear = Clear()
#                 self.clear_group.add(clear)
#
#                 self.clear_group.update()
#                 self.clear_group.draw(self.screen)
#                 pygame.sprite.groupcollide(self.clear_group, self.user1.DD_bullets1, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user1.DD_bullets2, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user2.LL_bullets1, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user2.LL_bullets2, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user1.nuts, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user1.fire_trees, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user1.fire_bullets, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.drugs, False, True)
#                 pygame.sprite.groupcollide(self.clear_group, self.user1.ices, False, True)
#                 clear.kill()
#                 Main.begin = True
#
#             elif event.type == jishiqi:
#                 self.user1.bullet += 2
#                 self.user1.power1 = 1
#                 self.user1.power2 += 1
#
#                 self.user2.bullet = 2
#                 self.user2.power1 = 1
#                 self.user2.power2 = 3
#
#             elif event.type == jishiqi2:
#                 drug = Drug()
#                 self.drugs.add(drug)
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
#             elif self.user1.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_i:
#                 self.user1.explosion()
#                 self.user1.power1 -= 1
#
#             elif self.user1.power2 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_u:
#                 self.user1.power2 -= 1
#                 self.user1.defence()
#
#             elif self.user2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 and User2.aim == 1:
#                 self.user2.trigger_create1()
#                 self.user2.fire()
#                 self.user2.bullet -= 1
#
#             elif self.user2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 and User2.aim == 0:
#                 self.user2.trigger_create2()
#                 self.user2.fire()
#                 self.user2.bullet -= 1
#
#             elif self.user2.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP4:
#                 self.user1.attacked()
#                 self.user2.power1 -= 1
#
#         key2 = pygame.key.get_pressed()
#         if key2[pygame.K_KP5] and self.user2.power2 != 0 and User2.aim == 0:
#             self.user2.trigger_create2()
#             self.user2.fire()
#             self.user2.power2 -= 1
#
#         elif key2[pygame.K_KP5] and self.user2.power2 != 0 and User2.aim == 1:
#             self.user2.trigger_create1()
#             self.user2.fire()
#             self.user2.power2 -= 1
#
#         key_operation = pygame.key.get_pressed()  # 返回元组
#         if key_operation[pygame.K_d]:
#             self.user1.rect.x += 6
#             self.user1.image = (pygame.image.load("./植物大战僵尸素材/豌豆.png"))
#             User1.aim = 0
#         elif key_operation[pygame.K_a]:
#             self.user1.rect.x -= 6
#             self.user1.image = (pygame.image.load("./植物大战僵尸素材/豌豆left.png"))
#             User1.aim = 1
#
#         key_operation2 = pygame.key.get_pressed()
#         if key_operation2[pygame.K_RIGHT]:
#             self.user2.rect.x += 6
#             self.user2.image = pygame.image.load("./植物大战僵尸素材//暴鲤鱼left.png")
#             User2.aim = 1
#         elif key_operation2[pygame.K_LEFT]:
#             self.user2.rect.x -= 6
#             self.user2.image = pygame.image.load("./植物大战僵尸素材//暴鲤鱼.png")
#             User2.aim = 0
#
#             pass
#
#     def draw(self):
#
#         self.background_group.update()
#         self.background_group.draw(self.screen)
#
#         self.user1blood.update()
#         self.user1blood.draw(self.screen)
#
#         self.user2blood.update()
#         self.user2blood.draw(self.screen)
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
#         self.user2.triggers1.update()
#         self.user1.triggers1.draw(self.screen)
#
#         self.user2.triggers2.update()
#         self.user1.triggers2.draw(self.screen)
#
#         self.drugs.update()
#         self.drugs.draw(self.screen)
#
#         self.user2.LL_bullets1.update()
#         self.user2.LL_bullets1.draw(self.screen)
#
#         self.user2.LL_bullets2.update()
#         self.user2.LL_bullets2.draw(self.screen)
#
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
#         pygame.sprite.groupcollide(self.user2.LL_bullets2, self.user1.DD_bullets1, True, True)
#         pygame.sprite.groupcollide(self.user2.LL_bullets1, self.user1.DD_bullets1, True, True)
#         pygame.sprite.groupcollide(self.user2.LL_bullets2, self.user1.DD_bullets2, True, True)
#         pygame.sprite.groupcollide(self.user2.LL_bullets1, self.user1.DD_bullets2, True, True)
#         pygame.sprite.groupcollide(self.user1.fire_trees, self.user2.LL_bullets1, True, True)
#         pygame.sprite.groupcollide(self.user1.nuts, self.user2.LL_bullets1, True, True)
#         pygame.sprite.groupcollide(self.user1.fire_trees, self.user2.LL_bullets2, True, True)
#         pygame.sprite.groupcollide(self.user1.nuts, self.user2.LL_bullets2, True, True)
#
#
#         if pygame.sprite.spritecollide(self.user1, self.user2.LL_bullets1, True):
#             if User1.life > 1:
#                 User1.life -= 1
#             else:
#                 font_name = pygame.font.match_font('fangsong')
#                 font = pygame.font.Font(font_name, 62)
#                 text = font.render('蓝龙WIN!', True, 'black')
#                 self.screen.blit(text, (650, 400))
#                 pygame.display.update()
#                 Main.begin = False
#         elif pygame.sprite.spritecollide(self.user1, self.user2.LL_bullets2, True):
#             if User1.life > 1:
#                 User1.life -= 1
#             else:
#                 font_name = pygame.font.match_font('fangsong')
#                 font = pygame.font.Font(font_name, 62)
#                 text = font.render('蓝龙WIN!', True, 'black')
#                 self.screen.blit(text, (650, 400))
#                 pygame.display.update()
#                 Main.begin = False
#         elif pygame.sprite.spritecollide(self.user1, self.user1.ices, True):
#             if User1.life > 1:
#                 User1.life -= 1
#             else:
#                 font_name = pygame.font.match_font('fangsong')
#                 font = pygame.font.Font(font_name, 62)
#                 text = font.render('蓝龙WIN!', True, 'black')
#                 self.screen.blit(text, (650, 400))
#                 pygame.display.update()
#                 Main.begin = False
#         elif pygame.sprite.spritecollide(self.user2, self.user1.DD_bullets1, True) or pygame.sprite.spritecollide(self.user2, self.user1.DD_bullets2, True):
#             if User2.life > 1:
#                 User2.life -= 1
#             else:
#                 font_name = pygame.font.match_font('fangsong')
#                 font = pygame.font.Font(font_name, 62)
#                 text = font.render('豌豆WIN!', True, 'black')
#                 self.screen.blit(text, (650, 400))
#                 pygame.display.update()
#                 Main.begin = False
#         elif pygame.sprite.groupcollide(self.user1.fire_trees, self.user1.DD_bullets1, False, True):
#             self.user1.tree_fire1()
#
#         elif pygame.sprite.groupcollide(self.user1.fire_trees, self.user1.DD_bullets2, False, True):
#             self.user1.tree_fire2()
#
#         elif pygame.sprite.groupcollide(self.user1.triggers1, self.user1.bullets1, False, True):
#             self.user1.DD_bullet1()
#             self.user1.trigger1.kill()
#
#         elif pygame.sprite.groupcollide(self.user1.triggers2, self.user1.bullets1, False, True):
#             self.user1.DD_bullet2()
#             self.user1.trigger2.kill()
#
#         elif pygame.sprite.groupcollide(self.user2.triggers1, self.user2.bullets2, False, True):
#             self.user2.LL_bullet1()
#             self.user2.trigger1.kill()
#
#
#         elif pygame.sprite.groupcollide(self.user2.triggers2, self.user2.bullets2, False, True):
#             self.user2.LL_bullet2()
#             self.user2.trigger2.kill()
#
#         elif pygame.sprite.spritecollide(self.user2, self.user1.fire_bullets, True):
#             if User2.life > 1:
#                 User2.life -= 1
#             else:
#                 font_name = pygame.font.match_font('fangsong')
#                 font = pygame.font.Font(font_name, 62)
#                 text = font.render('豌豆WIN!', True, 'black')
#                 self.screen.blit(text, (650, 400))
#                 pygame.display.update()
#                 Main.begin = False
#         elif pygame.sprite.spritecollide(self.user2, self.drugs, True):
#             if User2.life < 4:
#                 User2.life += 2
#             elif User2.life == 4:
#                 User2.life += 1
#
#         elif pygame.sprite.spritecollide(self.user1, self.drugs, True):
#             if User1.life < 4:
#                 User1.life += 2
#             elif User1.life == 4:
#                 User1.life += 1
#             pass
#
#     def start_game(self):
#         print("开始啦")
#         pygame.init()
#         pygame.mixer.music.load("./植物大战僵尸素材/门的另一端.mp3")
#
#         while True:
#             self.clock.tick(60)
#             self.draw()
#             self.__event()
#             self.crash()
#             if Main.begin is True:
#                 pygame.display.update()
#             if pygame.mixer.music.get_busy() is False:
#                 pygame.mixer.music.play()
#
#
#
#     @staticmethod
#     def __game_over():
#         print("游戏结束")
#         pygame.quit()
#         sys.exit()
#
# if __name__ == '__main__':
#     game = Main()
#     game.start_game()



import random
import sys
import pygame

jishiqi = pygame.USEREVENT
jishiqi2 = pygame.USEREVENT + 1
jishiqi3 = pygame.USEREVENT + 2

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
        super(Background, self).__init__(pygame.image.load("./植物大战僵尸素材/云端2.png"))

    def update(self):
        pass

class User1energy(Game):
    def __init__(self):
        super(User1energy, self).__init__(pygame.image.load('./植物大战僵尸素材/满能量.png'))

    def update(self):
        if User1.energy == 4:
            self.image = pygame.image.load('./植物大战僵尸素材/满能量.png')
        elif User1.energy == 3:
            self.image = pygame.image.load('./植物大战僵尸素材/三点能量.png')
        elif User1.energy == 2:
            self.image = pygame.image.load('./植物大战僵尸素材/一半能量.png')
        elif User1.energy == 1:
            self.image = pygame.image.load('./植物大战僵尸素材/一点能量.png')
        elif User1.energy == 0:
            self.image = pygame.image.load('./植物大战僵尸素材/无能量.png')
        pass

class User1_bullet_number(Game):
    def __init__(self):
        super(User1_bullet_number, self).__init__(pygame.image.load('./植物大战僵尸素材/子弹.png'))

    def update(self):
        if User1.bullet == 6:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹(6).png')
        elif User1.bullet == 5:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹(5).png')
        elif User1.bullet == 4:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹(4).png')
        elif User1.bullet == 3:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹(3).png')
        elif User1.bullet == 2:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹(2).png')
        elif User1.bullet == 1:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹(1).png')
        elif User1.bullet == 0:
            self.image = pygame.image.load('./植物大战僵尸素材/子弹.png')
        pass

class User2_bullet_number(Game):
    def __init__(self):
        super(User2_bullet_number, self).__init__(pygame.image.load('./植物大战僵尸素材/幽灵子弹.png'))

    def update(self):
        if User2.bullet == 6:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹(6).png')
        elif User2.bullet == 5:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹(5).png')
        elif User2.bullet == 4:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹(4).png')
        elif User2.bullet == 3:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹(3).png')
        elif User2.bullet == 2:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹(2).png')
        elif User2.bullet == 1:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹(1).png')
        elif User2.bullet == 0:
            self.image = pygame.image.load('./植物大战僵尸素材/幽灵子弹.png')
        pass

class User2energy(Game):
    def __init__(self):
        super(User2energy, self).__init__(pygame.image.load("./植物大战僵尸素材/大能量.png"))

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

class User2_Big_blood(Game):
    def __init__(self):
        super(User2_Big_blood, self).__init__(pygame.image.load("./植物大战僵尸素材/一管血.png"))
        # self.rect.x = SCREEN_RECT.x + 1350
        # self.rect.y = SCREEN_RECT.y

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
    energy = 0
    bullet = 2
    fire_tree = Fire_tree()
    trigger1 = Trigger1()
    trigger2 = Trigger2()
    user1blood = User1_Big_blood()
    use1_energy = User1energy()
    user1_bullet_number = User1_bullet_number()
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
        self.user1blood = pygame.sprite.Group(User1.user1blood)
        self.user1_energy = pygame.sprite.Group(User1.use1_energy)
        self.user1_bullet_number = pygame.sprite.Group(User1.user1_bullet_number)
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

        User1.user1blood.rect.x = self.rect.x
        User1.user1blood.rect.y = self.rect.y - 50

        User1.use1_energy.rect.x = self.rect.x
        User1.use1_energy.rect.y = self.rect.y - 10

        User1.user1_bullet_number.rect.x = self.rect.x + 128
        User1.user1_bullet_number.rect.y = self.rect.y - 40
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
        ice.rect.y = - 100
        self.ices.add(ice)

class User2(Game):
    power = 0
    energy = 0
    power1 = 1
    power2 = 3
    aim = 0
    bullet = 2
    trigger1 = Trigger1()
    trigger2 = Trigger2()
    user2blood = User2_Big_blood()
    use2_energy = User2energy()
    use2_energy_small = User2energy_small()
    user2_bullet_number = User2_bullet_number()

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
        self.user2blood = pygame.sprite.Group(User2.user2blood)
        self.user2_energy = pygame.sprite.Group(User2.use2_energy)
        self.user2_energy_small = pygame.sprite.Group(User2.use2_energy_small)
        self.user2_bullet_number = pygame.sprite.Group(User2.user2_bullet_number)

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

        User2.user2blood.rect.x = self.rect.x
        User2.user2blood.rect.y = self.rect.y - 50

        User2.use2_energy.rect.x = self.rect.x + 50
        User2.use2_energy.rect.y = self.rect.y - 100

        User2.use2_energy_small.rect.x = self.rect.x
        User2.use2_energy_small.rect.y = self.rect.y - 100

        User2.user2_bullet_number.rect.x = self.rect.x + 100
        User2.user2_bullet_number.rect.y = self.rect.y - 100

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
        pygame.time.set_timer(jishiqi3, 2000)
        pass

    def __create_sprites(self):  # 精灵组的创造
        bk = Background()
        self.background_group = pygame.sprite.Group(bk)

        self.clear_group = pygame.sprite.Group()

        self.drugs = pygame.sprite.Group()

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
                User1.energy = 0
                User2.life = 5
                self.user2.power1 = 1
                self.user2.power2 = 3
                User1.bullet = 0
                User2.bullet = 0
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

            elif event.type == jishiqi3:
                if User1.bullet <= 5:
                    User1.bullet += 1
                if User1.energy < 4:
                    User1.energy += 1
                if User2.bullet <= 5:
                    User2.bullet += 1

            elif event.type == jishiqi:
                User2.power1 = 1
                User2.power2 = 3

            elif event.type == jishiqi2:
                drug = Drug()
                self.drugs.add(drug)

            elif User1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j and User1.aim == 0:
                self.user1.trigger_create1()
                self.user1.fire()
                User1.bullet -= 1

            elif User1.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_j and User1.aim == 1:
                self.user1.trigger_create2()
                self.user1.fire()
                User1.bullet -= 1

            elif User1.energy >= 2 and event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.user1.explosion()
                User1.energy -= 2

            elif User1.energy >= 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                User1.energy -= 1
                self.user1.defence()

            elif User2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 and User2.aim == 1:
                self.user2.trigger_create1()
                self.user2.fire()
                User2.bullet -= 1

            elif User2.bullet != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 and User2.aim == 0:
                self.user2.trigger_create2()
                self.user2.fire()
                User2.bullet -= 1

            elif User2.power1 != 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_KP4:
                self.user1.attacked()
                User2.power1 -= 1

        key2 = pygame.key.get_pressed()
        if key2[pygame.K_KP5] and User2.power2 != 0 and User2.aim == 0:
            self.user2.trigger_create2()
            self.user2.fire()
            User2.power2 -= 1

        elif key2[pygame.K_KP5] and User2.power2 != 0 and User2.aim == 1:
            self.user2.trigger_create1()
            self.user2.fire()
            User2.power2 -= 1

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

        self.user1.user1blood.update()
        self.user1.user1blood.draw(self.screen)

        self.user2.user2blood.update()
        self.user2.user2blood.draw(self.screen)

        self.user1.user1_energy.update()
        self.user1.user1_energy.draw(self.screen)

        if User2.power2 != 0:
            self.user2.user2_energy.update()
            self.user2.user2_energy.draw(self.screen)

        if User2.power1 != 0:
            self.user2.user2_energy_small.update()
            self.user2.user2_energy_small.draw(self.screen)

        self.user1.user1_bullet_number.update()
        self.user1.user1_bullet_number.draw(self.screen)

        self.user2.user2_bullet_number.update()
        self.user2.user2_bullet_number.draw(self.screen)

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
        pygame.mixer.music.load("./植物大战僵尸素材/门的另一端.mp3")
        while True:
            self.clock.tick(60)
            self.draw()
            self.__event()
            self.crash()
            if Main.begin is True:
                pygame.display.update()
            if pygame.mixer.music.get_busy() is False:
                pygame.mixer.music.play()

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Main()
    game.start_game()