import pygame  
from settings import screen, screen_width, screen_height, PLAYER_IMAGE, SOUND_JUMP, jump_speed, gravity  
from game_platform import platforms, check_collision  

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0
        self.vel_x = 0
        self.jump_sound = pygame.mixer.Sound(SOUND_JUMP)
        self.jump_sound.set_volume(0.5)

        self.check_initial_platform()
        print(f"✅ Игрок создан на ({self.rect.x}, {self.rect.y})")

    def check_initial_platform(self):
        for platform in platforms:
            if platform[1] >= screen_height - 200:
                self.rect.y = platform[1] - self.rect.height
                print(f"✅ Игрок поставлен на платформу: ({self.rect.x}, {self.rect.y})")
                return

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.vel_x = -4
            print("⬅️ Игрок движется влево")
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 4
            print("➡️ Игрок движется вправо")
        else:
            self.vel_x = 0

    def apply_gravity(self):
        self.vel_y += gravity
        self.rect.y += self.vel_y

    def check_collision(self):
        platform_collided = check_collision(self.rect)
        if platform_collided and self.vel_y >= 0:
            self.rect.y = platform_collided.top - self.rect.height
            self.vel_y = jump_speed  
            print(f"🔄 Игрок прыгнул с платформы ({self.rect.x}, {self.rect.y})")
            self.jump_sound.play()

    def update(self, keys):
        self.move(keys)
        self.apply_gravity()
        self.check_collision()

        self.rect.x += self.vel_x


        if self.rect.right < 0:
            self.rect.left = screen_width
        elif self.rect.left > screen_width:
            self.rect.right = 0

        print(f"📍 Игрок на ({self.rect.x}, {self.rect.y})")

    def draw(self):
        screen.blit(self.image, self.rect)
