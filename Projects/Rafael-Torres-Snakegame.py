import pygame
pygame.init()

orange =(255,171,0)#Game over
green =(107,250,150)#snake
black =(0,0,0)#score
blue =(91,57,250)#food
pink =(255,0,2300)#background

dis =pygame.display.set_mode((400,300))


pygame.display.set_caption("Snake game by Rafa")
game_over=False
x1=150
y1=150
x1_change=0
y1_change=0
clock =pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KeyDown:
            
            if event.type == pygame.K_LEFT:
                x1_change =-10
                y1_change = 0
            elif event.type == pygame.K_RIGHT:
                x1_change =10
                y1_change = 0
            elif event.type == pygame.K_UP:
                x1_change =0
                y1_change = 10
            elif event.type == pygame.K_DOWN:
                x1_change = 0
                y1_change = -10

    x1+= x1_change
    y1+= y1_change
    dis.fill(pink)
    pygame.draw.rect(dis, green,[200,150,10,10])    
    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()