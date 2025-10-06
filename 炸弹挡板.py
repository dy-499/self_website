import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("炸弹挡板")

MyFont = pygame.font.SysFont("SimHei",30)

class Bomb:
    def __init__(self):
        self.x = random.randint(0,screen.get_width()-20*2)
        self.y = -50
        self.speed = 5
        self.radius = 20
        self.color = (230,230,50)
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
    def reset(self):
        self.x = random.randint(0,screen.get_width()-50*2)
        self.y = -50
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
    def update(self,grade):
        self.y += self.speed
        if self.y+self.radius*2 > screen.get_height():
            self.reset()
            grade -= 1
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        return grade
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x+self.radius,self.y+self.radius),self.radius)
class Baffle:
    def __init__(self):
        self.x = screen.get_width()//2
        self.y = screen.get_height()-50
        self.width = 100
        self.height = 20
        self.speed = 5
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.color = (0,0,255)
    def update(self,keys:pygame.key):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
        self.x = max(min(self.x,screen.get_width()-self.width),0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)

bomb = Bomb()
baffle = Baffle()

heart = 5
grade = 0
game_over = True

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    game_over = True
                    grade = 0
                    heart = 5
                    bomb.speed = 5
    screen.fill((0,0,0))
    if game_over:
        keys = pygame.key.get_pressed()
        baffle.update(keys)
        heart = bomb.update(heart)
        if bomb.rect.colliderect(baffle.rect):
            baffle.color = (0,255,0)
            bomb.speed += 0.1
            grade += bomb.speed
            bomb.reset()
        else:
            baffle.color = (0,0,255)
        bomb.draw()
        baffle.draw()
        heart_text = MyFont.render("生命："+str(heart),True,(255,255,255))
        speed_text = MyFont.render("小球速度："+str(round(bomb.speed,2)),True,(255,255,255))
        screen.blit(heart_text,(0,0))
        screen.blit(speed_text,(0,screen.get_height()-30))
    if heart <= 0:
        game_over = False
    if not game_over:
        text = MyFont.render("按空格键重新开始",True,(255,255,255))
        screen.blit(text,(screen.get_width()//2-text.get_width()//2,screen.get_height()//2-text.get_height()//2))
    grade_text = MyFont.render("分数：" + str(round(grade, 2)), True, (255, 255, 255))
    screen.blit(grade_text, (screen.get_height() - 200, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()