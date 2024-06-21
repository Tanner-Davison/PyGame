import pygame

pygame.init()

screen = pygame.display.set_mode((1512, 982), vsync=1)

class MyGameChar:
    x = 100 #sets x position on screen
    y = 100 #sets y position on screen
    width = 100
    height = 50
    color = (255, 0, 0)  
    speed = 20

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        MyGameChar.y -= MyGameChar.speed
    if keys[pygame.K_DOWN]:
        MyGameChar.y += MyGameChar.speed
    if keys[pygame.K_LEFT]:
        MyGameChar.x -= MyGameChar.speed
    if keys[pygame.K_RIGHT]:
        MyGameChar.x += MyGameChar.speed
    if keys[pygame.K_w]:
        MyGameChar.width


    if MyGameChar.x < 0:
       MyGameChar.x = 0
    if MyGameChar.x > screen.get_width() - MyGameChar.width:
        MyGameChar.x = screen.get_width() - MyGameChar.width
    if MyGameChar.y < 0:
        MyGameChar.y = 0
    if MyGameChar.y > screen.get_height() - MyGameChar.height-100:
        f = open("latest_moves.txt", "w")
        f.write("bottom border was hit!\n")
        f.close()
        MyGameChar.y = screen.get_height() - MyGameChar.height-100


    screen.fill((255, 255, 255)) 
    pygame.draw.rect(screen, MyGameChar.color, (MyGameChar.x, MyGameChar.y, MyGameChar.width, MyGameChar.height))

    pygame.display.flip()

pygame.quit()