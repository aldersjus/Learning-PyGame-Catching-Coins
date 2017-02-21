import pygame
import random
import pickle


pygame.init()

#Sounds play when arrow keys pushed.
soundA = pygame.mixer.Sound("match1.wav")


black = [0, 0, 0]
white = [255, 255, 255]
green = [0, 255, 0]
brown = [128, 64, 0]

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collect the coins!!!!")


timer = 1000
highscore = 0
score = 0
highscore_name = ' '

player = pygame.image.load('/home/pi/pygame_images/blue_blob.png')
coin = pygame.image.load('/home/pi/pygame_images/coin.png')

player_position_x = 250
player_position_y = 300

x = [300]
y = [300]

try:
    
    load_file = open('/home/pi/Catching_coins/catch_the_coin_game_data_two.dat', 'rb')
    loaded_game_data = pickle.load(load_file)
    data = loaded_game_data
    highscore = data['highscore_save_data']
    highscore_name = data['highscore_name_save']
    load_file.close()
    

except EOFError:
    pass

class Game():

    
    def __init__(self,highscore,highscore_name):
        self.highscore = highscore
        self.highscore_name = highscore_name
        self

    def update_dictionary(self):
        data = {'highscore_save_data':'0', 'highscore_name_save':'computer'}
        data['highscore_save_data'] = highscore
        data['highscore_name_save'] = name
        save_file = open('/home/pi/Catching_coins/catch_the_coin_game_data_two.dat','wb')
        pickle.dump(data, save_file)
        save_file.close()

    def display(self,message):
        font = pygame.font.Font(None, 36)
        self.font = font
        text = font.render(message, 1, white)
        screen.blit(text, (350, 0))

    def display_two(self,message):
        font = pygame.font.Font(None, 36)
        text_two = font.render(message, 1, white)
        screen.blit(text_two, (100, 0))


    def game_over(self):
        if timer <= 0:
            if score > self.highscore:
                self.highscore = score
                self.highscore_name = name
                game.update_dictionary()
                
            font2 = pygame.font.Font(None, 36)
            my_score = self.font.render(name + "`s score " + str(score), 1, white)
            ranking = font2.render("HIGHSCORE " + " " + str(self.highscore), 1 ,white)
            ranking_name = font2.render("HIGHSCORER " + " " + str(self.highscore_name), 1 ,white)
            end = font2.render("GAME OVER", 1, white)
            screen.blit(end, (70, 190))
            screen.blit(ranking_name, (70, 250))
            screen.blit(ranking, (70, 310))
            screen.blit(my_score, (75, 370))
            if timer <= -1:
                done = True

class Coin():
   
    def __init__(self,x,y,image):
        self.image = image
        self.x = x
        self.y = y
       

    def draw(self,screen):
        self.image = coin.get_rect()
        self.image.move_ip(x[0],y[0])
        screen.blit(coin, (self.x[0], self.y[0]))
         
    def place(self):
        self.x = [50,80,200,250,280,350,430,480,500,]
        self.y = [50,80,200,250,280,350,400,450,510,]
        random.shuffle(self.x)
        random.shuffle(self.y)
        return self.x, self.y
        
        
    def coin_display(self):
        if timer == 900:
            self.place()
        elif timer == 800:
            self.place()
        elif timer == 700:
            self.place()
        elif timer == 600:
            self.place()
        elif timer == 500:
            self.place()
        elif timer == 400:
            self.place()
        elif timer == 300:
            self.place()
        elif timer == 200:
            self.place()
        elif timer == 100:
            self.place()

class Player():

    def __init__(self, player_position_x, player_position_y, image, score):
        self.image = image
        self.player_position_x = player_position_x
        self.player_position_y = player_position_y
        self.score = score
       

    def draw(self,screen):
        self.image = player.get_rect()
        self.image.move_ip(self.player_position_x, self.player_position_y)
        screen.blit(player, (self.player_position_x, self.player_position_y))
            
    def touching_coin(self):
        if  self.player_position_x + 25 >= coin_class.x[0]:
            if  self.player_position_x - 25 <= coin_class.x[0]:
               if  self.player_position_y + 25 >= coin_class.y[0]:
                   if  self.player_position_y - 25 <= coin_class.y[0]:
                        self.score += 1
                        coin_class.place()
                        self.points()
    def points(self):
        return self.score
        
    def boundary(self):
        if  self.player_position_x < 0:
             self.player_position_x = 0
        if  self.player_position_x > screen_width -  self.image.width:
             self.player_position_x = screen_width -  self.image.width
        if  self.player_position_y < 0:
             self.player_position_y = 0
        if  self.player_position_y > screen_height + 20 -  self.image.height:
             self.player_position_y = screen_height + 20 -  self.image.height

        
game_running = False

clock = pygame.time.Clock()

name = raw_input("Please enter your name: ")

game = Game(highscore,highscore_name)
coin_class = Coin(x,y,coin)
player_class = Player(250,300,player,score)


done = False

while not done:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   	    pygame.quit()

        if event.type == pygame.KEYDOWN and timer > 0:
            
            if event.key == pygame.K_LEFT:
                player_class.player_position_x -= 10
                soundA.play()
            elif event.key == pygame.K_RIGHT:
                player_class.player_position_x += 10
                soundA.play()
            elif event.key == pygame.K_UP:
                player_class.player_position_y -= 10
                soundA.play()
            elif event.key == pygame.K_DOWN:
                player_class.player_position_y += 10
                soundA.play()

            if event.key == pygame.K_SPACE:
                game_running = True

    if game_running == False:
        font = pygame.font.Font(None, 45)
        begin = font.render("PUSH SPACE", 1, white)
        begin_two = font.render("TO START", 1, white)
        screen.blit(begin, (70, 250))
        screen.blit(begin_two, (70, 300))
        
         
    if game_running == True:
        screen.fill(black) 
        game.display("Time Left:" + str(timer))
        game.display_two("Score:" + str(score))
        game.game_over()
       
        coin_class.draw(screen)
        coin_class.coin_display()
        
        
        player_class.draw(screen)
        player_class.boundary()
        player_class.touching_coin()
        
        
        
    if timer < 0:
        timer = 0
    elif timer > 0:
        timer -= 1

    score = player_class.points()    
    clock.tick(30)
    pygame.display.update()

pygame.quit()










                


