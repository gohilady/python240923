import pygame
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('블럭 깨기 게임')

# 공 속도
ball_speed = [4, -4]

# 패들
paddle_width = 200
paddle_height = 15
paddle_speed = 10
paddle = pygame.Rect(SCREEN_WIDTH // 2 - paddle_width // 2, SCREEN_HEIGHT - 40, paddle_width, paddle_height)

# 공
ball_radius = 10
ball = pygame.Rect(SCREEN_WIDTH // 2 - ball_radius // 2, SCREEN_HEIGHT // 2 - ball_radius // 2, ball_radius * 2, ball_radius * 2)

# 블럭 설정
block_rows = 5
block_cols = 10
block_width = SCREEN_WIDTH // block_cols
block_height = 30

blocks = []
for row in range(block_rows):
    block_row = []
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        block_row.append(block)
    blocks.append(block_row)

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 움직임 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.x += paddle_speed

    # 공 움직임
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 공이 벽에 부딪히면 반대 방향으로 움직임
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # 공이 바닥에 떨어지면 게임 오버
    if ball.bottom >= SCREEN_HEIGHT:
        running = False

    # 공이 패들에 닿으면 반대 방향으로 튕김
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 공이 블럭에 닿으면 반대 방향으로 튕기고 블럭 제거
    for row in blocks:
        for block in row:
            if ball.colliderect(block):
                ball_speed[1] = -ball_speed[1]
                row.remove(block)
                break

    # 화면 그리기
    screen.fill(BLACK)

    # 패들 그리기
    pygame.draw.rect(screen, BLUE, paddle)

    # 공 그리기
    pygame.draw.ellipse(screen, WHITE, ball)

    # 블럭 그리기
    for row in blocks:
        for block in row:
            pygame.draw.rect(screen, RED, block)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임
    clock.tick(60)

# 종료 처리
pygame.quit()
