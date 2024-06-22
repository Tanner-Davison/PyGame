import pygame

pygame.init()

screen = pygame.display.set_mode((1512, 982), vsync=1)

class MainChar:
    x = 100 
    y = 100 
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
        MainChar.y -= MainChar.speed
    if keys[pygame.K_DOWN]:
        MainChar.y += MainChar.speed
    if keys[pygame.K_LEFT]:
        MainChar.x -= MainChar.speed
    if keys[pygame.K_RIGHT]:
        MainChar.x += MainChar.speed
    if keys[pygame.K_w]:
        MainChar.width


    if MainChar.x < 0:
       MainChar.x = 0
    if MainChar.x > screen.get_width() - MainChar.width:
        MainChar.x = screen.get_width() - MainChar.width
    if MainChar.y < 0:
        MainChar.y = 0
    if MainChar.y > screen.get_height() - MainChar.height-100:
        f = open("latest_moves.txt", "w")
        f.write("bottom border was hit!\n")
        f.close()
        MainChar.y = screen.get_height() - MainChar.height-100


    screen.fill((255, 255, 255)) 
    pygame.draw.rect(screen, MainChar.color, (MainChar.x, MainChar.y, MainChar.width, MainChar.height))

    pygame.display.flip()
print('wow')
pygame.quit()