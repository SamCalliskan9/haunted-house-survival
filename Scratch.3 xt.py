Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... import pygame
... import random
... 
... pygame.init()
... 
... WIDTH, HEIGHT = 800, 600
... screen = pygame.display.set_mode((WIDTH, HEIGHT))
... pygame.display.set_caption("Haunted House Prototype")
... 
... clock = pygame.time.clock()
... 
... # ---------- PLAYER SETTINGS ----------
... player_pos = [400, 300]
... player_speed = 3
... flashlight_on = True
... 
... # ---------- WALLS (COLLOSIONS) ----------
... walls = [
...     pygame.Rect(100, 200, 600, 20), # üst duvar
...     pygame.Rect(100, 480, 600, 20), # alt duvar
...     pygame.Rect(100, 100, 20, 400), # sol duvar
...     pygame.Rect(600, 100, 20, 400)  # sağ duvar
... ]
... 
... # ----------- RANDOM PARANORMAL EVENT -----------
... def paranormal_event():
...     chance = random.randint(1, 200)
...     if chance == 1:
...         print("Paranormal ses tetiklendi... kapı gıcırdıyor...")
... 
... # ---------- PLAYER MOVEMENT ------------
... def move_player(keys):
...     global player_pos
... 
...     new_x, new_y = player_pos()
... 
    if keys[pygame.K_w]:
        new_y -= player_speed
    if keys[pygame.k_s]:
        new_y += player_speed
    if keys[pygame.k_a]:
        new_x -= player_speed
    if keys[pygame.K_d]:
        new_x += player_speed

    new_rect = pygame.Rect(new_x, new_y, 20, 20)

    for wall in walls:
        if new_rect.colliderect(wall):
            return

    player_pos[0] = new_x
    player_pos[1] = new_y

# ----------- MAİN GAME LOOP -----------
running = True
while running:
    screen.fill((10, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fener aç/kapa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                flashlight_on = not flashlight_on

    keys = pygame.key.get_pressed()
    move_player(keys)

    # Paranormal efekt tetikleme
    paranormal_event()

    # Player çiz
    pygame.draw.rect(screen, (200, 200, 200), (*player_pos, 20, 20))

    # Fener efekti
    if flashlight_on:
        pygame.draw.circle(screen, (255, 255, 150), player_pos, 120,2)

    # Duvarları çiz
    for wall in walls:
        pygame.draw.rect(screen, (80, 0, 0), wall)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

