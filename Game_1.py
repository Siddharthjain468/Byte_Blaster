import pygame
import time
import random
pygame.font.init()
WIDTH, HEIGHT = 1024, 768

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test_game")

BG = pygame.transform.scale(pygame.image.load("bg_1.jpg"), (WIDTH,HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 20)

def draw(player, elapsed_time, stars):
    WIN.blit(BG,(0,0))
    time_text = FONT.render(f"Time:{int(elapsed_time//3600)}h:{int((elapsed_time%3600)//60)}m:{int(elapsed_time%60)}s", 1, "white")
    WIN.blit(time_text, (WIDTH-200,10))
    pygame.draw.rect(WIN, "white", player)
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    pygame.display.update()

def main():
    run=True
    player = pygame.Rect(200, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    hit = False

    stars = []

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment-50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL>=0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("YOU LOST!!!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2-lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)
          
            WIN.fill(pygame.Color("black"))
            continue_or_not = FONT.render("1.Continue \n 2.Exit", 1, "white")
            WIN.blit(continue_or_not, (WIDTH/2-continue_or_not.get_width()/2, HEIGHT/2 - continue_or_not.get_height()/2))
            pygame.display.update()
            # pygame.time.delay(4000)

            pygame.event.clear()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.K_1:
                    main()
                    continue
                if event.type == pygame.K_2:
                    print("in else if")
                    pygame.quit()
                    break

        draw(player, elapsed_time, stars)
    pygame.quit() 

if __name__ == "__main__":
    main()
