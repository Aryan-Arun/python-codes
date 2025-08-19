import pygame


pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Initials")


midasx=300
midasy=300

midasposition=(midasx,midasy,20,20)
midas=pygame.draw.rect(screen,"pink",midasposition)




block1=pygame.draw.rect(screen,"blue",(50,50,50,50))
block2=pygame.draw.rect(screen,"red",(500,500,50,50))
block3=pygame.draw.rect(screen,"green",(50,500,50,50))
block4=pygame.draw.rect(screen,"grey",(500,50,50,50))


FPS=60
clock=pygame.time.Clock()





gameloop=True
speed=10

midasdx=0
midasdy=0

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            midasdx=1*speed
            midasdy=0
        if event.key == pygame.K_LEFT:
            midasdx=-1*speed
            midasdy=0
        if event.key == pygame.K_UP:
            midasdx=0
            midasdy=-1*speed
        if event.key == pygame.K_DOWN:
            midasdx=0
            midasdy=1*speed
    midasx=midasx+midasdx
    midasy=midasy+midasdy
    midasposition=(midasx,midasy,20,20)
    screen.fill("white")
    midas=pygame.draw.rect(screen,"pink",midasposition)
    block1=pygame.draw.rect(screen,"blue",(50,50,50,50))
    block2=pygame.draw.rect(screen,"red",(500,500,50,50))
    block3=pygame.draw.rect(screen,"green",(50,500,50,50))
    block4=pygame.draw.rect(screen,"grey",(500,50,50,50))
    if midas.colliderect(block1):
        block1=pygame.draw.rect(screen,"gold",(50,50,50,50))
        pygame.display.update()
    if midas.colliderect(block2):
        block2=pygame.draw.rect(screen,"gold",(500,500,50,50))
        pygame.display.update()
    if midas.colliderect(block3):
        block3=pygame.draw.rect(screen,"gold",(50,500,50,50))
        pygame.display.update()
    if midas.colliderect(block4):
        block4=pygame.draw.rect(screen,"gold",(500,50,50,50))
        pygame.display.update()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
