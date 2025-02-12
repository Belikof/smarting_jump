import pygame  # Импорт библиотеки Pygame для работы с графикой и событиями
import random  # Импорт модуля random для генерации случайных чисел (например, для расположения платформ)
from settings import screen_width, screen_height, screen, green  # Импортируем настройки игры, такие как размеры экрана, цвета и гравитация

# Настройки облаков
cloud_width = 80
cloud_height = 40
clouds = []
light_blue = (173, 216, 230)

# Создаем начальные облака
for _ in range(5):
    cloud_x = random.randint(0, screen_width)
    cloud_y = random.randint(0, screen_height // 2)
    clouds.append((cloud_x, cloud_y))

def draw_cloud(x, y):
    pygame.draw.circle(screen, light_blue, (x + 10, y + 10), 20)
    pygame.draw.circle(screen, light_blue, (x + 20, y), 20)
    pygame.draw.circle(screen, light_blue, (x + 60, y + 20), 20)
    pygame.draw.ellipse(screen, light_blue, (x + 20, y + 10, 40, 20))

def draw_objects():
    for i in range(len(clouds)):
        cloud_x, cloud_y = clouds[i]
        draw_cloud(cloud_x, cloud_y)
        clouds[i] = (cloud_x - 1, cloud_y)  # Движение облаков влево
        if cloud_x + cloud_width < 0:
            clouds[i] = (screen_width, random.randint(0, screen_height // 2))

    pygame.draw.rect(screen, green, (0, screen_height - 50, screen_width, 50))
