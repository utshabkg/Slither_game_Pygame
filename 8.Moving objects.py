import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0

while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10   #if change is not given, holding the keys doesn't make any work 
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
            if event.key == pygame.K_UP:
                lead_y_change -= 10
            if event.key == pygame.K_DOWN:
                lead_y_change += 10
    lead_x += lead_x_change
            
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,100])
    pygame.draw.rect(gameDisplay, red, [lead_x,lead_y,10,10])

    pygame.display.update()


pygame.quit()
quit()
