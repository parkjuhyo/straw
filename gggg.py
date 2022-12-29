import pygame
pygame.init()
screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Keyboard Test")
clock = pygame.time.Clock()
run = True; key_status = ""; key = None
while run:
# 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            key_status = "Key Down"
            key = event.key
        elif event.type == pygame.KEYUP:
            key_status = "Key Up"
            key = event.key
# 2) 게임 상태 업데이트
# 3) 게임 상태 그리기
    screen.fill(pygame.color.Color(255, 255, 255))
# 글자 넣기
    font = pygame.font.SysFont("arial",20,True,True)
    if key != None:
        text = font.render(key_status,True,(0,0,0))
        screen.blit(text, (10,10))
    pygame.display.flip()
clock.tick(60)
pygame

