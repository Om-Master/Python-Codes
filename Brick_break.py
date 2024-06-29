import pygame
import random
import asyncio

pygame.init()
width = 385
height = 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def draw_text(text,size,color,x,y,bold = False):
    font = pygame.font.SysFont("arial",size)
    if bold:
        font.set_bold(True)
    text_img = font.render(text, True, color)
    screen.blit(text_img,(x,y))

def gameover(win):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        screen.fill((35, 226, 255))
        if win:
            draw_text("Game Over!!",40,(31, 197, 109),80,100,bold=True)
            draw_text("You Won!!",40,(31, 197, 109),90,150,bold=True)
            draw_text("Press Space Bar To",40,(31, 197, 109),10,200,bold=True)
            draw_text("Play Again",40,(31, 197, 109),80,250,bold=True)
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                gameloop()
        else:
            draw_text("Game Over!!",40,(108,108,108),80,100,bold=True)
            draw_text("You Lost!!",40,(108,108,108),90,150,bold=True)
            draw_text("Press Space Bar To",40,(108,108,108),10,200,bold=True)
            draw_text("Play Again",40,(108,108,108),80,250,bold=True)
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                gameloop()
        pygame.display.flip()
        clock.tick(60)
            

def gameloop():
    #defining variables

    brick_width = 90
    brick_height = 30
    brick = pygame.Surface((brick_width, brick_height),)
    brick.fill((7, 13, 131))

    brick_mask = pygame.mask.from_surface(brick)
    brick_masks = pygame.Mask.to_surface(brick_mask)

    level1 = [(5, 50), (5+brick_width + 5, 50), (5 + brick_width + 5 + brick_width+5, 50), (5+brick_width+5
            +brick_width+5+brick_width+5, 50),

            (5, 50+brick_height+5), (5+brick_width + 5, 50+brick_height+5), (5 + brick_width + 5 + brick_width+5, 50+brick_height+5), (5+brick_width+5+brick_width+5+brick_width+5, 50+brick_height+5),

            (5, 50+brick_height+5+brick_height+5), (5+brick_width + 5, 50+brick_height+5+brick_height+5), (5 + brick_width + 5 + brick_width+5, 50+brick_height+5+brick_height+5), (5+brick_width+5+brick_width+5+brick_width+5, 50+brick_height+5+brick_height+5),

            (5, 50+brick_height+5+brick_height+5+brick_height+5), (5+brick_width + 5, 50+brick_height+5+brick_height+5+brick_height+5), (5 + brick_width + 5 + brick_width+5, 50+brick_height+5+brick_height+5+brick_height+5), (5+brick_width+5+brick_width+5+brick_width+5, 50+brick_height+5+brick_height+5+brick_height+5)]


    board = pygame.Surface((100, 20))
    board_x = width/2 - 50
    board_y = 350
    board_mask = pygame.mask.from_surface(board)
    left = False
    right = False

    ball_x = width/2
    ball_y = 300
    ball_radius = 15
    ball = pygame.draw.circle

    ball_surface = pygame.Surface((30,30))
    ball_surface.set_alpha(0)
    ball_surface_mask = pygame.mask.from_surface(ball_surface)

    ball_velo_x = random.choice([-2,2])
    ball_velo_y = -3
    ball_xs = [(10,-5),(20,-4),(30,-3),(40,-2),(50,-1),(60,1),(70,2),(80,3),(90,4),(100,5)]

    game_start = False

    count_gameover = 0
    win = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        left = True if key[pygame.K_LEFT] else False
        right = True if key[pygame.K_RIGHT] else False

        screen.fill((35, 226, 255))

        for i in level1:
            screen.blit(brick, i)
        
        if (board_x >= 0):
            if left:
                board_x -= 10
        if (board_x+100 <= width):
            if right:
                board_x += 10

        #displaying ball on screen
        screen.blit(ball_surface, (ball_x-15, ball_y-15))
        ball(screen,(245, 255, 54), (ball_x, ball_y), ball_radius)

        #ball's movements
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            game_start = True
            
        if game_start:
            ball_x += ball_velo_x
            ball_y += ball_velo_y
        else:
            draw_text("Press \"Space\" to Start",35,(107, 0, 201),20,200)
            draw_text("The Game!!",35,(107, 0, 201),100,240)

        screen.blit(board, (board_x, board_y))
        
        #ball collision with bricks
        for i in level1:
            overlap = brick_mask.overlap(ball_surface_mask,(ball_x - i[0] - 15,ball_y - i[1] - 15))
            if overlap is not None:
                if (overlap[0] >= 0) and (overlap[1] >= 25):
                    ball_velo_y = -ball_velo_y
                    level1.remove(i)
                elif (overlap[0] <= 1) and (overlap[1] >= 0):
                    ball_velo_x = - ball_velo_x
                    level1.remove(i)
                elif (overlap[0] <= 85) and (overlap[1] >= 0):
                    ball_velo_x = -ball_velo_x
                    level1.remove(i)
                elif (overlap[0] >= 0) and (overlap[1] <= 0):
                    ball_velo_y = -ball_velo_y
                    level1.remove(i)

        #board overlap
        board_lap = board_mask.overlap(ball_surface_mask,(ball_x - board_x - 15, ball_y - board_y - 15))
        if board_lap is not None:
            for i in ball_xs:
                if board_lap[0] == 50 and board_lap[1] >= 0:
                    ball_velo_y = -ball_velo_y
                    ball_velo_x = 0
                    break
                elif board_lap[0] <= i[0] and board_lap[1] >= 0 and board_lap[0] >= i[0]-10:
                    ball_velo_y = -ball_velo_y
                    ball_velo_x = i[1]
                    break
        
        #wall touch
        if ball_x - 15 <= 0:
            ball_velo_x = -ball_velo_x
        elif ball_x + 15 >= width:
            ball_velo_x = -ball_velo_x
        elif ball_y - 15 <= 0:
            ball_velo_y = -ball_velo_y

        #gameover
        if level1 == []:
            win = True
            count_gameover+=1
            if count_gameover == 60:
                running = False
                gameover(win)
        elif ball_y + 15 >= height:
            win = False
            count_gameover+=1
            if count_gameover == 60:
                running = False
                gameover(win)
        pygame.display.flip()
        clock.tick(60)


gameloop()
pygame.quit()
quit()