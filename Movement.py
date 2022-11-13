import pygame

# Init
pygame.init()

# Setup window and title
WIN_SIZE = (700,700)
WIN = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Basic Movements')

# FPS
FPS = 60
clock = pygame.time.Clock()

# Load Image/
PLAYER = pygame.image.load('Assets\PacMan.png')
# Scale image (optional)
PLAYER = pygame.transform.scale(PLAYER, (200,160))


def handle_keys(keys: list, pos: pygame.Rect, SPEED):
    
    if keys[pygame.K_w]: # Forward
        # If W is pressed
        if (pos.y - SPEED >= 0): # top wall
            pos.y -= SPEED
    
    if keys[pygame.K_a]:
        # If A is pressed
        if (pos.x - SPEED >= 0): # Left wall
            pos.x -= SPEED
     
    if keys[pygame.K_s]:
        # If S is pressed
        if (pos.y + SPEED <= (700-160)): # bottom wall
            pos.y += SPEED
    
    if keys[pygame.K_d]:
        # If D is pressed
        if (pos.x + SPEED <= (700-200)): # right wall
            pos.x += SPEED

    if keys[pygame.K_UP]:
        if (SPEED +1) < 50:
            SPEED += 1
            print('up - ' + str(SPEED))

    if keys[pygame.K_DOWN]:
        if (SPEED -1) >0:
            SPEED -= 1
            print('down - ' + str(SPEED))

    return SPEED
        
def draw(pos: pygame.Rect):
    # Fill white
    WIN.fill((255,255,255))
    # Blit player
    WIN.blit(PLAYER, pos)

    # Update
    pygame.display.update()
def main():
    PLAYER_RECT = PLAYER.get_rect(center=(
        WIN.get_width()//2,
        WIN.get_height()//2
    ))
    run = True
    #
    SPEED = 2;
    while run:
        # Tick at n FPS
        clock.tick(FPS)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Get keys pressed
        KEYS_PRESSED = pygame.key.get_pressed()
        # Handle the keys
        SPEED = handle_keys(KEYS_PRESSED, PLAYER_RECT, SPEED)
        # Call draw function
        draw(PLAYER_RECT)
    # Quit
    pygame.quit()
if __name__ == '__main__':
    main()
