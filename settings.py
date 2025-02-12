import pygame  # Импорт библиотеки Pygame для работы с графикой и событиями

# Инициализация Pygame
pygame.init()
pygame.font.init()

# Настройки экрана
screen_width, screen_height = 360, 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smart Jump")

# Цвета
light_blue = (173, 216, 230)  # Цвет для облаков
white = (255, 255, 255)       # Цвет фона
green = (34, 139, 34)         # Цвет для земли
brown = (139, 69, 19)         # Цвет для платформ
yellow = (255, 255, 0)        # Цвет для курицы
orange = (255, 165, 0)        # Цвет для клюва и лап
black = (0, 0, 0)             # Цвет для глаз

# Пути к изображениям
PLAYER_IMAGE = 'assets/images/player.png'

# Пути к звуковым файлам
SOUND_MENU = 'assets/sounds/background_music.mp3'
SOUND_JUMP = 'assets/sounds/jumping_sound.mp3'
SOUND_BACKGROUND = 'assets/sounds/music_game1.mp3'

# Настройки для звука
music_volume = 0.5  # фоновая музыка
sound_volume = 0.7  # звуковые эффекты

# Физика движения
jump_speed = -15  # Скорость прыжка
horizontal_speed = 5  # Скорость движения влево/вправо
gravity = 0.8  # Гравитация

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
