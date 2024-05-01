import pygame
import random
import time
import threading
from PIL import ImageFilter, Image

pygame.init()
width = 500
height = 400
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stone, Paper, Scissor - Made by Om")

# creating variables for images
paper = pygame.image.load("paper.png")
paper_rect = paper.get_rect()
paper_rect.topleft = (0, (height / 2) - (paper.get_height() / 2))
paper_no = 1

paper_comp = pygame.image.load("paper2.png")
paper_comp_rect = paper_comp.get_rect()
paper_comp_rect.topright = (width, (height / 2) - (paper_comp.get_height() / 2))

rock = pygame.image.load("rock.png")
rock_rect = rock.get_rect()
rock_rect.topleft = (0, (height / 2) - (rock.get_height() / 2))
rock_no = 0

rock_comp = pygame.image.load("rock2.png")
rock_comp_rect = rock_comp.get_rect()
rock_comp_rect.topright = (width, (height / 2) - (rock_comp.get_height() / 2))

scissor = pygame.image.load("scissor.png")
scissor_rect = scissor.get_rect()
scissor_rect.topleft = (0, (height / 2) - (scissor.get_height() / 2))
scissor_no = 2

scissor_comp = pygame.image.load("scissor2.png")
scissor_comp_rect = scissor_comp.get_rect()
scissor_comp_rect.topright = (width, (height / 2) - (scissor_comp.get_height() / 2))

# creating variables for buttons

rock_button = pygame.Surface((120, 50))
rock_button.fill((255, 0, 0))
rock_button_x = 20

paper_button = pygame.Surface((120, 50))
paper_button.fill((255, 0, 0))
paper_button_x = rock_button_x + rock_button.get_width() + 50

scissor_button = pygame.Surface((120, 50))
scissor_button.fill((255, 0, 0))
scissor_button_x = paper_button_x + paper_button.get_width() + 50

confirm = pygame.Surface((120, 50))
confirm.fill(pygame.Color("blue1"))
confirm_x = 50
confirm_y = 150
stop_buttons = False

fill_comp = pygame.Surface((250, 250))
fill_comp.fill(pygame.Color("gray"))

# variable to store what to show images
show_player = [paper, paper_rect, paper_no]
show_comp = [paper_comp, paper_comp_rect, paper_no]

comp_options = [[paper_comp, paper_comp_rect, paper_no], [rock_comp, rock_comp_rect, rock_no],
                    [scissor_comp, scissor_comp_rect, scissor_no]]

done = False

# matrix for win
# first comp then user
# ex - rock - rock(tie), paper(win), scissor(lose); paper - lose, tie, win; scissor - win, lose, tie
win_matrix = [["Tie", "You Win", "You Lose"], ["You Lose", "Tie", "You Win"], ["You Win", "You Lose", "Tie"]]
win_text = "Tie"
win_colors = [["turquoise4", "lime", "gray20"], ["gray20", "turquoise4", "lime"], ["lime", "gray20", "turquoise4"]]
win_color = "lime"
win_text_x = 0
win_over = False

font = pygame.font.SysFont("Arial", 30)
font2 = pygame.font.SysFont("Arial", 50)
font3 = pygame.font.SysFont("Arial", 70)

def draw_text(text, font, text_color, y, button_x):
    img = font.render(text, True, text_color)
    screen.blit(img, (button_x, y))
    global win_text_x
    if text in win_matrix[0]:
        win_text_x = img.get_width()

check_timer = False

def timer():
    time.sleep(0.5)
    global check_timer
    check_timer = True

back_timer = threading.Thread(target=timer)

check_timer_win = False
timer_run = False
countdown = 3

def timer_win():
    global timer_run
    timer_run = True
    timer1 = 0
    global countdown
    global check_timer_win
    while timer_run:
        timer1 += 1
        if timer1 % 60 == 0:
            timer1 = 0
            if countdown == 1:
                timer_run = False
                check_timer_win = True
                countdown = 4
            countdown -= 1
        clock.tick(60)

back_timer_win = threading.Thread(target=timer_win)


def gameover(gameloop):
    time.sleep(0.5)

    global win_over
    play_again = pygame.Surface((280, 75))
    play_again.fill(pygame.Color("darkblue"))
    back_screen = pygame.image.load("back_screen.png")
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    text_image = font3.render(win_text, True, pygame.Color(win_color))

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_pos[0] > (width/2)- (play_again.get_width()/2)) and (mouse_pos[0] < ((width/2)-(play_again.get_width()/2)) + play_again.get_width()) and (mouse_pos[1] > 220) and (mouse_pos[1] < 220 + (play_again.get_height())):
                    play_again.fill(pygame.Color("cyan2"))

            if event.type == pygame.MOUSEBUTTONUP:
                if play_again.get_at((0, 0)) == pygame.Color("cyan2"):
                    play_again.fill(pygame.Color("darkblue"))
                    win_over = False
                    gameloop()

        screen.fill((255, 255, 255))
        screen.blit(back_screen, (0, 0))
        for offset in offsets:
            text_rect = text_image.get_rect(center=(width // 2 + offset[0], (height // 2 - 50) + offset[1]))
            screen.blit(text_image, text_rect)

        screen.blit(play_again, ((width/2)- (play_again.get_width()/2), 220))
        draw_text("Play Again", font2, (255, 255, 255), 220 + 10, ((width/2)- (play_again.get_width()/2)) + 25 )

        pygame.display.flip()
        clock.tick(60)


def gameloop():
    global width
    global height
    global clock
    global screen
    global show_player
    global check_timer
    global back_timer
    global back_timer
    global back_timer_win
    global stop_buttons
    global done
    global show_comp
    global check_timer_win
    global win_over
    global win_text_x
    global win_text
    global win_color
    global fill_comp

    running = True

    while running:
        screen.fill(pygame.Color("gray"))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_pos[0] > rock_button_x) and (mouse_pos[1] > height - 70) and (mouse_pos[0] < rock_button_x + rock_button.get_width()) and (mouse_pos[1] < (height - 70) + rock_button.get_height()) and not stop_buttons:
                    rock_button.fill((0, 255, 0))
                    show_player = [rock, rock_rect, rock_no]
                    check_timer = False
                    back_timer = threading.Thread(target=timer)
                    back_timer.start()

                elif (mouse_pos[0] > paper_button_x) and (mouse_pos[1] > height - 70) and (mouse_pos[0] < paper_button_x + paper_button.get_width()) and (mouse_pos[1] < (height - 70) + paper_button.get_height()) and not stop_buttons:
                    paper_button.fill((0, 255, 0))
                    show_player = [paper, paper_rect, paper_no]
                    check_timer = False
                    back_timer = threading.Thread(target=timer)
                    back_timer.start()

                elif (mouse_pos[0] > scissor_button_x) and (mouse_pos[1] > height - 70) and (mouse_pos[0] < scissor_button_x + scissor_button.get_width()) and (mouse_pos[1] < (height - 70) + scissor_button.get_height()) and not stop_buttons:
                    scissor_button.fill((0, 255, 0))
                    show_player = [scissor, scissor_rect, scissor_no]
                    check_timer = False
                    back_timer = threading.Thread(target=timer)
                    back_timer.start()

                if (mouse_pos[0] > confirm_x) and (mouse_pos[1] > confirm_y) and (mouse_pos[0] < confirm_x + confirm.get_width()) and (mouse_pos[1] < confirm_y + confirm.get_height()):
                    confirm.fill(pygame.Color("cadetblue1"))
                    back_timer_win = threading.Thread(target=timer_win)
                    back_timer_win.start()
                    stop_buttons = True

            if event.type == pygame.MOUSEBUTTONUP:
                if rock_button.get_at((0,0)) == (0,255,0):
                    rock_button.fill((255,0,0))
                elif paper_button.get_at((0,0)) == (0,255,0):
                    paper_button.fill((255,0,0))
                elif scissor_button.get_at((0,0)) == (0,255,0):
                    scissor_button.fill((255,0,0))
                elif confirm.get_at((0,0)) == pygame.Color("cadetblue1"):
                    confirm.fill(pygame.Color("blue1"))
                    check_timer = False

        if not back_timer.is_alive() and check_timer:
            done = True
        else:
            done = False

        if timer_run:
            draw_text(str(countdown), font3, pygame.Color("firebrick1"), 80, 230)
            rock_button.fill(pygame.Color("orangered"))
            paper_button.fill(pygame.Color("orangered"))
            scissor_button.fill(pygame.Color("orangered"))

        # display the images
        screen.blit(show_player[0], show_player[1])
        screen.blit(show_comp[0], show_comp[1])

        # display the buttons
        screen.blit(rock_button,(rock_button_x,height-70))
        screen.blit(paper_button,(paper_button_x,height - 70))
        screen.blit(scissor_button,(scissor_button_x,height-70))

        if done:
            screen.blit(confirm,(confirm_x, confirm_y))
            draw_text("Confirm", font, (0,0,0),confirm_y + 10, confirm_x + 10)

        # display the text on button
        draw_text("Rock", font, (0,0,0), height - 60, rock_button_x + 27)
        draw_text("Paper", font, (0,0,0), height - 60, paper_button_x + 22)
        draw_text("Scissor", font, (0,0,0), height - 60, scissor_button_x + 13)

        draw_text("You", font2, (0, 0, 255), 20, 50)
        draw_text("Computer", font2, (0, 0, 255), 20, 270)

        if not back_timer_win.is_alive() and check_timer_win:
            screen.blit(fill_comp, paper_comp_rect.topleft)
            show_comp = random.choice(comp_options)
            screen.blit(show_comp[0], show_comp[1])
            check_timer_win = False
            stop_buttons = False
            win_over = True
            rock_button.fill((255, 0, 0))
            paper_button.fill((255, 0, 0))
            scissor_button.fill((255, 0, 0))
            win_text = win_matrix[show_comp[2]][show_player[2]]
            win_color = win_colors[show_comp[2]][show_player[2]]
            pygame.display.flip()

        if win_over:
            pygame.image.save(screen, "back_screen.png")
            original_screen = Image.open("back_screen.png")
            blurred_screen = original_screen.filter(ImageFilter.GaussianBlur(10))
            blurred_screen.save("back_screen.png")
            gameover(gameloop)

        pygame.display.flip()
        clock.tick(60)

gameloop()
pygame.quit()
quit()
