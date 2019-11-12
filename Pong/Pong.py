# paddle-ball.py
import sys, platform
import pygame
import random
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE, K_LEFT, K_RIGHT, K_r

class Ball:
    """ Describes a ball and it's attributes."""
    def __init__ (self):
        """Initialize ball and it's attributes."""
        self.ball_x = 200
        self.ball_y = 30
        self.ball_r = 8
        self.dx = 1
        self.dy = 1
        self.ball_speed = 1
    def ball_move(self):
        # move a ball
        self.ball_x += (self.dx * self.ball_speed); self.ball_y += (self.dy *self.ball_speed)
    def bounce_x(self):
        """bounce's ball in the horizontal"""
        self.dx *= -1
    def bounce_y(self):
        """bounce's ball in the horizontal"""
        self.dy *= -1



class Racket:
    """ Describes a racket."""
    def __init__(self):
        self.rckt_x = 200
        self.rckt_y = 280
        self.rckt_w = 40
        self.rckt_move = 15

    def move_right(self):
       self.rckt_x += self.rckt_move
    def move_left(self):
       self.rckt_x -= self.rckt_move




class Game:
    """Game status and variables"""
    def __init__(self,game_balls):
        self.state = 0
        self.point = 0
        self.balls = game_balls
        self.racket = Racket()
        self.bounce = 0
    def should_bounce(self):
        for ball in self.balls:
            if self.ball_x
    def turn(self, event):





def display_massage(sf, msg, h) :
    sysfont = pygame.font.sysfont(none, 36)
    message = sysfont.render(msg, true, (100,255,200))
    message_rect = message.get_rect()
    message_rect.center = (200, h)
    sf.blit(message, message_rect)
    pygame.display.update()

def main():
    random.seed()
    pygame.init()                       # pygame initialize
    pygame.display.set_mode((400, 300))  # set screen
    pygame.display.set_caption("paddle-ball")
    surface = pygame.display.get_surface()
    surface.fill(0x006633)

    pygame.key.set_repeat(5,5)

    first_ball= 

    #variables
#    ball_x = 200; ball_y = 30   # Ball's coordinates
#    ball_r = 8                  # ball's radius
#    dx = 0; dy = 0              # ball's delta

#    rckt_x = 180;rckt_y = 280   # racket's coordinates
#    rckt_w = 40                 # racket's width

#    point = 0
#    state = 0                  # 0:Initial, 1:Game started, 2:Gave over

#    while (True) :

#        if state == 0:
#            surface.fill(0x006633)
#            display_massage(surface, "Press Space Key to Start", 160)
#        elif state == 1:
#            surface.fill(0x006633)
#            # move a ball
#            ball_x += dx; ball_y += dy
#            # draw a ball
#            pygame.draw.circle(surface,(0,255,0),(ball_x,ball_y),ball_r)

#            # draw a racket
#            pygame.draw.rect(surface,(0,0,255),(rckt_x,rckt_y,rckt_w,5),0)
#            point += 1






#        # Check the collision. If there is a collision, change the direction of the ball
#            #if right wall
#            if ball_x +8 >= 400:
#                dx *= -1
#            #if left wall
#            elif ball_x -8 <= 0:
#                dx *= -1
#            #if top
#            elif ball_y -8 <= 0:
#                dy *= -1
#            #Bottom Bounce-Testing only
#            elif ball_y +8 >= ball_y +8 >= 300:
#                dx = 0
#                dy = 0
#                state = 2
#        # if Hit the racket
#            elif ball_y +8 >= rckt_y and (rckt_x < ball_x < (rckt_x + rckt_w)):
#                dy *= -1
#            # if the ball touched the bottom of the screen,display messages and change the state to 2
#        elif state ==2:
#            msg1 = f"Game Over! Your score is {point}."
#            display_massage(surface, msg1, 50)
#            display_massage(surface, "Press 'r' to play again.", 80)
#            display_massage(surface, "Press 'Esc' to quit", 110)

#        # Handle events
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit()
#                sys.exit()
#            if event.type == KEYDOWN:
#                if event.key == K_ESCAPE:
#                    pygame.quit()
#                    sys.exit()

#                # Start Game
#                if event.key == K_SPACE and state == 0:
#                    state = 1
#                    dx = random.randint(1, 9) - 4
#                    if dx == 0:
#                        dx = 3#"""Add some code here"""
#                    dy = random.randint(1, 9) - 4
#                    if dy == 0:
#                        dy = 3#"""Add some code here"""

#                # Restart Game
#                if event.key == K_r:
#                    state = 0
#                    #Ball's original coordinates
#                    #reset values
#                    ball_x = 200; ball_y = 30
#                    point = 0

#                #Move the racket to Left
#                if event.key == K_LEFT and rckt_x > 0:
#                    rckt_x -= 15


#                    #Make sure the racket does not disappear

#                #Move the racket to Right
#                if event.key == K_RIGHT and (rckt_x + rckt_w)<400:
#                    rckt_x +=15


#                    #Make sure the racket does not disappear


#        pygame.display.update()
#        pygame.time.delay(50)

if __name__ == "__main__":
    main()



