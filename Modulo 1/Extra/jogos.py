import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Matar Zumbi - Atire com espaço!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
GRAY = (100, 100, 100)

clock = pygame.time.Clock()
FPS = 60

player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

zombie_size = 50
zombies = []  # Agora cada zumbi é [x, y, has_sword]

bullet_size = 8
bullet_speed = 15
bullets = []  # Cada bala é [x, y, dir_x, dir_y]

font = pygame.font.SysFont(None, 36)

score = 0
level = 1

spawn_event = pygame.USEREVENT + 1
spawn_delay = 1500
zombie_speed = 2

game_state = "menu"

last_shot_time = 0
shot_cooldown = 300  # ms

player_health = 5  # Vida do jogador

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def draw_text(text, pos, color=WHITE):
    render = font.render(text, True, color)
    screen.blit(render, pos)

def spawn_zombie():
    side = random.choice(['top', 'bottom', 'left', 'right'])
    if side == 'top':
        x = random.randint(0, WIDTH - zombie_size)
        y = 0
    elif side == 'bottom':
        x = random.randint(0, WIDTH - zombie_size)
        y = HEIGHT - zombie_size
    elif side == 'left':
        x = 0
        y = random.randint(0, HEIGHT - zombie_size)
    else:
        x = WIDTH - zombie_size
        y = random.randint(0, HEIGHT - zombie_size)
    has_sword = random.choice([True, False])  # 50% chance de ter espada
    zombies.append([x, y, has_sword])

def move_zombies():
    for i, (zx, zy, has_sword) in enumerate(zombies):
        px, py = player_pos[0] + player_size / 2, player_pos[1] + player_size / 2
        dx = px - (zx + zombie_size / 2)
        dy = py - (zy + zombie_size / 2)
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx /= dist
            dy /= dist
        zx += dx * zombie_speed
        zy += dy * zombie_speed
        zombies[i] = [zx, zy, has_sword]

def normalize_vector(dx, dy):
    dist = math.hypot(dx, dy)
    if dist == 0:
        return 0, 0
    return dx / dist, dy / dist

def draw_player():
    pygame.draw.rect(screen, GREEN, (*player_pos, player_size, player_size))

def draw_zombies():
    for zx, zy, has_sword in zombies:
        pygame.draw.rect(screen, RED, (zx, zy, zombie_size, zombie_size))
        if has_sword:
            sword_rect = pygame.Rect(zx + zombie_size, zy + zombie_size // 3, 10, zombie_size // 3)
            pygame.draw.rect(screen, GRAY, sword_rect)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (int(bullet[0]), int(bullet[1])), bullet_size)

def show_score():
    draw_text(f"Zumbis mortos: {score}", (10, 10))

def show_level():
    draw_text(f"Nível: {level}", (10, 50))

def show_health():
    draw_text(f"Vida: {player_health}", (WIDTH - 150, 10), (255, 0, 0))

def reset_game():
    global zombies, bullets, score, player_pos, level, zombie_speed, spawn_delay, player_health
    zombies = []
    bullets = []
    score = 0
    level = 1
    player_pos[:] = [WIDTH // 2, HEIGHT // 2]
    player_health = 5
    zombie_speed = initial_zombie_speed
    spawn_delay = initial_spawn_delay
    pygame.time.set_timer(spawn_event, spawn_delay)

def start_game(dif):
    global spawn_delay, zombie_speed, level, game_state, initial_spawn_delay, initial_zombie_speed, player_health
    if dif == "Facil":
        spawn_delay = 1800
        zombie_speed = 1.5
    elif dif == "Medio":
        spawn_delay = 1200
        zombie_speed = 2.5
    else:
        spawn_delay = 800
        zombie_speed = 4
    initial_spawn_delay = spawn_delay
    initial_zombie_speed = zombie_speed
    player_health = 5
    pygame.time.set_timer(spawn_event, spawn_delay)
    reset_game()
    game_state = "playing"

def menu():
    screen.fill(BLACK)
    draw_text("Selecione o nível:", (WIDTH // 2 - 100, 100))
    
    buttons = {
        "Facil": pygame.Rect(WIDTH // 2 - 100, 200, 200, 50),
        "Medio": pygame.Rect(WIDTH // 2 - 100, 300, 200, 50),
        "Dificil": pygame.Rect(WIDTH // 2 - 100, 400, 200, 50),
    }
    for text, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        draw_text(text, (rect.x + 60, rect.y + 10), BLACK)
    return buttons

running = True
buttons = None

while running:
    if game_state == "menu":
        buttons = menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for dif, rect in buttons.items():
                    if rect.collidepoint(mx, my):
                        start_game(dif)
                        break

    elif game_state == "playing":
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == spawn_event:
                spawn_zombie()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_time = pygame.time.get_ticks()
                    if current_time - last_shot_time > shot_cooldown:
                        px = player_pos[0] + player_size / 2
                        py = player_pos[1] + player_size / 2
                        mx, my = pygame.mouse.get_pos()
                        dx = mx - px
                        dy = my - py
                        dir_x, dir_y = normalize_vector(dx, dy)
                        bullets.append([px, py, dir_x, dir_y])
                        last_shot_time = current_time
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_pos[0] -= player_speed
            if player_pos[0] < 0:
                player_pos[0] = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_pos[0] += player_speed
            if player_pos[0] > WIDTH - player_size:
                player_pos[0] = WIDTH - player_size
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_pos[1] -= player_speed
            if player_pos[1] < 0:
                player_pos[1] = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_pos[1] += player_speed
            if player_pos[1] > HEIGHT - player_size:
                player_pos[1] = HEIGHT - player_size
        
        for bullet in bullets[:]:
            bullet[0] += bullet[2] * bullet_speed
            bullet[1] += bullet[3] * bullet_speed
            if bullet[0] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
                bullets.remove(bullet)
        
        move_zombies()

        player_rect = pygame.Rect(*player_pos, player_size, player_size)

        for zombie in zombies[:]:
            zx, zy, has_sword = zombie
            zombie_rect = pygame.Rect(zx, zy, zombie_size, zombie_size)
            
            if check_collision(player_rect, zombie_rect):
                damage = 2 if has_sword else 1
                player_health -= damage
                zombies.remove(zombie)
                if player_health <= 0:
                    game_state = "gameover"
            
            for bullet in bullets[:]:
                bullet_rect = pygame.Rect(bullet[0] - bullet_size, bullet[1] - bullet_size, bullet_size*2, bullet_size*2)
                if zombie_rect.colliderect(bullet_rect):
                    zombies.remove(zombie)
                    bullets.remove(bullet)
                    score += 1

                    if score % 10 == 0:
                        level += 1
                        zombie_speed += 0.5
                        spawn_delay = max(200, spawn_delay - 150)
                        pygame.time.set_timer(spawn_event, spawn_delay)
                    break
        
        draw_player()
        draw_zombies()
        draw_bullets()
        show_score()
        show_level()
        show_health()

    elif game_state == "gameover":
        screen.fill(BLACK)
        draw_text("Game Over!", (WIDTH // 2 - 70, HEIGHT // 2 - 50))
        draw_text(f"Zumbis mortos: {score}", (WIDTH // 2 - 100, HEIGHT // 2))
        draw_text("Pressione R para voltar ao menu", (WIDTH // 2 - 160, HEIGHT // 2 + 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = "menu"

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
