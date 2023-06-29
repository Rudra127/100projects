import random
import pygame
def dice2():
    pygame.init()
    WIDTH , HEIGHT = 800,600
    windows = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Dice")
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    #if you want to increase the possiblity to get the particular number than add that number to this list multiple times
    dice1 = [0,1,2,3,4,5]
    dice_num= random.choice(dice1)

    BLACK=(0,0,0)
    #iamges
    images = []
    for i in range(0,6):
        img = '2dice\dice'+str(i)+'.png'
        imge=pygame.image.load(img)
        images.append(imge) 

    #color
    BLUE =(122,194,212)
    #font
    LETTER_FONT = pygame.font.SysFont('comicsans',30)
    def drawthedice():
        windows.fill(BLUE)
        windows.blit(images[dice_num],(60,65))
        text = LETTER_FONT.render(f"hey if you want to restat than click this line ",1,BLACK)
        windows.blit(text,(WIDTH/2-text.get_width()/2,10))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        drawthedice()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x , m_y = pygame.mouse.get_pos() 
                print(m_x,m_y)
            if event.type == pygame.MOUSEBUTTONDOWN and m_x>93 and m_x<697:
                dice2()
    pygame.quit()

dice2()
