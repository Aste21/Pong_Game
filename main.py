import pygame
import sys
import random


def menu_key_input(key):
    """
    A function taking the users input in the menu.
    """
    if key == pygame.K_1:
        return 1
    elif key == pygame.K_2:
        return 2
    elif key == pygame.K_3:
        return 3
    elif key == pygame.K_4:
        return 4
    elif key == pygame.K_5:
        return 5
    elif key == pygame.K_6:
        return 6
    elif key == pygame.K_ESCAPE:
        return "esc"


def menu_selection(gm_chosen, gm, menu_stay):
    """
    A function setting the game mode based on the users input.
    """
    if gm_chosen == 1:
        gm = 1
        menu_stay = False
    elif gm_chosen == 2:
        gm = 2
        menu_stay = False
    if gm_chosen == 3:
        gm = 3
        menu_stay = False
    if gm_chosen == 4:
        gm = 4
        menu_stay = False
    if gm_chosen == 5:
        gm = 5
        menu_stay = False
    if gm_chosen == 6:
        gm = 6
        menu_stay = False
    if gm_chosen == "esc":
        sys.exit()
    return gm, menu_stay


def menu_txt(screen):
    """
    A function displaying all the menu text.
    """
    screen.fill(black)
    screen.blit(title, msg_box_title)
    screen.blit(instruction, msg_box_instruction)
    screen.blit(game_mode_1_text, msg_box_game_mode_1)
    screen.blit(game_mode_2_text, msg_box_game_mode_2)
    screen.blit(game_mode_3_text, msg_box_game_mode_3)
    screen.blit(game_mode_4_text, msg_box_game_mode_4)
    screen.blit(game_mode_5_text, msg_box_game_mode_5)
    screen.blit(game_mode_6_text, msg_box_game_mode_6)
    screen.blit(signature, msg_box_signature)
    screen.blit(exit_info, msg_box_exit_info)


def move(key, object_moved, speed, mode_3d):
    """
    Function used to move the player on the left
    using the arrow keys in game modes 1 - 5.
    In game mode number 5 the player can move 2d,
    the variable mode_2d is used to check
    if the player can move sideways.
    """
    if mode_3d:
        if key == pygame.K_UP:
            return object_moved.move(0, -speed)
        elif key == pygame.K_DOWN:
            return object_moved.move(0, speed)
        elif key == pygame.K_LEFT:
            return object_moved.move(-speed, 0)
        elif key == pygame.K_RIGHT:
            return object_moved.move(speed, 0)
    else:
        if key == pygame.K_UP:
            return object_moved.move(0, -speed)
        elif key == pygame.K_DOWN:
            return object_moved.move(0, speed)
    return object_moved


def move_player_2(key, object_moved, speed, mode_2d):
    """
    Function used to move the player on the right
    using the keys wasd in game modes 4 and 5.
    In game mode number 5 the player can move 2d,
    the variable mode_2d is used to check
    if the player can move sideways.
    """
    if not mode_2d:
        if key == pygame.K_w:
            return object_moved.move(0, -speed)
        elif key == pygame.K_s:
            return object_moved.move(0, speed)
    if mode_2d:
        if key == pygame.K_w:
            return object_moved.move(0, -speed)
        elif key == pygame.K_s:
            return object_moved.move(0, speed)
        elif key == pygame.K_a:
            return object_moved.move(-speed, 0)
        elif key == pygame.K_d:
            return object_moved.move(speed, 0)
    return object_moved


def key_selection(key_list):
    """
    Function reading multiple keys inputted
    at once. It is used in game mode
    4 and 5 (multiplayer).
    """
    key_1 = pygame.K_SPACE
    key_2 = pygame.K_SPACE
    if key_list[pygame.K_UP]:
        key_1 = pygame.K_UP
    elif key_list[pygame.K_DOWN]:
        key_1 = pygame.K_DOWN
    elif key_list[pygame.K_LEFT]:
        key_1 = pygame.K_LEFT
    elif key_list[pygame.K_RIGHT]:
        key_1 = pygame.K_RIGHT
    if key_list[pygame.K_w]:
        key_2 = pygame.K_w
    elif key_list[pygame.K_s]:
        key_2 = pygame.K_s
    elif key_list[pygame.K_a]:
        key_2 = pygame.K_a
    elif key_list[pygame.K_d]:
        key_2 = pygame.K_d
    return key_1, key_2


def collision_detection_border(object_1, key, speed):
    """
    Function detecting collision between
    the player and the border and the
    midway point on the screen.
    by checking if the player
    had been out of
    border the next frame.
    It returns True if it
    had left the border.
    """
    if move(key, object_1, speed, True).bottom > win.bottom:
        return True
    if move(key, object_1, speed, True).top < win.top:
        return True
    if object_1.centerx > win.centerx:
        if move(key, object_1, speed, True).left < win.centerx:
            return True
    if move(key, object_1, speed, True).right > win.right:
        return True
    return False


def collision_detection_border_playground(object_1, key, speed):
    """
    Function detecting collision between the player and the border
    in testing game mode number 6 by checking if the player
    had been out of border the next frame.
    It returns True if it had left the border.
    """
    if move(key, object_1, speed, True).bottom > win.bottom:
        return True
    if move(key, object_1, speed, True).top < win.top:
        return True
    if move(key, object_1, speed, True).left < win.left:
        return True
    if move(key, object_1, speed, True).right > win.right:
        return True
    return False


def collision_detection_border_2(object_1, key, speed):
    """
    Function used in game modes 4 and 5 to detect
    collision between the player and the border
    when the player is using wasd keys.
    """
    if move_player_2(key, object_1, speed, True).bottom > win.bottom:
        return True
    if move_player_2(key, object_1, speed, True).top < win.top:
        return True
    if move_player_2(key, object_1, speed, True).left < win.left:
        return True
    if move_player_2(key, object_1, speed, True).right > win.centerx:
        return True
    return False


def collision_detection_player(player, ball, key_player, speed_player,
                               speed_ball):
    """
    Function detecting collision between the ball and the player by
    checking if they would collide on the next frame.
    It returns True when the collision would appear
    and False if it wouldn't. It is used to stop the
    player from running into the ball.
    """
    if pygame.Rect.colliderect(move(key_player, player, speed_player, True),
                               ball.move(speed_ball)):
        return True
    if pygame.Rect.colliderect(move_player_2(key_player, player, speed_player,
                                             True), ball.move(speed_ball)):
        return True
    return False


def collision_detection_ball_playground(ball, speed):
    """
    Function detecting collision
    between the ball and the border.
    If it hits the left or right side
    of the border, the horizontal speed is inverted.
    If it hits the top or bottom side
    of the border, the vertical speed is inverted.
    If it hits any of the corners both
    horizontal and vertical speed is inverted.
    It is used in game mode 6 just for testing.
    """
    if ball.bottomright == win.bottomright or ball.topright == win.topright \
            or ball.bottomleft == win.bottomleft or ball.topleft == win.topleft:
        speed[0] = -speed[0]
        speed[1] = -speed[1]
        return speed
    if ball.left < win.left or ball.right > win.right:
        speed[0] = -speed[0]
        return speed
    if ball.top < win.top or ball.bottom > win.bottom:
        speed[1] = -speed[1]
        return speed
    return speed


def collision_detection_ball(ball, speed):
    """
    Function detecting collision between
    the ball and the top and bottom border.
    If a collision is detected the vertical speed is inverted.
    It is used in game modes 1-5.
    """
    if ball.top < win.top or ball.bottom > win.bottom:
        speed[1] = -speed[1]
        return speed
    return speed


def collision_detection_enemy_border(enemy, enemy_speed):
    """
    Function detecting collision between the enemy and the border.
    It stops the enemy from going through the border.
    """
    if enemy.move(enemy_speed).top == win.top or enemy.move(enemy_speed).bottom == win.bottom:
        enemy.move([0, 1])
        return True
    return False


def collision_detection_ball_player(ball, player, speed):
    """
    Function detecting collision between ball and the player,
    if a collision is detected it changes the balls vector
    from left to right, and from right to left.
    The horizontal speed is bigger by a random amount between 0 and 0.5.
    The vertical speed is bigger or lower by -0.2 and 0.5.
    If the vertical speed is lower than 1, then it will increase until
    its bigger than 1.
    """
    if pygame.Rect.colliderect(ball, player):
        if abs((ball.h + player.h) / 2 - abs(ball.centery - player.centery)) < \
                abs((ball.w + player.w) / 2 - abs(ball.centerx - player.centerx)):
            speed[1] = -speed[1]
            return speed
        else:
            if speed[1] > 1 or speed[1] < -1:
                if speed[1] > 0:
                    speed[1] = speed[1] + random.uniform(-0.2, 0.5)
                else:
                    speed[1] = speed[1] - random.uniform(-0.2, 0.5)
            else:
                if speed[1] > 0:
                    speed[1] = speed[1] + random.uniform(0, 0.5)
                else:
                    speed[1] = speed[1] - random.uniform(0, 0.5)
            if speed[0] > 0:
                speed[0] = -speed[0] - random.uniform(0, 0.5)
            else:
                speed[0] = -speed[0] + random.uniform(0, 0.5)
            return speed
    return speed


def ball_return(ball, gm, player_a, player_b):
    """
    A function used when the ball is out of the screen.
    It sets the coordinates of the players to their original coordinates,
    sets the ball coordinates to the center of the screen,
    and sets the balls speed to its original depending on the game mode.
    """
    player_a.center = [17, win.centery]
    player_b.center = [1063, win.centery]
    ball.center = [540, 360]
    if gm == 1:
        ball_speed = [1.5, -1.5]
        return ball_speed
    elif gm == 2:
        ball_speed = [2.5, -2]
        return ball_speed
    elif gm == 3:
        ball_speed = [3.5, 3]
        return ball_speed
    elif gm == 4 or gm == 5:
        ball_speed = [2, 1.5]
        return ball_speed


def ai_vector(enemy, ball, enemy_speed):
    """
    Function setting the enemy(computers) vector. It is based on the ball position.
    If the ball is higher than the computer, the computer will go up,
    and if the ball is lower than the computer then the computer will go down.
    """
    enemy_speed_y = abs(enemy_speed[1])
    if enemy.centery < ball.centery:
        enemy_speed[1] = enemy_speed_y
        return enemy_speed
    if enemy.centery > ball.centery:
        enemy_speed[1] = -enemy_speed_y
        return enemy_speed
    return enemy_speed


def gm_1_2_3(ball, ball_speed, enemy, enemy_speed, player, screen, gm, score_game):
    """
    Main function detecting collision,
    setting enemy vector, drawing all the objects, setting the score
    and deciding the ball movement in game mode 1 - 3.
    When the score is equal to 10 for
    either of the players the game ends and player with
    10 points is the winner.
    """
    global score_left, score_right, line
    if score_game[0] < 10 and score_game[1] < 10:
        score_left = font_score.render(str(score[0]), True, white)
        score_right = font_score.render(str(score[1]), True, white)
        if ball.right < 0:
            score[1] += 1
            ball_speed = ball_return(ball, gm, player, enemy)
        elif ball.left > 1080:
            score[0] += 1
            ball_speed = ball_return(ball, gm, player, enemy)
        ball = ball.move(ball_speed)
        collision_detection_ball(ball, ball_speed)
        collision_detection_ball_player(ball, player, ball_speed)
        collision_detection_ball_player(ball, enemy, ball_speed)
        if collision_detection_enemy_border(enemy, enemy_speed):
            ai_vector(enemy, ball, enemy_speed)
        else:
            enemy = enemy.move(enemy_speed)
            ai_vector(enemy, ball, enemy_speed)
        screen.fill(black)
        screen.blit(score_left, msg_box_score_left)
        screen.blit(score_right, msg_box_score_right)
        pygame.draw.rect(screen, gray, line)
        pygame.draw.rect(screen, white, player)
        pygame.draw.rect(screen, white, ball)
        pygame.draw.rect(screen, white, enemy)
        return ball, enemy, ball_speed, score_game
    if score_game[0] >= 10:
        screen.fill(black)
        screen.blit(you_win, msg_box_you_win)
        screen.blit(press_backspace, msg_box_press_backspace)
    elif score_game[1] >= 10:
        screen.fill(black)
        screen.blit(you_loose, msg_box_you_loose)
        screen.blit(press_backspace, msg_box_press_backspace)
    return ball, enemy, ball_speed, score_game


def player_movement_1_2_3(player_a, key, player_a_speed, ball, ball_speed):
    """
    Function used to detect collision and move the player in game mode number 1-3.
    """
    if not collision_detection_border(player_a, key, player_a_speed) \
            and not collision_detection_player(player_a, ball, key, player_a_speed, ball_speed):
        player_a = move(key, player_a, player_a_speed, False)
    return player_a


def gm_4_5(ball, ball_speed, player_a, player_b, screen, gm, score_game):
    """
    Main function detecting collision, setting enemy vector, drawing all the objects, setting the score
    and deciding the ball movement in game mode 4 and 5.
    When the score is equal to 10 for either of the players the game ends and player with
    10 points is the winner.
    """
    global score_left, score_right, line
    if score_game[0] < 10 and score_game[1] < 10:
        score_left = font_score.render(str(score[0]), True, white)
        score_right = font_score.render(str(score[1]), True, white)
        if ball.right < 0:
            score[1] += 1
            ball_speed = ball_return(ball, gm, player_a, player_b)
        elif ball.left > 1080:
            score[0] += 1
            ball_speed = ball_return(ball, gm, player_a, player_b)
        ball = ball.move(ball_speed)
        collision_detection_ball(ball, ball_speed)
        collision_detection_ball_player(ball, player_a, ball_speed)
        collision_detection_ball_player(ball, player_b, ball_speed)
        screen.fill(black)
        screen.blit(score_left, msg_box_score_left)
        screen.blit(score_right, msg_box_score_right)
        pygame.draw.rect(screen, gray, line)
        pygame.draw.rect(screen, white, player_a)
        pygame.draw.rect(screen, white, player_b)
        pygame.draw.rect(screen, white, ball)
    if score_game[0] >= 10:
        screen.fill(black)
        screen.blit(player_1_win, msg_box_player_1_win)
        screen.blit(press_backspace, msg_box_press_backspace)
    elif score_game[1] >= 10:
        screen.fill(black)
        screen.blit(player_2_win, msg_box_player_2_win)
        screen.blit(press_backspace, msg_box_press_backspace)
    return ball, ball_speed, score_game


def player_movement_4_5(player_a, player_b, key, player_a_speed, player_b_speed, ball, ball_speed):
    """
    Function used to detect collision and move the player in game mode number 4 and 5.
    Variable is_2d determines if the player can move left and right. (it is used in game mode 5)
    """
    if game_mode == 4:
        is_2d = False
    else:
        is_2d = True
    if not collision_detection_border_2(player_a, key, player_a_speed) \
            and not collision_detection_player(player_a, ball, key, player_a_speed, ball_speed):
        player_a = move_player_2(key, player_a, player_a_speed, is_2d)
    if not collision_detection_border(player_b, key, player_b_speed) \
            and not collision_detection_player(player_b, ball, key, player_b_speed, ball_speed):
        player_b = move(key, player_b, player_b_speed, is_2d)
    return player_a, player_b


def player_movement_6(player_a, key, player_a_speed, ball, ball_speed):
    """
    Function used to detect collision and move the player in game mode number 6.
    """
    if not collision_detection_border_playground(player_a, key, player_a_speed) \
            and not collision_detection_player(player_a, ball, key, player_a_speed, ball_speed):
        player_a = move(key, player_a, player_a_speed, True)
    return player_a


def gm_6(ball, ball_speed, enemy, enemy_speed, player, screen):
    """
    Main function detecting collision, setting enemy vector, drawing all the objects,
    and deciding the ball movement in game mode 6.
    """
    global score_left, score_right, line
    if 1 > 0:
        ball = ball.move(ball_speed)
        collision_detection_ball_playground(ball, ball_speed)
        collision_detection_ball_player(ball, player, ball_speed)
        collision_detection_ball_player(ball, enemy, ball_speed)
        if collision_detection_enemy_border(enemy, enemy_speed):
            ai_vector(enemy, ball, enemy_speed)
        else:
            enemy = enemy.move(enemy_speed)
            ai_vector(enemy, ball, enemy_speed)
        screen.fill(black)
        pygame.draw.rect(screen, gray, line)
        pygame.draw.rect(screen, white, player)
        pygame.draw.rect(screen, white, ball)
        pygame.draw.rect(screen, white, enemy)
        return ball, enemy, ball_speed,


def starting_values_1_2_3(gm, ball_speed, enemy_speed, score_start, player_a, player_b):
    # Function setting the starting values in game modes 1-3
    player_a.center = [17, win.centery]
    player_b.center = [1063, win.centery]
    if enemy_speed == [0, 0] and gm == 1:
        score_start = [0, 0]
        ball_speed = [1.5, 1.5]
        enemy_speed = [0, 1]
    elif enemy_speed == [0, 0] and gm == 2:
        score_start = [0, 0]
        ball_speed = [2.5, 2]
        enemy_speed = [0, 2]
    elif enemy_speed == [0, 0] and gm == 3:
        score_start = [0, 0]
        ball_speed = [3.5, 3]
        enemy_speed = [0, 4]
    return ball_speed, enemy_speed, score_start


def starting_values_4_5(gm, ball_speed, score_start, player_a, player_b):
    # Function setting the staring values in game modes 4 and 5.
    player_a.center = [17, win.centery]
    player_b.center = [1063, win.centery]
    if gm == 1:
        score_start = [0, 0]
        ball_speed = [1.5, 1.5]
    elif gm == 2:
        score_start = [0, 0]
        ball_speed = [2.5, 2]
    elif gm == 3:
        score_start = [0, 0]
        ball_speed = [3.5, 3]
    elif gm == 4 or gm == 5:
        score_start = [0, 0]
        ball_speed = [2, 1.5]
    return ball_speed, score_start


if __name__ == "__main__":
    pygame.init()

    # Declaration of all the colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (100, 100, 100)
    green = (0, 255, 0)
    red = (255, 0, 0)

    # Declaration of a table having a score, where score[0] is score of left player.
    score = [0, 0]

    # Declaration of all the texts.
    font_score = pygame.font.SysFont("arial black", 40)
    score_left = font_score.render(str(score[0]), True, white)
    score_right = font_score.render(str(score[0]), True, white)
    msg_box_score_left = score_left.get_rect()
    msg_box_score_right = score_right.get_rect()
    msg_box_score_left.center = [270, 100]
    msg_box_score_right.center = [810, 100]

    font_title = pygame.font.SysFont("arial black", 100)
    title = font_title.render("PONG !", True, white)
    msg_box_title = title.get_rect()
    msg_box_title.center = [540, 100]

    font_instruction = pygame.font.SysFont("arial black", 15)
    instruction = font_instruction.render(
        "Pick game mode by pressing number on your keyboard.", True, white)
    msg_box_instruction = instruction.get_rect()
    msg_box_instruction.center = [540, 200]

    font_game_mode = pygame.font.SysFont("arial black", 40)
    game_mode_1_text = font_game_mode.render(
        "1. Player vs Computer (EASY)", True, white)
    msg_box_game_mode_1 = game_mode_1_text.get_rect()
    msg_box_game_mode_1.center = [540, 250]

    game_mode_2_text = font_game_mode.render(
        "2. Player vs Computer (MEDIUM)", True, white)
    msg_box_game_mode_2 = game_mode_2_text.get_rect()
    msg_box_game_mode_2.center = [540, 320]

    game_mode_3_text = font_game_mode.render(
        "3. Player vs Computer (HARD)", True, white)
    msg_box_game_mode_3 = game_mode_3_text.get_rect()
    msg_box_game_mode_3.center = [540, 390]

    game_mode_4_text = font_game_mode.render(
        "4. Player vs Player (Classic)", True, white)
    msg_box_game_mode_4 = game_mode_4_text.get_rect()
    msg_box_game_mode_4.center = [540, 460]

    game_mode_5_text = font_game_mode.render(
        "5. Player vs Player (2D)", True, white)
    msg_box_game_mode_5 = game_mode_5_text.get_rect()
    msg_box_game_mode_5.center = [540, 530]

    game_mode_6_text = font_game_mode.render("6. TEST", True, white)
    msg_box_game_mode_6 = game_mode_6_text.get_rect()
    msg_box_game_mode_6.center = [540, 600]

    font_signature = pygame.font.SysFont("arial black", 15)
    signature = font_signature.render(
        "Made by: Wiktor Kopczynski 246939", True, white)
    msg_box_signature = signature.get_rect()
    msg_box_signature.center = [920, 700]

    exit_info = font_signature.render("Press ESCAPE to exit", True, white)
    msg_box_exit_info = exit_info.get_rect()
    msg_box_exit_info.center = [100, 20]

    you_win = font_title.render("YOU WIN!", True, green)
    you_loose = font_title.render("YOU LOOSE!", True, red)
    msg_box_you_win = you_win.get_rect()
    msg_box_you_loose = you_loose.get_rect()
    msg_box_you_win.center = [540, 360]
    msg_box_you_loose.center = [540, 360]

    player_1_win = font_title.render("PLAYER 1 WON!", True, green)
    msg_box_player_1_win = player_1_win.get_rect()
    msg_box_player_1_win.center = [540, 360]

    player_2_win = font_title.render("PLAYER 2 WON!", True, green)
    msg_box_player_2_win = player_2_win.get_rect()
    msg_box_player_2_win.center = [540, 360]

    press_backspace = font_score.render(
        "press backspace to go back to menu.", True, white)
    msg_box_press_backspace = press_backspace.get_rect()
    msg_box_press_backspace.center = [540, 440]

    # Declaration of the mid-screen line.
    line = pygame.Rect(535, 0, 10, 2000)

    # Declaration of screen
    scr = pygame.display.set_mode((1080, 720))
    win = scr.get_rect()
    line.center = win.center

    # Declaration of player 1 and 2
    player_1 = pygame.Rect(10, (scr.get_size()[1]) / 2 - 100, 15, 100)
    player_2 = pygame.Rect(1055, (scr.get_size()[1]) / 2 - 100, 15, 100)

    # Declaration of the enemy used in game modes 1-3
    enemy_1 = pygame.Rect((scr.get_size()[0]) - 40, (scr.get_size()[1]) / 2 - 10, 15, 100)
    enemy_vect = [0, 0]

    # Declaration of the ball.
    ball_1 = pygame.Rect(0, 0, 20, 20)
    ball_1.center = win.center
    ball_vect = [-1.5, -1.5]

    # Declaration of players speed.
    player_1_speed = 7
    player_2_speed = 7

    pygame.key.set_repeat(10, 10)
    fps = pygame.time.Clock()

    # variable checking if it's the first frame in chosen game mode.
    is_first = True

    # variable checking if we are in menu selection
    menu = True
    """
    Variable checking our game mode, if game_mode == 0 then we are in menu.
    At the start its set to the value 0.
    game mode 1 - PvC easy
    game mode 2 - PvC medium
    game mode 3 - PvC hard
    game mode 4 - PvP 1d
    game mode 5 - PvP 2d
    """
    game_mode = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if menu:
                    game_mode_chosen = menu_key_input(event.key)
                    game_mode, menu = menu_selection(game_mode_chosen, game_mode, menu)
                if game_mode == 1 or game_mode == 2 or game_mode == 3:
                    if event.key == pygame.K_BACKSPACE:
                        enemy_vect = [0, 0]
                        game_mode = 0
                        menu = True
                    player_1 = player_movement_1_2_3(player_1, event.key, player_1_speed, ball_1, ball_vect)
                if game_mode == 4 or game_mode == 5:
                    if event.key == pygame.K_BACKSPACE:
                        enemy_vect = [0, 0]
                        game_mode = 0
                        menu = True
                    keys = pygame.key.get_pressed()
                    key_one, key_two = key_selection(keys)
                    player_1, player_2 = player_movement_4_5(player_1, player_2, key_one, player_1_speed,
                                                             player_2_speed, ball_1, ball_vect)
                    player_1, player_2 = player_movement_4_5(player_1, player_2, key_two, player_1_speed,
                                                             player_2_speed, ball_1, ball_vect)
                if game_mode == 6:
                    if event.key == pygame.K_BACKSPACE:
                        enemy_vect = [0, 0]
                        game_mode = 0
                        menu = True
                    if not collision_detection_border_playground(player_1, event.key, player_1_speed):
                        player_1 = player_movement_6(player_1, event.key, player_1_speed, ball_1, ball_vect)

        if menu:
            menu_txt(scr)
            is_first = True

        if game_mode == 1 or game_mode == 2 or game_mode == 3:
            if is_first:
                ball_1.center = win.center
                ball_vect, enemy_vect, score = \
                    starting_values_1_2_3(game_mode, ball_vect, enemy_vect, score, player_1, enemy_1)
                is_first = False
            ball_1, enemy_1, ball_vect, score = \
                gm_1_2_3(ball_1, ball_vect, enemy_1, enemy_vect, player_1, scr, game_mode, score)

        if game_mode == 4 or game_mode == 5:
            if is_first:
                ball_1.center = win.center
                ball_vect, score = starting_values_4_5(game_mode, ball_vect, score, player_1, player_2)
                is_first = False
            ball_1, ball_vect, score = \
                gm_4_5(ball_1, ball_vect, player_1, player_2, scr, game_mode, score)

        if game_mode == 6:
            if is_first:
                ball_vect = [2, 2]
                is_first = False
            ball_1, enemy_1, ball_vect = gm_6(ball_1, ball_vect, enemy_1, enemy_vect, player_1, scr)

        pygame.display.flip()

        fps.tick(240)
