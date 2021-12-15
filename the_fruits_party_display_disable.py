import math
import pygame 
import sys
import random
from pygame.locals import*

class GAME:
    def __init__(self, title_point=1):
        self.title_point = title_point
        self.list_fruits = []
        self.FPSCLOCK = pygame.time.Clock()
        self.direction = 'R'
        self.score = 0
        self.fruits_speed = 1
        self.player_hit_rect = pygame.Rect(0, 0, 10, 10)
        self.con = False
        self.pause_1 = 1
        self.fruits = pygame.Rect(0, 0, 10, 10)
        self.fruits_count = 0
        self.timegame = 0
        self.player_vel = 79
        self.level_stat = 0
        self.sound_stat = 0
        self.isDash = False
        self.dash_count = 12
        self.savelevel = 0
        self.savescore = 0
        self.ftime = 0
        self.position = [0, 79, 158, 237, 316, 395, 474, 553, 632, 711]
        self.sound = Sound()
        self.targetSoundFruit = 0
        self.intereact = False
        self.isSay = False

    def reset(self):
        self.list_fruits = []
        self.FPSCLOCK = pygame.time.Clock()
        self.direction = 'R'
        self.time = 0
        self.level = '0'
        self.score = 0
        self.fruits_speed = 1
        self.player_hit_rect = pygame.Rect(0, 0, 10, 10)
        self.fruits = pygame.Rect(500, 250, 10, 10)
        self.con = False
        self.pause_1 = 1
        self.timegame = 0
        self.level_stat = 0
        self.sound_stat = 0
        self.fruits_count = 0
        self.isDash = False
        self.dash_count = 12

    def image_load(self):
        self.menu = pygame.image.load('image/menu/menu_fruits_party.png')
        self.start = pygame.image.load('image/menu/start_fruits_party.png')
        self.con = pygame.image.load('image/menu/con_fruits_party.png')
        self.exit = pygame.image.load('image/menu/exit_fruits_party.png')
        self.BG = pygame.image.load('image/BG/Background_1.png')
        self.orange = pygame.image.load('image/fruits/orange.png')
        self.cherry = pygame.image.load('image/fruits/cherry.png')
        self.watamelon = pygame.image.load('image/fruits/watamelon.png')
        self.rose_apple = pygame.image.load('image/fruits/rose_apple.png')
        self.player = pygame.image.load('image/player/player.png')
        self.stage_1 = pygame.image.load('image/BG/stage_1.png')
        self.stage_2 = pygame.image.load('image/BG/stage_2.png')
        self.stage_3 = pygame.image.load('image/BG/stage_3.png')
        self.stage_4 = pygame.image.load('image/BG/stage_4.png')
        self.stage_5 = pygame.image.load('image/BG/stage_5.png')
        self.clear = pygame.image.load('image/BG/clear.png')
        self.over = pygame.image.load('image/BG/game_over.png')
        self.wall = pygame.image.load('image/wall/wall.png')
        self.tutor0 = pygame.image.load('image/BG/tutor0.png')
        self.tutor1 = pygame.image.load('image/BG/tutor1.png')
        self.tutor2 =pygame.image.load('image/BG/tutor2.png')
        self.tutor3 =pygame.image.load('image/BG/tutor3.png')
        self.tutor4 =pygame.image.load('image/BG/tutor4.png')

    def Title_screen(self, title_check):
        self.screen = pygame.display.set_mode((800, 800))
        if title_check == -1:
            if self.title_point == 4:
                self.title_point = 1
            else:
                self.title_point += 1
        elif title_check == 1:
            if self.title_point == 1:
                self.title_point = 4
            else:
                self.title_point -= 1
        if self.title_point == 1:
            Title = pygame.image.load(
                "image/menu/start_fruits_party.png").convert()
        elif self.title_point == 2:
            Title = pygame.image.load(
                "image/menu/con_fruits_party.png").convert()
        elif self.title_point == 3: 
            Title = pygame.image.load(
                "image/menu/tutorial_fruits_party.png").convert()
        elif self.title_point == 4:
            Title = pygame.image.load(
                "image/menu/exit_fruits_party.png").convert()
        self.screen.blit(Title, (0, 0))

    def draw_background(self):
        self.screen.blit(self.BG, (0, 0))

    def close(self):
        pygame.quit()
        sys.exit()

    def menu_run(self):
        pygame.init()
        pygame.display.set_caption('The Fruits Party')
        pygame.display.set_icon(pygame.image.load('image/icon/icon_game.jpg'))
        self.screen = pygame.display.set_mode((800, 800))
        Sound.BG_music_menu()
        self.image_load()
        Sound.Sound_menu()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if self.title_point == 1:
                            Sound.Sound_Cursor_1()
                            self.reset()
                            self.con = True
                            self.game_run()
                        elif self.title_point == 2:
                            Sound.Sound_Cursor_1()
                            self.game_con()
                            self.game_run()
                        elif self.title_point == 3:
                            Sound.Sound_Cursor_1()
                            self.tutor()
                        elif self.title_point == 4:
                            Sound.Sound_Cursor_1()
                            self.close()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.Title_screen(-1)
                        if self.title_point == 1:
                            Sound.Sound_startparty()
                        if self.title_point == 2:
                            Sound.Sound_continue()
                        if self.title_point == 3:
                            Sound.Sound_tutorial()
                        if self.title_point == 4:
                            Sound.Sound_exit()
                        Sound.Sound_Cursor_2()
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.Title_screen(1)
                        if self.title_point == 1:
                            Sound.Sound_startparty()
                        if self.title_point == 2:
                            Sound.Sound_continue()
                        if self.title_point == 3:
                            Sound.Sound_tutorial()
                        if self.title_point == 4:
                            Sound.Sound_exit()
                        Sound.Sound_Cursor_2()
            self.FPSCLOCK.tick(60)
            self.Title_screen(0)
            pygame.display.update()

    def game_run(self):
        pygame.init()
        Sound.Sound_stop()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gameover()
                    if (event.key == K_LEFT or event.key == K_a and self.isDash == False):
                        self.direction = 'L'
                        self.intereact = True
                        self.isDash = True
                    elif (event.key == K_RIGHT or event.key == K_d and self.isDash == False ):
                        self.direction = 'R'
                        self.intereact = True
                        self.isDash = True
                        self.isSay = True
                    elif (event.key == K_UP or event.key == K_w and self.isDash == False):
                        self.direction = 'U'
                        self.intereact = True
                        self.isDash = True
                    elif (event.key == K_DOWN or event.key == K_s and self.isDash == False):
                        self.direction = 'D'
                        self.intereact = True
                        self.isDash = True
                    elif event.key == K_p:
                        self.pause_screen()
                        self.pause_1 = 1
                    print(pygame.key.name(event.key))
            self.check_level()
            self.show_level()
            self.draw_background()
            self.generate_fruits(self.time)
            self.fruit_Sound()
            self.fruits_move()
            self.check_position()
            self.draw_fruits()
            self.sound.Sound_Distance(self.list_fruits,self.player_hit_rect)
            self.player_move()
            self.draw_player()
            self.FPSCLOCK.tick(60)
            self.time += 1
            self.timegame += 1
            

    def show_level(self):
        if self.level_stat == 1:
            self.screen.blit(self.stage_1, (0, 0))
            Sound.Sound_stage(self.level_stat)
            pygame.display.update()
            pygame.time.delay(2000)
            self.level_stat = 1.5

        if self.level_stat == 2:
            self.screen.blit(self.stage_2, (0, 0))
            Sound.Sound_stage(self.level_stat)
            pygame.display.update()
            pygame.time.delay(2000)
            self.level_stat = 2.5
            self.sound_stat = 0

        if self.level_stat == 3:
            self.screen.blit(self.stage_3, (0, 0))
            Sound.Sound_stage(self.level_stat)
            pygame.display.update()
            pygame.time.delay(2000)
            self.level_stat = 3.5
            self.sound_stat = 0

        if self.level_stat == 4:
            self.screen.blit(self.stage_4, (0, 0))
            Sound.Sound_stage(self.level_stat)
            pygame.display.update()
            pygame.time.delay(2000)
            self.level_stat = 4.5
            self.sound_stat = 0


        if self.level_stat == 5:
            self.screen.blit(self.stage_5, (0, 0))
            Sound.Sound_stage(self.level_stat)
            pygame.display.update()
            pygame.time.delay(2000)
            self.level_stat = 5.5
            self.sound_stat = 0

    def check_level(self):
        if self.timegame % 60 == 0:
            print(self.timegame/60)
        if self.level_stat == 0:
            self.level_stat = 1
            self.BG = self.BG
            self.savescore = self.score

        elif self.level_stat == 1.5:
            self.savelevel = self.level_stat
            if (self.time % 600 == 0):
                print('score', self.score)
            if self.timegame % 9000  == 0 and self.score < 2:
                self.gameover()
            elif self.score == 2:
                Sound.Sound_stop()
                self.timegame = 0
                self.level_stat = 2
                self.savescore = self.score

        elif self.level_stat == 2.5:
            self.savelevel = self.level_stat
            if (self.time % 600 == 0):
                print('score', self.score)
            if self.timegame % 9000 == 0 and self.score < 4:
                self.gameover()
            elif self.score == 4:
                Sound.Sound_stop()
                self.timegame = 0
                self.level_stat = 3
                self.savescore = self.score

        elif self.level_stat == 3.5:
            self.savelevel = self.level_stat
            if (self.time % 600 == 0):
                print('score', self.score)
            if self.timegame % 9000 == 0 and self.score < 7:
                self.gameover()
            elif self.score == 7:
                Sound.Sound_stop()
                self.timegame = 0
                self.level_stat = 4
                self.savescore = self.score

        elif self.level_stat == 4.5:
            self.savelevel = self.level_stat
            if (self.time % 600 == 0):
                print('score', self.score)
            if self.timegame % 9000 == 0 and self.score < 10:
                self.gameover()
            elif self.score == 10:
                Sound.Sound_stop()
                self.timegame = 0
                self.level_stat = 5
                self.savescore = self.score
                self.list_fruits = []

        elif self.level_stat == 5.5:
            self.savelevel = self.level_stat
            if (self.time % 600 == 0):
                print('score', self.score)
            if self.timegame % 9000 == 0 and self.score < 14:
                self.gameover()
            elif self.score == 14:
                Sound.Sound_stop()
                self.timegame = 0
                self.gameover()

    def game_con(self):
        self.level_stat = self.savelevel
        self.sound_stat = 0
        self.list_fruits = []
        self.timegame = 1
        self.score = self.savescore
        self.player_hit_rect = pygame.Rect(0, 0, 10, 10)

    def tutor(self):
        self.tutor_point = 0
        Sound.Sound_stop()
        Sound.Sound_tutor0()
        self.screen.blit(self.tutor0,(0,0))
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()         
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.tutor_point +=1
                        if self.tutor_point <= 0:
                            self.tutor_point = 0
                        if self.tutor_point >= 4:
                            self.tutor_point = 4
                        if self.tutor_point == 0:
                            Sound.Sound_stop()
                            Sound.Sound_tutor0()
                            self.screen.blit(self.tutor0,(0,0))    
                        if self.tutor_point == 1:
                            Sound.Sound_stop()
                            Sound.Sound_tutor1()
                            self.screen.blit(self.tutor1,(0,0))        
                        if self.tutor_point == 2:
                            Sound.Sound_stop()
                            Sound.Sound_tutor2()
                            self.screen.blit(self.tutor2,(0,0))
                        if self.tutor_point == 3:
                            Sound.Sound_stop()
                            Sound.Sound_tutor3()
                            self.screen.blit(self.tutor3,(0,0))
                        if self.tutor_point == 4:
                            Sound.Sound_stop()
                            Sound.Sound_tutor4()
                            self.screen.blit(self.tutor4,(0,0))
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.tutor_point -=1
                        if self.tutor_point <= 0:
                            self.tutor_point = 0
                        if self.tutor_point >= 4:
                            self.tutor_point = 4
                        if self.tutor_point == 0:
                            Sound.Sound_stop()
                            Sound.Sound_tutor0()
                            self.screen.blit(self.tutor0,(0,0))    
                        if self.tutor_point == 1:
                            Sound.Sound_stop()
                            Sound.Sound_tutor1()
                            self.screen.blit(self.tutor1,(0,0)) 
                        if self.tutor_point == 2:
                            Sound.Sound_stop()
                            Sound.Sound_tutor2()
                            self.screen.blit(self.tutor2,(0,0))
                        if self.tutor_point == 3:
                            Sound.Sound_stop()
                            Sound.Sound_tutor3()
                            self.screen.blit(self.tutor3,(0,0))
                        if self.tutor_point == 4:
                            Sound.Sound_stop()
                            Sound.Sound_tutor4()
                            self.screen.blit(self.tutor4,(0,0))
                    elif event.key == pygame.K_s or pygame.K_SPACE or pygame.K_RETURN :
                        Sound.Sound_stop()
                        return
            pygame.display.update()

    def draw_player(self):
        if (self.direction == 'U'):
            self.screen.blit(self.player,
                             (self.player_hit_rect))
        if (self.direction == 'D'):
            self.screen.blit(self.player,
                             (self.player_hit_rect))
        if (self.direction == 'L'):
            self.screen.blit(self.player,
                             (self.player_hit_rect))
        if (self.direction == 'R'):
            self.screen.blit(self.player,
                             (self.player_hit_rect))

    def player_move(self):
        self.keys = pygame.key.get_pressed()
        if self.direction == 'R':
            if self.isDash:
                if self.dash_count >= 0:
                    self.player_hit_rect.x += self.dash_count
                    self.dash_count -= 1
                else:
                    self.player_hit_rect.x += 1
                    self.isDash = False
                    self.dash_count = 12
        if self.direction == 'L':
            if self.isDash:
                if self.dash_count >= 0:
                    self.player_hit_rect.x -= self.dash_count * 1
                    self.dash_count -= 1
                else:
                    self.player_hit_rect.x -= 1
                    self.isDash = False
                    self.dash_count = 12
        if self.direction == 'U':
            if self.isDash:
                if self.dash_count >= 0:
                    self.player_hit_rect.y -= self.dash_count * 1
                    self.dash_count -= 1
                else:
                    self.player_hit_rect.y -= 1
                    self.isDash = False
                    self.dash_count = 12
        if self.direction == 'D':
            if self.isDash:
                if self.dash_count >= 0:
                    self.player_hit_rect.y += self.dash_count * 1
                    self.dash_count -= 1
                else:
                    self.player_hit_rect.y += 1
                    self.isDash = False
                    self.dash_count = 12

        if self.player_hit_rect.x > 712:
            Sound.Sound_wall()
            self.player_hit_rect.x = 712
        if self.player_hit_rect.x < 0:
            Sound.Sound_wall()
            self.player_hit_rect.x = 0
        if self.player_hit_rect.y > 712:
            Sound.Sound_wall()
            self.player_hit_rect.y = 712
        if self.player_hit_rect.y < 0:
            Sound.Sound_wall()
            self.player_hit_rect.y = 0
        for fruits in self.list_fruits:
            if self.player_hit_rect.colliderect(fruits.rect):
                if fruits.type == 'wall' and self.direction == 'D':
                    Sound.Sound_wall()
                    self.player_hit_rect.y -= 79
                if fruits.type == 'wall' and self.direction == 'U':
                    Sound.Sound_wall()
                    self.player_hit_rect.y += 79
                if fruits.type == 'wall' and self.direction == 'R':
                    Sound.Sound_wall()
                    self.player_hit_rect.x -= 79
                if fruits.type == 'wall' and self.direction == 'L':
                    Sound.Sound_wall()
                    self.player_hit_rect.x += 79
                if fruits.type != 'wall':
                    self.list_fruits.remove(fruits)
                    self.score += 1
                    Sound.Sound_get()

    def generate_fruits(self, time):
        if (len(self.list_fruits) == 0):
            fruits = Fruits(
                self.player_hit_rect.x, self.player_hit_rect.y, self.list_fruits, self.fruits_count, self.level_stat)
            for i in fruits.type:
                fruits = Fruits(
                    self.player_hit_rect.x, self.player_hit_rect.y, self.list_fruits, self.fruits_count, self.level_stat)
                self.list_fruits.append(fruits)
                self.fruits_count += 1
                fruits.type = i

    def draw_fruits(self):
        for fruits in self.list_fruits:
            if fruits.type == 'orange':
                self.screen.blit(
                    self.orange, (fruits.x, fruits.y))
            if fruits.type == 'rose_apple':
                self.screen.blit(
                    self.rose_apple, (fruits.x, fruits.y))
            if fruits.type == 'cherry':
                self.screen.blit(
                    self.cherry, (fruits.x, fruits.y))
            if fruits.type == 'watamelon':
                self.screen.blit(
                    self.watamelon, (fruits.x, fruits.y))
            if fruits.type == 'wall':
                self.screen.blit(
                    self.wall, (fruits.x, fruits.y))

    def fruits_move(self):
        for fruits in self.list_fruits:
            if fruits.type == 'rose_apple' or fruits.type == 'cherry' or fruits.type == 'watamelon':
                fruits.distance = math.hypot(self.player_hit_rect.x-fruits.x,
                                             self.player_hit_rect.y-fruits.y)
                if fruits.distance > 150:
                    if fruits.type == 'rose_apple' or fruits.type == 'cherry':
                        if fruits.direction == 0:
                            fruits.direction = random.choice(
                                fruits.list_direction_fruits)
                        if self.timegame % 60 == 0:
                            fruits.direction = random.choice(
                                fruits.list_direction_fruits)
                        if self.timegame % 60 == 0:
                            if fruits.direction == "left":
                                fruits.x = fruits.x-fruits.ran
                            elif fruits.direction == "right":
                                fruits.x = fruits.x+fruits.ran
                            elif fruits.direction == "down":
                                fruits.y = fruits.y-fruits.ran
                            elif fruits.direction == "top":
                                fruits.y = fruits.y+fruits.ran

                elif fruits.distance <= 150:
                    if fruits.type == 'cherry':
                        if self.timegame % 90 == 0:
                            if fruits.x-self.player_hit_rect.x > 0:
                                fruits.x = fruits.x+fruits.ran
                            elif fruits.x-self.player_hit_rect.x < 0:
                                fruits.x = fruits.x+fruits.ran
                            if fruits.y-self.player_hit_rect.y > 0:
                                fruits.y = fruits.y-fruits.ran
                            elif fruits.y-self.player_hit_rect.y < 0:
                                fruits.y = fruits.y-fruits.ran

                    if fruits.type == 'watamelon':
                        if fruits.blink == 0:
                            Sound.Sound_blink()
                            fruits.blink = 1
                            while True:
                                fruits.x = random.choice(self.position)
                                fruits.y = random.choice(self.position)
                                if self.player_hit_rect.x - 100 <= fruits.x and self.player_hit_rect.x+150 >= fruits.x:
                                    if self.player_hit_rect.y - 100 <= fruits.y and self.player_hit_rect.y+150 >= fruits.y:
                                        print("Again random fruits")
                                else:
                                    contain_other = False
                                    fruits.rect = Rect(fruits.x, fruits.y, 10, 10)
                                    for other_fruits in self.list_fruits:
                                        if fruits.rect.colliderect(other_fruits.rect) and fruits.type != 'watamelon':
                                            contain_other = True
                                    if contain_other == False:
                                        break
                                    else:
                                        print("again")
            if fruits.x >= 711:
                fruits.x = 711
            if fruits.x <= 1:
                fruits.x = 1
            if fruits.y >= 711:
                fruits.y = 711
            if fruits.y <= 1:
                fruits.y = 1

            fruits.rect = Rect(fruits.x, fruits.y, 10, 10)

    def check_position(self):
        for fruits in self.list_fruits:
            if self.timegame % 120 == 0:
                if fruits.x <= 316:
                    if fruits.y <= 316:
                        fruits.area = 'red'
                    else:
                        fruits.area = 'blue'
                if fruits.x > 316:
                    if fruits.y <= 316:
                        fruits.area = 'green'
                    else:
                        fruits.area = 'yellow'
    def fruit_Sound(self):
        if self.intereact == True:
            if self.ftime % 60 == 0 :
                print(self.targetSoundFruit,len(self.list_fruits))
                if self.targetSoundFruit >= len(self.list_fruits):
                    self.targetSoundFruit = len(self.list_fruits)-1
                fruits = self.list_fruits[self.targetSoundFruit]
                Sound.Sound_trick()
                self.sound.Sound_fruits(fruits.type,fruits.area,fruits.Sound_distance)
                self.targetSoundFruit+=1
                if (self.targetSoundFruit == len(self.list_fruits)):
                    self.targetSoundFruit = 0
                    print('123')
                    self.intereact = False
                    print(self.intereact) 
            self.ftime += 1
                

    def gameover(self):
        if self.score == 14:
            Sound.Sound_clear()
            Sound.Sound_cleargame()
            self.screen.blit(self.clear, (0, 0))
            pygame.display.update()
            pygame.time.delay(5000)
            self.menu_run()
        else :
            Sound.Sound_stop()
            Sound.Sound_gameover()
            self.screen.blit(self.over, (0, 0))
            Sound.Sound_over()
            pygame.display.update()
            pygame.time.delay(5000)
            self.title_point = 1
            self.menu_run()



class Fruits:
    def __init__(self, x_player, y_player, list_other_fruits, fruits_num, stage):
        self.list_direction_fruits = ["top", "down", "left", "right"]
        self.direction = 0
        self.position = [0, 79, 158, 237, 316, 395, 474, 553, 632, 711]
        self.distance = 0  # ระยะห่างplayerกับผลไม้
        self.number = fruits_num
        self.ran = 79
        self.area = ''
        self.blink = 0
        self.Sound_distance = 0
        
        if (stage == 1.5):
            self.type = ['orange', 'orange']
        if (stage == 2.5):
            self.type = ['orange', 'rose_apple']
        if (stage == 3.5):
            self.type = ['orange', 'rose_apple', 'cherry']
        if (stage == 4.5):
            self.type = ['orange', 'rose_apple', 'watamelon', 'wall']
        if (stage == 5.5):
            self.type = ['orange', 'rose_apple',
                         'cherry', 'watamelon', 'wall', 'wall']
        while True:
            self.x = random.choice(self.position)
            self.y = random.choice(self.position)
            if x_player - 100 <= self.x and x_player+150 >= self.x:
                if y_player - 100 <= self.y and y_player+150 >= self.y:
                    print("Again random fruits")
            else:
                contain_other = False
                self.rect = Rect(self.x, self.y, 10, 10)
                for other_fruits in list_other_fruits:
                    if self.rect.colliderect(other_fruits.rect):
                        contain_other = True
                if contain_other == False:
                    break
                else:
                    print("again")        


class Sound():
    def __init__(self):
        self.Sound_distance = 0

    def Sound_Cursor_2():
        sound_buttom2 = pygame.mixer.Sound('sound/effect/Cursor2.mp3')
        sound_buttom2.play()

    def Sound_Cursor_1():
        sound_buttom1 = pygame.mixer.Sound('sound/effect/Cursor1.mp3')
        sound_buttom1.play()

    def BG_music_menu():
        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.load('sound/BGM/Fanfare2.mp3')
        pygame.mixer.music.play(0)

    def Sound_get():
        sound_Decision1 = pygame.mixer.Sound('sound/effect/Decision1.mp3')
        sound_Decision1.play()
    def Sound_trick():
        sound_tick = pygame.mixer.Sound('sound/effect/trick_before_say.mp3')
        sound_tick.play()

    def Sound_stop():
        pygame.mixer.music.stop()
        pygame.mixer.stop()

    def Sound_wall():
        sound_wall = pygame.mixer.Sound('sound/effect/hitwall.mp3')
        sound_wall.play()
    
    def Sound_menu():
        Sound_menu = pygame.mixer.Sound('sound/effect/menu.mp3')
        Sound_menu.set_volume(0.5)
        Sound_menu.play()

    def Sound_cleargame():
        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load('sound/BGM/clear.mp3')
        pygame.mixer.music.play(0)

    def Sound_over():
        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(0.025)
        pygame.mixer.music.load('sound/BGM/over.mp3')
        pygame.mixer.music.play(0)

    def Sound_gameover():
        Sound_gameover = pygame.mixer.Sound('sound/effect/gameover.mp3')
        Sound_gameover.play()

    def Sound_clear():
        Sound_clear = pygame.mixer.Sound('sound/effect/gameclear.mp3')
        Sound_clear.play()

    def Sound_tutor0():
        Sound_tutor0 = pygame.mixer.Sound('sound/effect/tutor0.mp3')
        Sound_tutor0.set_volume(0.5)
        Sound_tutor0.play()

    def Sound_tutor1():
        Sound_tutor1 = pygame.mixer.Sound('sound/effect/tutor1.mp3')
        Sound_tutor1.set_volume(0.5)
        Sound_tutor1.play()

    def Sound_tutor2():
        Sound_tutor2 = pygame.mixer.Sound('sound/effect/tutor2.mp3')
        Sound_tutor2.set_volume(0.5)
        Sound_tutor2.play()
        
    def Sound_tutor3():
        Sound_tutor3 = pygame.mixer.Sound('sound/effect/tutor3.mp3')
        Sound_tutor3.set_volume(0.5)
        Sound_tutor3.play()
    def Sound_tutor4():
        Sound_tutor4 = pygame.mixer.Sound('sound/effect/tutor4.mp3')
        Sound_tutor4.set_volume(0.5)
        Sound_tutor4.play()

    def Sound_startparty():
        Sound_startparty = pygame.mixer.Sound('sound/effect/startparty.mp3')
        Sound_startparty.play()

    def Sound_continue():
        Sound_continue = pygame.mixer.Sound('sound/effect/continue.mp3')
        Sound_continue.play()

    def Sound_tutorial():
        Sound_tutorial = pygame.mixer.Sound('sound/effect/tutorial.mp3')
        Sound_tutorial.play()

    def Sound_exit():
        Sound_exit = pygame.mixer.Sound('sound/effect/exit.mp3')
        Sound_exit.play()

    def Sound_stage(levels):
        level = levels
        if (level == 1):
            Sound_stage = pygame.mixer.Sound('sound/effect/stage_1.mp3')
            Sound_stage.play()
        if (level == 2):
            Sound_stage = pygame.mixer.Sound('sound/effect/stage_2.mp3')
            Sound_stage.play()
        if (level == 3):
            Sound_stage = pygame.mixer.Sound('sound/effect/stage_3.mp3')
            Sound_stage.play()
        if (level == 4):
            Sound_stage = pygame.mixer.Sound('sound/effect/stage_4.mp3')
            Sound_stage.play()
        if (level == 5):
            Sound_stage = pygame.mixer.Sound('sound/effect/stage_5.mp3')
            Sound_stage.play()

    def Sound_blink():
        Sound_blink = pygame.mixer.Sound('sound/effect/blink.mp3')
        Sound_blink.play()

    def Sound_fruits(self,type,area,Sound_distance,):
        if type == 'orange' :
            if area == 'red' :
                Sound_orangered = pygame.mixer.Sound('sound/effect/orangered.mp3')
                Sound_orangered.set_volume(Sound_distance)
                Sound_orangered.play()
            if area == 'green' :
                Sound_orangegreen = pygame.mixer.Sound('sound/effect/orangegreen.mp3')
                Sound_orangegreen.set_volume(Sound_distance)
                Sound_orangegreen.play()
            if area == 'blue' :
                Sound_orangeblue = pygame.mixer.Sound('sound/effect/orangeblue.mp3')
                Sound_orangeblue.set_volume(Sound_distance)
                Sound_orangeblue.play()
            if area == 'yellow' :
                Sound_orangeyellow = pygame.mixer.Sound('sound/effect/orangeyellow.mp3')
                Sound_orangeyellow.set_volume(Sound_distance)
                Sound_orangeyellow.play()

        if type == 'rose_apple' :
            if area == 'red' :
                Sound_roseapplered = pygame.mixer.Sound('sound/effect/roseapplered.mp3')
                Sound_roseapplered.set_volume(Sound_distance)
                Sound_roseapplered.play()
            if area == 'green' :
                Sound_roseapplegreen = pygame.mixer.Sound('sound/effect/roseapplegreen.mp3')
                Sound_roseapplegreen.set_volume(Sound_distance)
                Sound_roseapplegreen.play()
            if area == 'blue' :
                Sound_roseappleblue = pygame.mixer.Sound('sound/effect/roseappleblue.mp3')
                Sound_roseappleblue.set_volume(Sound_distance)
                Sound_roseappleblue.play()
            if area == 'yellow' :
                Sound_roseappleyellow = pygame.mixer.Sound('sound/effect/roseappleyellow.mp3')
                Sound_roseappleyellow.set_volume(Sound_distance)
                Sound_roseappleyellow.play()

        if type == 'cherry' :
            if area == 'red' :
                Sound_cherryred = pygame.mixer.Sound('sound/effect/cherryred.mp3')
                Sound_cherryred.set_volume(Sound_distance)
                Sound_cherryred.play()
            if area == 'green' :
                Sound_cherrygreen = pygame.mixer.Sound('sound/effect/cherrygreen.mp3')
                Sound_cherrygreen.set_volume(Sound_distance)
                Sound_cherrygreen.play()
            if area == 'blue' :
                Sound_cherryblue = pygame.mixer.Sound('sound/effect/cherryblue.mp3')
                Sound_cherryblue.set_volume(Sound_distance)
                Sound_cherryblue.play()
            if area == 'yellow' :
                Sound_cherryyellow = pygame.mixer.Sound('sound/effect/cherryyellow.mp3')
                Sound_cherryyellow.set_volume(Sound_distance)
                Sound_cherryyellow.play()

        if type == 'watamelon' :
            if area == 'red' :
                Sound_watermelonred = pygame.mixer.Sound('sound/effect/watermelonred.mp3')
                Sound_watermelonred.set_volume(Sound_distance)
                Sound_watermelonred.play()
            if area == 'green' :
                Sound_watermelongreen = pygame.mixer.Sound('sound/effect/watermelongreen.mp3')
                Sound_watermelongreen.set_volume(Sound_distance)
                Sound_watermelongreen.play()
            if area == 'blue' :
                Sound_watermelonblue = pygame.mixer.Sound('sound/effect/watermelonblue.mp3')
                Sound_watermelonblue.set_volume(Sound_distance)
                Sound_watermelonblue.play()
            if area == 'yellow' :
                Sound_watermelonyellow = pygame.mixer.Sound('sound/effect/watermelonyellow.mp3')
                Sound_watermelonyellow.set_volume(Sound_distance)
                Sound_watermelonyellow.play()

    def Sound_Distance(self,list_fruits,player_hit_rect):
        for fruits in list_fruits:
            fruits.distance = math.hypot(player_hit_rect.x-fruits.x,
                                             player_hit_rect.y-fruits.y)
            if fruits.distance <=600:
                fruits.Sound_distance = 0
                if fruits.distance <=480:
                    fruits.Sound_distance = 0.05
                    if fruits.distance <=360:
                        fruits.Sound_distance = 0.1
                        if fruits.distance <=240:
                            fruits.Sound_distance = 0.5
                            if fruits.distance <=120:
                                fruits.Sound_distance = 1

if __name__ == '__main__':
    try:
        Play_Game = GAME()
        Play_Game.menu_run()
    except SystemExit:
        pass