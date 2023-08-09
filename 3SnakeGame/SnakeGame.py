import pygame #pip install pygame 
import random 
from enum import Enum #used to declare varibale etc properly 
from collections import namedtuple 

#initalization the pygame
pygame.init()#used initialize the pygame to ready for environment 
#declare font
font = pygame.font.SysFont("arial",25)

#direction
class Direction(Enum): #Enum is the base class for all enum enumerations.
    RIGHT = 1 #we can access as values and name 
    LEFT = 2 #such as this 
    UP = 3 #Direction.UP.name
    DOWN = 4 #for values Direction.DOWN.values
    
Point = namedtuple("Point","x, y")#can be accessed by their values such as Point.x


#colors
WHITE = (255,255,255)
RED = (200,0,0)
BLUE1 = (0,0,255)
BLUE2 = (0,100,255)
BLACK = (0,0,0)

#variables
#you can change the block size of the snake and the window block size 
BLOCK_SIZE = 20
#you can change the speed of snake as you want
SPEED = 20
#in this code self is an object 
class SnakeGame:
    def __init__(self,w = 640, h = 480):
        self.w = w
        self.h = h
        #set display as per h and w
        self.display = pygame.display.set_mode((self.w,self.h))
        #set_caption fucntion is used to add the name which we want to add to the game screen
        pygame.display.set_caption("Snake game")
        #clock function is used to create a clcok object which is used to tarck the time
        self.clock = pygame.time.Clock() 
        #it will determine the default direction such as starting position
        self.direction = Direction.RIGHT
        #it will determine the head of the snake it will be start at the center 
        self.head = Point(self.w/2, self.h/2)
        #self.snake determine the snake such as it will breaks into 3 snake body have head after that second portion means the x value of point - block size and y as the y of head
        #and the third one is another body after the gap of 1 block 
        self.snake = [self.head,
                     Point(self.head.x-BLOCK_SIZE,self.head.y),
                     Point(self.head.x-(2*BLOCK_SIZE),self.head.y)]
    #this score variable is used to store the score
        self.score = 0
        self.food = None
        self._place_food()
        #this function is used to genrate food at random place on screen using randint function
    def _place_food(self):
            x = random.randrange(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            y = random.randrange(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            self.food = Point(x,y)
            #this condition check if the food generates near or on the snake than it will generate new food at antoher random place 
            if self.food in self.snake:
                self._place_food()
        #this function is used to take input from user to handle(control) the snake 
    def play_step(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    #this will take user input as WASD W for up A for left S for down D for right
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.direction = Direction.UP
                    elif event.key == pygame.K_a:
                        self.direction = Direction.LEFT
                    elif event.key == pygame.K_s:
                        self.direction = Direction.DOWN
                    elif event.key == pygame.K_d:
                        self.direction =  Direction.RIGHT
            #this move function is used to move the snake
            self._move(self.direction)
            self.snake.insert(0,self.head)
            #this will indicate if game is over or not
            gameover = False
            #for boundary
            if self._is_collision():
                gameover = True
                return gameover, self.score
            #for hitting it self
            if self.head in self.snake[1:]:
                return True
            #for chceking the food is taken by snake if yes than increment score and place food and if food is not taken than pop one block from snake
            if self.head == self.food:
                self.score += 1
                self._place_food()
            else:
                self.snake.pop()
            
            self._update_ui()
            self.clock.tick(SPEED)

            return gameover, self.score
    #this function is used to check if collision is happen or not it will terminate the game if collison happen 
    #there are two possiblity for the collision 
    #1.if snake hits boundary
    #.if snake touch it self
    def _is_collision(self):
            #for hitting boundary
            if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
                return True
            #for hitting it self
            if self.head in self.snake[1:]:
                return True
            
            return False
    #this functions is used to update the ui it plays main role for moving the snake or generating the food 
    def _update_ui(self):
            self.display.fill(BLACK)
        
            for pt in self.snake:
                #FOR HIS HEAD
                pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
                #for his otherpart of body when we get point it will add to snake list and than it will print/display using this line below
                pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            #this is used to display the food from where we wrote that where randomly food position x y will generate and than it will come to this and display by this
            pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
            #this will used  to return score as text on display
            text = font.render("Score: "+ str(self.score), True, WHITE)
            self.display.blit(text,[0,0])
            pygame.display.flip()
    #this function is used to move the snake as per user input from direction function
    def _move(self, direction):
            x = self.head.x
            y = self.head.y
            if direction == Direction.UP:
                y -= BLOCK_SIZE
            elif direction == Direction.LEFT:
                x -= BLOCK_SIZE
            elif direction == Direction.DOWN:
                y += BLOCK_SIZE
            elif direction == Direction.RIGHT:
                x += BLOCK_SIZE
            
            self.head = Point(x, y)
if __name__ == '__main__':
    game = SnakeGame()
    #game loop
    while True:
        gameover,score = game.play_step()

        if gameover == True:
            break
            #printing final score
    print("final score ",score)
#this pygame.quit() function is used to quit the game 
    pygame.quit()


