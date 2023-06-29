import pygame #pip install pygame
import math
import random 
from faker import Faker #pip install faker
#set up display

faker = Faker()
def hangman():
    pygame.init()
    name = input("hey what's up ready to play the game please enter your name to continue ")
    
    WIDTH, HEIGHT=800, 500 
    #set windows size as per your requirements you can change width and hwight 
    windows=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Hangman")
    #import the images of Hangman on display using pygame
    
     
    images=[]
    for i in range(7):
        img='1hangmangui\hangman'+str(i)+".png" #set this as per your file path
        image=pygame.image.load(img)       
        images.append(image)

    #game variables which we will use in our game 

    hangman_status = 0
    # words =["PYTHON","RUDRA","GAME","NOTHING","NOONE","TIM","WEEKEND"]
    word1= faker.word()
    word = word1.upper()
    guessed =[]
    
    
    #colors 
    BLUE=(25,179,226)
    BLACK=(0,0,0)

    #button varibales
    RADIUS = 20
    GAP = 15
    letters = []
    #using this ewuation ((WIDTH - (RADIUS * 2 + GAP)*13)/2) we can have the perfect button position where the button should be in this game the distance between the first edge and the last button edge to the line both sould be same for design to look the gui good 
    #if we use that equation then we can do something like teh distance between the first and last button to a both side edge should be same so we use that equation then we get the 42.2 if we place each button to the y = 42.2 distance than we can get the perfect distance between the two buttons   
    #                     ----------------------
    #                     this part will give the distance   
    startx=round((WIDTH - (RADIUS * 2 + GAP)*13)/2)
    starty=400
    A = 65
    for i in range(26):
        x=startx + GAP*2 + ((RADIUS * 2 + GAP) * (i%13))
        y=starty + ((i//13)*(GAP  + RADIUS * 2))
        letters.append([x,y,chr(A+i),True])
    #this function is for draw the circle for letters 
    hint_letter = ""
    def random_characters(string, num_characters):
        return random.sample(string, num_characters)
# Add a random character from word to hint_letter
    hint_letter += ''.join(random.sample(word, 3))
    hint_letter = hint_letter.upper()
    def draw():
        windows.fill(BLUE)
        #draw title
        #hint
        
        text = TITLE_FONT.render(f"hey {name} ",1,BLACK)
        hint= HINT_FONT.render(f"Hint are {hint_letter} ",1,BLACK)
        windows.blit(hint,(WIDTH/2-text.get_width()/2,60))
        windows.blit(text,(WIDTH/2-text.get_width()/2,10))
        #draw words 
        display_word = " "
        for letter in word :
            if letter in guessed :
                display_word +=letter + " "
            else:
                display_word +=("_ ")
        text = WORD_FONT.render(display_word,1,BLACK)
        windows.blit(text,(400,200))
        
      


        
        #draw buttons
        for letter in letters:
            x,y,ltr,visible = letter
            if visible:
                pygame.draw.circle(windows,BLACK,(x,y),RADIUS,3)
                text = LETTER_FONT.render(ltr,1,BLACK)
                windows.blit(text ,(x- text.get_width()/2,y-text.get_height()/2))
        windows.blit(images[hangman_status],(150,80))
        pygame.display.update()
        

    noguesses=0
    #fonts 
    LETTER_FONT = pygame.font.SysFont('comicsans', 25)
    WORD_FONT=pygame.font.SysFont('comicsans', 40)
    WINNERORLOOSER_FONT=pygame.font.SysFont('comicsans', 20)
    TITLE_FONT = pygame.font.SysFont('comicsans',40)
    HINT_FONT = pygame.font.SysFont('comicsans',25)
    #Hangman Gameloop

    def display_message(message):
        pygame.time.delay(1000)
        windows.fill(BLUE)
        text= WINNERORLOOSER_FONT.render(message,1,BLACK)
        windows.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)

    FPS=60
    clock=pygame.time.Clock()
    run = True
    while run:

        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                m_x , m_y=pygame.mouse.get_pos()
                print(m_x,m_y)
                for letter in letters:
                    x,y,ltr,visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis<RADIUS:
                            letter[3]=False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status +=1
                                noguesses +=1
        
                            
    
        
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message(f"Yeahh {name} YOU WON!! you took {noguesses} guess {word}" )
            break
        if hangman_status == 6 :
            display_message(f" you lost{name} better luck next time the word was {word} ")
            break
    #hint
    hint_letter = ""

# Add a random character from word to hint_letter
    hint_letter += random.choice(word)
    hint_letter = hint_letter.upper()
 
       
    pygame.quit()
hangman()
