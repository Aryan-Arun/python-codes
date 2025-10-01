import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("tune tap challenge")

gameloop=True
FPS=60

speed=5

mallet_x=300
mallet_y=300


mallet_dx=0
mallet_dy=0


mallet=pygame.draw.rect(screen,"white",(mallet_x,mallet_y,20,20))

clock=pygame.time.Clock()



r1=pygame.draw.rect(screen,"red",(10,50,60,400))
r2=pygame.draw.rect(screen,"orange",(20,50,60,350))
r3=pygame.draw.rect(screen,"yellow",(170,50,60,300))
r4=pygame.draw.rect(screen,"green",(250,50,60,250))
r5=pygame.draw.rect(screen,"blue",(330,50,60,200))
r6=pygame.draw.rect(screen,"purple",(410,50,60,150))
r7=pygame.draw.rect(screen,"violet",(490,50,60,100))
r8=pygame.draw.rect(screen,"grey",(570,50,60,50))


s1=pygame.mixer.Sound("note1.mp3")
s2=pygame.mixer.Sound("note2.mp3")
s3=pygame.mixer.Sound("note3.mp3")
s4=pygame.mixer.Sound("noteA.mp3")
s5=pygame.mixer.Sound("noteB.mp3")
s6=pygame.mixer.Sound("noteC.mp3")
s7=pygame.mixer.Sound("noteD.mp3")
s8=pygame.mixer.Sound("noteE.mp3")







while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False


    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            mallet_dx=1*speed
            mallet_dy=0
        if event.key == pygame.K_LEFT:
            mallet_dx=-1*speed
            snake_dy=0
        if event.key == pygame.K_UP:
            mallet_dx=0
            mallet_dy=-1*speed
        if event.key == pygame.K_DOWN:
            mallet_dx=0
            mallet_dy=1*speed
    mallet_x=mallet_x+mallet_dx
    mallet_y=mallet_y+mallet_dy

    r1=pygame.draw.rect(screen,"red",(10,50,60,400))
    r2=pygame.draw.rect(screen,"orange",(90,50,60,350))
    r3=pygame.draw.rect(screen,"yellow",(170,50,60,300))
    r4=pygame.draw.rect(screen,"green",(250,50,60,250))
    r5=pygame.draw.rect(screen,"blue",(330,50,60,200))
    r6=pygame.draw.rect(screen,"purple",(410,50,60,150))
    r7=pygame.draw.rect(screen,"violet",(490,50,60,100))
    r8=pygame.draw.rect(screen,"grey",(570,50,60,50))

    mallet=pygame.draw.rect(screen,"white",(mallet_x,mallet_y,20,20))
    if mallet.colliderect(r1):
        s1.play()
    if mallet.colliderect(r2):
        s2.play()
    if mallet.colliderect(r3):
        s3.play()
    if mallet.colliderect(r4):
        s4.play()
    if mallet.colliderect(r5):
        s5.play()
    if mallet.colliderect(r6):
        s6.play()
    if mallet.colliderect(r7):
        s7.play()
    if mallet.colliderect(r8):
        s8.play()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

    



