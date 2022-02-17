import time
import pygame
pygame.init()

orange =(255,171,0)#Game over
green =(107,250,150)#snake
black =(0,0,0)#score
blue =(91,57,250)#food
pink =(255,0,230)#background
dis_width =400
dis_height=300
dis =pygame.display.set_mode((400,300))


pygame.display.set_caption("Snake game by Rafa")
game_over=False

x1=dis_width/2
y1=dis_height/2
x1_change=0
y1_change=0

snake_block =10
snake_speed =30

clock = pygame.time.Clock()
font_style =pygame.font.SysFont(None,50)

def message(msg,color):
    msg=font_style.render(msg,True,color)
    dis.blit(msg, [dis_width/4, dis_height/2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change =snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change =0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    if x1>dis_width or x1<0 or y1 >dis_height or y1<0:
        game_over=True
    x1+= x1_change
    y1+= y1_change
    dis.fill(pink)
    pygame.draw.rect(dis, green,[200,150,snake_block,snake_block])    
    pygame.display.update()

    clock.tick(snake_speed)
message("You lost", orange)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()