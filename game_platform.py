import pygame  
import random  
from settings import screen, screen_width, screen_height, brown  

platform_width = 60  
platform_height = 15

# Глобальный список платформ
platforms = []

def log_debug(text):
    with open("debug.txt", "a") as f:
        f.write(text + "\n")

def create_platform(x, y):
    global platforms
    platforms.append((x, y))
    print(f"✅ Создана платформа: ({x}, {y})")
    log_debug(f"✅ Создана платформа: ({x}, {y})")

def create_starting_platforms(player_x, player_y):
    global platforms
    platforms.clear()  


    start_platform_x = player_x - platform_width // 2  
    start_platform_y = player_y + 50  
    create_platform(start_platform_x, start_platform_y)  


    for i in range(5):
        x = random.randint(0, screen_width - platform_width)
        y = platforms[-1][1] - random.randint(80, 120)
        create_platform(x, y)

    log_debug(f"🎯 Итоговый список платформ: {platforms}")

def get_platforms():
    return platforms

def draw_platform(x, y):
    pygame.draw.rect(screen, brown, (x, y, platform_width, platform_height))

def check_collision(rect):
    global platforms
    for platform in platforms:
        platform_rect = pygame.Rect(platform[0], platform[1], platform_width, platform_height)
        if rect.colliderect(platform_rect):
            return platform_rect
    return None

def generate_new_platforms(player_y):
    global platforms

    # Удаляем платформы, которые ушли за нижний край экрана
    platforms = [p for p in platforms if p[1] < screen_height]

    # Определяем максимальную высоту платформы
    if platforms:
        highest_y = min(p[1] for p in platforms)
    else:
        highest_y = screen_height

    # Генерируем несколько платформ выше, если игрок поднимается вверх
    while highest_y > player_y - screen_height // 2:
        new_x = random.randint(0, screen_width - platform_width)
        new_y = highest_y - random.randint(80, 120)
        create_platform(new_x, new_y)
        highest_y = new_y  # Обновляем высоту для следующей платформы
