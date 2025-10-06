import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("贪吃蛇游戏")

green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
white = (0,0,255)

MyFont = pygame.font.SysFont("SimHei",30)

size = 20
width,height = screen.get_width()//size,screen.get_height()//size
snack = [(width//2,height//2)]
up,down,left,right = (0,-1),(0,1),(-1,0),(1,0)
rection = right
text = ">"
body_text = "-"
food = (random.randint(0,width-1), random.randint(0,height-1))
while food in snack:
    food = (random.randint(0,width-1),random.randint(0,height-1))
state = "play"

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rection != down:
                rection = up
            elif event.key == pygame.K_DOWN and rection != up:
                rection = down
            elif event.key == pygame.K_LEFT and rection != right:
                rection = left
            elif event.key == pygame.K_RIGHT and rection != left:
                rection = right
            if event.key == pygame.K_SPACE and state == "lose":
                state = "play"
    screen.fill(black)
    head = (snack[0][0] + rection[0],snack[0][1] + rection[1])
    snack.insert(0,head)
    if head[0] < 0 or head[0] >= width or head[1] <0 or head[1] >= height or head in snack[1:]:
        state = "lose"
    if head == food :
        while True:
            food = (random.randint(0,width-1),random.randint(0,height-1))
            if food not in snack:
                break
    else:
        snack.pop()
    body = snack[1:]
    for rect in snack:
        pygame.draw.rect(screen,green,(rect[0]*size,rect[1]*size,size,size))
    pygame.draw.rect(screen,red,(food[0]*size,food[1]*size,size,size))
    
    if rection == right:
        text = ">"
        body_text = "-"
    elif rection == left:
        text = "<"
        body_text = "-"
    elif rection == up:
        text = "∧"
        body_text = "|"
    elif rection == down:
        text = "∨"
        body_text = "|"
    rec_text = MyFont.render(text,True,white)
    screen.blit(rec_text,(head[0]*size+size//2-rec_text.get_width()//2,head[1]*size+size//2-rec_text.get_height()//2))
    if body:
        body_surface = MyFont.render(body_text,True,white)
        for i in body:
            screen.blit(body_surface,(i[0]*size+size//2-body_surface.get_width()//2,i[1]*size+size//2-body_surface.get_height()//2))
    if state == "lose":
        screen.fill(black)
        lose_text = "You Lose!\n按空格继续"
        lose_surface = MyFont.render(lose_text,True,white)
        screen.blit(lose_surface,(screen.get_width()//2-lose_surface.get_width()//2,screen.get_height()//2-lose_surface.get_height()//2))
        snack = [(width//2,height//2)]
        food = (random.randint(0,width-1), random.randint(0,height-1))
        while food in snack:
            food = (random.randint(0,width-1),random.randint(0,height-1))
    pygame.display.update()
    clock.tick(5)
pygame.quit()