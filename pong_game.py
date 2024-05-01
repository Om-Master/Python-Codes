import pygame
import random
import math
from PIL import ImageFilter, Image

pygame.init()

width = 700
height = 470
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("Arial", 50)


def draw_text(text, font, color, destination):
    img = font.render(text, True, color)
    screen.blit(img, destination)


def game_loop():
    divider = pygame.Surface((10, 50))
    divider.fill(pygame.Color("gray90"))
    text_divider = pygame.Surface((700, 10))
    text_divider.fill(pygame.Color("gray60"))
    offsets = [(-1, 0), (1, 0)]

    ball = pygame.Surface((16, 16))
    ball.fill(pygame.Color("gray60"))
    ball_y = int(random.randrange(70, 436))
    ball_x = width / 2 - ball.get_width()/2
    ball_velocity_y = random.choice([0, 1, 2, 3, 4])
    ball_velocity_x = 4

    player_board_y = (height/2) - 50
    player_height = 100
    player_width = 15
    player_board_x = 60
    player_score = 0
    comp_board_y = (height/2) - 50
    comp_height = 100
    comp_width = 15
    comp_board_x = width - 75
    comp_velocity = 4
    comp_score = 0

    win_lose = ["You Win", "You Lose"]

    collision_num = random.choice([1, 2, 3, 4])

    key_pressed_up = False
    key_pressed_down = False
    game_over = False
    running = True
    while running:
        if game_over:
            image = pygame.image.load("back_screen.png")
            button = pygame.Surface((250, 80))
            button.fill(pygame.Color("gray32"))
            if player_score == 10:
                win_text = win_lose[0]
            else:
                win_text = win_lose[1]
            running_in = True
            while running_in:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_in = False
                        pygame.quit()
                        quit()

                if pygame.mouse.get_pressed()[0] == True:
                    if (pygame.mouse.get_pos()[0] > width/2 - button.get_width()/2) and (pygame.mouse.get_pos()[0] < width/2 + button.get_width()/2) and (pygame.mouse.get_pos()[1] > height/2) and (pygame.mouse.get_pos()[1] < height/2 + button.get_height()):
                        button.fill(pygame.Color("gray"))
                        game_over = False
                        running_in = False
                        player_score = 0
                        comp_score = 0
                else:
                    button.fill(pygame.Color("gray32"))

                screen.blit(image, (0,0))
                draw_text(win_text, pygame.font.SysFont("Arial", 80), pygame.Color("gray60"), (width/2-150, height/2-100))

                screen.blit(button, (width/2 - button.get_width()/2, height/2))
                draw_text("Play Again", pygame.font.SysFont("Arial", 40), pygame.Color("gray10"), (width/2 - 90, height/2 + 20))

                pygame.display.flip()
                clock.tick(60)
        else:
            screen.fill(pygame.Color("gray5"))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        key_pressed_up = True
                    if event.key == pygame.K_DOWN:
                        key_pressed_down = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        key_pressed_up = False
                    if event.key == pygame.K_DOWN:
                        key_pressed_down = False

            if player_board_y > 70:
                if key_pressed_up:
                    player_board_y -= 10

            if player_board_y < height - 100:
                if key_pressed_down:
                    player_board_y += 10

            # Collision logic
            player_collisions_y = list(range(int(player_board_y), int(player_board_y + player_height + 1)))
            player_collisions_x = player_board_x + player_width
            comp_collisions_y = list(range(int(comp_board_y), int(comp_board_y + comp_height + 1)))
            comp_collisions_x = comp_board_x
            board_col1 = 70
            board_col2 = 470

            # Computer logic
            if (comp_board_y <= 70) or (comp_board_y + comp_width >= 270):
                if (ball_y > comp_board_y) and (ball_y < comp_board_y + comp_height):
                    comp_velocity = 0
                else:
                    if ball_y < comp_board_y + comp_height/2:
                        comp_velocity = (-(ball_velocity_y / 1.2))
                    elif ball_y > comp_board_y + comp_height/2:
                        comp_velocity = ball_velocity_y / 1.2
            else:
                if (ball_y > comp_board_y + comp_height/2) and (ball_y < comp_board_y + comp_height/2):
                    comp_velocity = 0
                else:
                    if ball_y < comp_board_y + comp_height/2:
                        comp_velocity = (-ball_velocity_y/1.5) - 7
                    elif ball_y > comp_board_y + comp_height/2:
                        comp_velocity = (ball_velocity_y/1.5) + 7
            comp_board_y += comp_velocity

            if ((int(ball_y + (ball.get_height()/2)) in player_collisions_y) and (int(ball_x) >= player_collisions_x) and (int(ball_x) <= player_collisions_x + comp_width) and (collision_num == 2)) or ((ball_y <= board_col1) and (collision_num == 3)):
                collision_num = 1
                ball_velocity_x = 10
            elif ((ball_y <= 70) and (collision_num == 4)) or ((int(ball_y + (ball.get_height()/2)) in comp_collisions_y) and (int(ball_x) >= comp_collisions_x) and (int(ball_x) <= comp_collisions_x + comp_width) and (collision_num == 1)):
                collision_num = 2
                ball_velocity_x = 10
            elif ((ball_y + ball.get_height() > height) and (collision_num == 1)) or ((int(ball_y + (ball.get_height()/2)) in player_collisions_y) and (int(ball_x) >= player_collisions_x) and (int(ball_x) <= player_collisions_x + comp_width) and ((collision_num == 4) or (collision_num == 0))):
                collision_num = 3
                ball_velocity_x = 10
            elif ((int(ball_y + (ball.get_height()/2)) in comp_collisions_y) and (int(ball_x) >= comp_collisions_x) and (int(ball_x) <= comp_collisions_x + comp_width) and (collision_num == 3)) or ((ball_y + ball.get_height() > height) and (collision_num == 2)):
                collision_num = 4
                ball_velocity_x = 10

            # increase ball_velocity_y
            if (ball_y + (ball.get_height()/2) in player_collisions_y) and (ball_x <= player_collisions_x) and (ball_x >= player_collisions_x - player_width) and ((collision_num == 2) or (collision_num == 4)):
                if ((ball_y + ball.get_height()/2) - (player_board_y + player_height/2))/5 > 0:
                    collision_num = 1
                    ball_velocity_y = math.ceil(((ball_y + ball.get_height()/2) - (player_board_y + player_height/2))/5)
                elif ((ball_y + ball.get_height()/2) - (player_board_y + player_height/2))/5 < 0:
                    collision_num = 3
                    ball_velocity_y = -(math.ceil(((ball_y + ball.get_height()/2) - (player_board_y + player_height/2))/5))
            elif (ball_y + (ball.get_height()/2) in comp_collisions_y) and (ball_x <= comp_collisions_x) and (ball_x >= comp_collisions_x - comp_width) and ((collision_num == 1) or (collision_num == 3)):
                if ((ball_y + ball.get_height()/2) - (comp_board_y + comp_height/2))/5 > 0:
                    collision_num = 2
                    ball_velocity_y = math.ceil(((ball_y + ball.get_height()/2) - (comp_board_y + comp_height/2))/5)
                elif ((ball_y + ball.get_height()/2) - (comp_board_y + comp_height/2))/5 < 0:
                    collision_num = 4
                    ball_velocity_y = -(math.ceil(((ball_y + ball.get_height()/2) - (comp_board_y + comp_height/2))/5))

            if collision_num % 4 == 0:
                ball_x -= ball_velocity_x
                ball_y -= ball_velocity_y
            if collision_num % 4 == 1:
                ball_x += ball_velocity_x
                ball_y += ball_velocity_y
            if collision_num % 4 == 2:
                ball_x -= ball_velocity_x
                ball_y += ball_velocity_y
            if collision_num % 4 == 3:
                ball_x += ball_velocity_x
                ball_y -= ball_velocity_y

            if ball_x < -200 or ball_x > width + 200:
                if ball_x < 0:
                    comp_score += 1
                if ball_x > width:
                    player_score += 1
                if (comp_score == 10) or (player_score == 10):
                    game_over = True
                ball_y = int(random.randrange(70, 436))
                ball_x = width / 2 - ball.get_width() / 2
                collision_num = random.choice([1, 2, 3, 4])
                ball_velocity_y = random.choice([1, 2, 3, 4, 5])
                ball_velocity_x = 4

            # players dash_board on screen
            pygame.draw.rect(screen, pygame.Color("gray60"), (player_board_x, player_board_y, player_width, player_height))
            pygame.draw.rect(screen, pygame.Color("gray60"), (comp_board_x, comp_board_y, comp_width, comp_height))

            # dividers on screen
            screen.blit(divider, (width / 2 - divider.get_width()/2, 70))
            screen.blit(divider, (width / 2 - divider.get_width()/2, 157.5))
            screen.blit(divider, (width / 2 - divider.get_width()/2, 245))
            screen.blit(divider, (width / 2 - divider.get_width()/2, 332.5))
            screen.blit(divider, (width / 2 - divider.get_width()/2, 420))

            # text on screen
            screen.blit(text_divider, (0, 60))
            for offset in offsets:
                draw_text("You", font1, pygame.Color("gray60"), (10 + offset[0], 5 + offset[1]))
                draw_text("Computer", font1, pygame.Color("gray60"), (470 + offset[0], 5 + offset[1]))

            # ball on screen
            screen.blit(ball, (ball_x, ball_y))

            # scores on screen
            draw_text(str(player_score), pygame.font.SysFont("Arial", 60), pygame.Color("gray60"), (270, 75))
            draw_text(str(comp_score), pygame.font.SysFont("Arial", 60), pygame.Color("gray60"), (400, 75))

            if game_over:
                pygame.image.save(screen, "back_screen.png")
                original_screen = Image.open("back_screen.png")
                blurred_screen = original_screen.filter(ImageFilter.GaussianBlur(10))
                blurred_screen.save("back_screen.png")

            pygame.display.flip()
            clock.tick(60)


game_loop()
pygame.quit()
quit()
