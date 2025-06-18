import pygame


pygame.init

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Initials")


midasx=0
midasy=0
midasposition=(300,300,20,20)

midas=pygame.draw.rect(screen,"pink",midasposition)

FPS=30

gameloop=True
speed=10

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            midasx=1*speed
            midasy=0
        if event.key == pygame.K_LEFT:
            midasx=-1*speed
            midasy=0
        if event.key == pygame.K_UP:
            midasx=0
            midasy=-1*speed
        if event.key == pygame.K_DOWN:
            midasx=0
            midasy=1*speed

    midasposition=(midasx,midasy,20,20)
    screen.fill("white")
    midas=pygame.draw.rect(screen,"pink",midasposition)
    pygame.display.flip()
pygame.quit()


   