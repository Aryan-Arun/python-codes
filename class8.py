import pygame


pygame.init()

screen=pygame.display.set_mode((1500,600))
pygame.display.set_caption("initials")


gameloop=True
while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    v=pygame.draw.rect(screen,"blue",(300,50,200,20))
    x=pygame.draw.rect(screen,"blue",(300,50,20,200))
    y=pygame.draw.rect(screen,"blue",(300,250,200,20))
    h=pygame.draw.rect(screen,"blue",(500,250,20,200))
    h=pygame.draw.rect(screen,"blue",(300,450,200,20))



    pygame.display.flip()

pygame.quit()