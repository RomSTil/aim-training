#                        
#　　　　　　　　　　_,.. -──- ､,
#　　　　　　　　,　'" 　 　　　 　　 `ヽ.
#　　　　　　 ／/¨7__　　/ 　 　 i　 _厂廴
#　　　　　 /￣( ノ__/　/{　　　　} ｢　（_冫}
#　　　　／￣l＿// 　/-|　 ,!　 ﾑ ￣|＿｢ ＼＿_
#　　. イ　 　 ,　 /!_∠_　|　/　/_⊥_,ﾉ ハ　 イ 
#　　　/ ／ / 　〃ん心 ﾚ'|／　ｆ,心 Y　i ＼_＿＞　
#　 ∠イ 　/　 　ﾄ弋_ツ　　 　 弋_ﾂ i　 |　 | ＼
#　 _／ _ノ|　,i　⊂⊃　　　'　　　⊂⊃ ./　 !､＿ン
#　　￣　　∨|　,小、　　` ‐ ' 　　 /|／|　/
#　 　 　 　 　 Y　|ﾍ＞ 、 ＿ ,.　イﾚ|　 ﾚ'
#　　　　　　 r'.| 　|;;;入ﾞ亠―亠' );;;;;! 　|､
#　　　　　 ,ノ:,:|.　!|く　__￣￣￣__У　ﾉ|:,:,ヽ
#　　　　　(:.:.:.:ﾑ人!ﾍ　 　` ´ 　　 厂|ノ:.:.:丿 by @RomSTil

#подключение библеотек
import pygame, random

#Класс Прицела
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("awp.mp3") 
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

#класс Мишени
class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

#главный сетап
pygame.init
pygame.mixer.init()
clock = pygame.time.Clock()


#параметры окна
sc_top = 0
sc_left = 0
sc_widht = 1200
sc_height = 700
sc_icon = pygame.image.load("Icon.png")
screen = pygame.display.set_mode((sc_widht, sc_height))
pygame.display.set_caption("by @RomSTil")
pygame.display.set_icon(sc_icon)
color_white = (240,245,249)
backround = pygame.image.load("bg_blue.png")
pygame.mouse.set_visible(False)




#прицел
crosshair = Crosshair("crosshair_red_large.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Мешени
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("target_colored.png", random.randrange(0, sc_widht), random.randrange(0, sc_widht))
    target_group.add(new_target)

#----------------------#
screen.fill(color_white)
is_game = True
while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(backround, (0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)