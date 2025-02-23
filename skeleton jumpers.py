import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = score_font.render(f'{current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (800,200))
    screen.blit(score_surf,score_rect)

pygame.init()
text1 = pygame.font.Font(None,50)
text2 = pygame.font.Font(None,50)
text3 = pygame.font.Font(None,50)
text4 = pygame.font.Font(None,50)

pygame.mixer.init
screen = pygame.display.set_mode((1600,800))
pygame.display.set_caption('bandit dodger')
clock = pygame.time.Clock()
score_font = pygame.font.Font('C:/Users/Administrator/Desktop/patriot pixels/images/art work for games/Super Cartoon.ttf', 50)
game_active = True

sky = pygame.image.load('C:/Users/Administrator/Desktop/patriot pixels/images/art work for games/sky2.png').convert_alpha()
ground = pygame.image.load('C:/Users/Administrator/Desktop/patriot pixels/images/art work for games/ground.png').convert_alpha()
logo = pygame.image.load('C:/Users/Administrator/Desktop/patriot pixels/images/american flag.png')
text1 = text1.render('patriot', False, 'Red')
text2 = text2.render('pixels', False, 'White')
text3 = text3.render('studios', False, 'Blue')
text4 = text4.render('developed by',False, 'White')

background_music = pygame.mixer.music.load('C:/Users/Administrator/Desktop/patriot pixels/music/medival background.mp3')

score = score_font.render('my game', False, 'Black')
score_rect = score.get_rect(center =(700,250))

hitler = pygame.image.load('C:/Users/Administrator/Desktop/patriot pixels/images/art work for games/zombie.png').convert_alpha()
hitler_rect = hitler.get_rect(topleft =(10,445))

player = pygame.image.load('C:/Users/Administrator/Desktop/patriot pixels/images/art work for games/jumper.png').convert_alpha()
player_rect = player.get_rect(topleft =(1500,400))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 600:
                    player_gravity = -25

        #if event.type == pygame.MOUSEMOTION:  
            #if player_rect.collidepoint(event.pos): print('collision')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 600:
                player_gravity = -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                hitler_rect.left = 10
    if game_active:
        screen.blit(sky,(0,0))
        screen.blit(ground,(-5,600))
        hitler_rect.x +=10
        if hitler_rect.right >= 1700: hitler_rect.left  = 10
        screen.blit(hitler,hitler_rect)
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 600: player_rect.bottom = 600
        screen.blit(player,player_rect)
        pygame.draw.rect(screen,'Blue',score_rect,6)
        screen.blit(score,score_rect)
        display_score()
        pygame.mixer.music.play(-1)
        #collision
        if hitler_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Black')
        screen.blit(logo,(0,0))
        screen.blit(text1,(790,50))
        screen.blit(text2,(790,80))
        screen.blit(text3,(790,110))
        screen.blit(text4,(720,20))
        

    pygame.display.update()
    clock.tick(60)
