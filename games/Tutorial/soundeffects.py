import  pygame
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sound Effects')

#creating sound effects

#define sounds
sound1_hit = pygame.mixer.Sound('../assets/sound1Hit.wav')
sound2_zap = pygame.mixer.Sound('../assets/sound1Zap.wav')

#play sounds effects
sound1_hit.play()
pygame.time.delay(2000)
sound2_zap.play()
pygame.time.delay(2000)

#change the volume of sound effce
sound2_zap.set_volume(.1)

#load background music
pygame.mixer.music.load('../assets/pixel.ai_ytk1ytazndqtytbkzi00nzq1lwjlogqtymrjnddmzwe2y2e1')

#play and stop music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(20000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()