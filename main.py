import pygame 
import sys
from pygame.locals import* 
import time 
import random

pygame.init() 

#Screen dimensions 
WIDTH = 800
HEIGHT = 600 
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Christmas Present Catcher")

RED = (255,0,0)

santa_image = pygame.image.load("santa.png")
santa_image = pygame.transform.scale(santa_image, (60, 80))  # width=60, height=80
gift_image = pygame.image.load("giftbox.png")
gift_image =pygame.transform.scale(gift_image, (30,30)) 

class Santa:
    #constructor - use when you want to create(initialize)new objects 
    def __init__(self):
        self.width = 60
        self.height = 80
        self.x = WIDTH // 2 - self.width // 2 #middle of screen
        self.y = HEIGHT - self.height - 10   #near bottom of screen
        self.speed = 5 #santa's position
        self.score = 0 
    
    def move(self,direction):
        if (direction == "left") and self.x > 0:
            self.x -= self.speed 
        if (direction == "right")and self.x < WIDTH - self.width:
            self.x += self.speed
    
    def draw(self):
        window.blit(santa_image,(self.x,self.y))

#Present class 
class Present:
    #constructor
    def __init__(self):
        self.width = 30 
        self.height = 30 
        self.x = random.randint(0,WIDTH - self.width)
        self.y = -self.height #above the screen
        self.speed = random.randint(3,7)
        
    def move(self):
        self.y += self.speed 
        
    def draw(self):
        window.blit(gift_image,(self.x,self.y))
        

santa = Santa()
presents = [] 
spawn_time = 0 
clock = pygame.time.Clock()
font = pygame.font.Font(None,36)

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movements 
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT]):
        santa.move("left")
    if (keys[pygame.K_RIGHT]):
        santa.move("right")
            
    # Create new presents 
    if random.random() <0.02:
        presents.append(Present())
    
    # Presents 
    for present in presents[:]:
        present.move()
        
        if(present.y + present.height > santa.y 
            and present.x < santa.x + santa.width 
            and present.x + present.width > santa.x):
            santa.score +=1 
            presents.remove(present)
            
        elif present.y > HEIGHT:
            presents.remove(present)
    
    #Fill screen 
    window.fill((255,255,255))
    santa.draw()
    for present in presents:
        present.draw()

    # Score
    score_text = font.render(f"Presents collected: {santa.score}",True, RED)
    window.blit(score_text,(10,10))
    
    pygame.display.update()
    clock.tick(30)


pygame.quit() 