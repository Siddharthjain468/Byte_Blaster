import pygame 
import create_button
# 6 12
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("'Main menu")

game_pause = False

font = pygame.font.SysFont("arialblack", 40)

text_col = (255, 255, 155)

resume_image = pygame.image.load("images\play_pasue.png").convert_alpha()
resume_button = create_button.Button(330, 150, resume_image, 0.2)

exit_image = pygame.image.load("images\exit.png").convert_alpha()
exit_button = create_button.Button(320, 270, exit_image, 0.2)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while (run):

    screen.fill((52, 78, 91))
    if game_pause == True:
        if resume_button.draw(screen):
            game_pause = False 
        if exit_button.draw(screen):
            run = False
            break
    else:
        draw_text("Press SPACE to pause", font, text_col, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()