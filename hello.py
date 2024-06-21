import pygame

pygame.init()

screen = pygame.display.set_mode((1512, 982), vsync=1)

rect_x = 100
rect_y = 100
rect_width = 100
rect_height = 50
rect_color = (255, 0, 0)  # Red
rect_speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed


    if rect_x < 0:
        rect_x = 0
    if rect_x > screen.get_width() - rect_width:
        rect_x = screen.get_width() - rect_width
    if rect_y < 0:
        rect_y = 0
    if rect_y > screen.get_height() - rect_height-100:
        rect_y = screen.get_height() - rect_height-100


    screen.fill((255, 255, 255)) 
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

pygame.quit()