import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Initials")



gameloop=True
while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    p=pygame.draw.rect(screen,"blue",(300,50,20,400))
    x=pygame.draw.rect(screen,"blue",(600,50,20,400))
    y=pygame.draw.rect(screen,"blue",(300,50,300,20))
    w=pygame.draw.rect(screen,"blue",(300,180,300,20))


    pygame.display.flip()

pygame.quit()

