import pygame
import random

# Configuración de la ventana
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong 3D')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Palas y pelota
paddle_width = 15
paddle_height = 100
ball_size = 15

player1_pos = [50, 250]
player2_pos = [735, 250]
ball_pos = [400, 300]
ball_vel = [random.choice([-4, 4]), random.choice([-4, 4])]

# Puntuación
player1_score = 0
player2_score = 0

# Reloj para controlar la velocidad
clock = pygame.time.Clock()

# Función para dibujar elementos
def draw_elements():
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, pygame.Rect(player1_pos[0], player1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, pygame.Rect(player2_pos[0], player2_pos[1], paddle_width, paddle_height))
    pygame.draw.circle(window, WHITE, (ball_pos[0], ball_pos[1]), ball_size)
    
    # Mostrar puntuación
    font = pygame.font.SysFont('Arial', 24)
    text1 = font.render(f'Jugador 1: {player1_score}', True, WHITE)
    text2 = font.render(f'Jugador 2: {player2_score}', True, WHITE)
    window.blit(text1, (50, 10))
    window.blit(text2, (600, 10))
    
    pygame.display.update()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de las palas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= 5
    if keys[pygame.K_s] and player1_pos[1] < 500:
        player1_pos[1] += 5
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= 5
    if keys[pygame.K_DOWN] and player2_pos[1] < 500:
        player2_pos[1] += 5

    # Movimiento de la pelota
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Colisiones con las paredes
    if ball_pos[1] <= 0 or ball_pos[1] >= 600:
        ball_vel[1] = -ball_vel[1]

    # Colisiones con las palas
    if player1_pos[0] < ball_pos[0] < player1_pos[0] + paddle_width and player1_pos[1] < ball_pos[1] < player1_pos[1] + paddle_height:
        ball_vel[0] = -ball_vel[0]
    
    if player2_pos[0] < ball_pos[0] < player2_pos[0] + paddle_width and player2_pos[1] < ball_pos[1] < player2_pos[1] + paddle_height:
        ball_vel[0] = -ball_vel[0]

    # Comprobación de puntuación
    if ball_pos[0] <= 0:  # Jugador 2 anota
        player2_score += 1
        ball_pos = [400, 300]  # Reseteamos la pelota al centro
        ball_vel = [random.choice([-4, 4]), random.choice([-4, 4])]  # Nuevo ángulo para la pelota
    
    if ball_pos[0] >= 800:  # Jugador 1 anota
        player1_score += 1
        ball_pos = [400, 300]  # Reseteamos la pelota al centro
        ball_vel = [random.choice([-4, 4]), random.choice([-4, 4])]  # Nuevo ángulo para la pelota

    draw_elements()
    clock.tick(60)

pygame.quit()
