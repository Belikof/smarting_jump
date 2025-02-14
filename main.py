import sys
import os
import pygame  
import random  
from settings import screen, white, screen_width, screen_height, SOUND_MENU, music_volume  
from objects import draw_objects  
import game_platform  
from player import Player  
print(os.getcwd())
pygame.init()

def log_debug(text):
    with open("debug.txt", "a") as f:
        f.write(text + "\n")

def draw_text(text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x - text_surface.get_width() // 2, y))

def game_over_screen():
    screen.fill((0, 0, 0))  # Чёрный фон
    draw_text("GAME OVER", 50, screen_width // 2, 200)
    
    buttons = ["Restart", "Main Menu"]
    selected = 0  # Индекс выбранной кнопки
    
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        draw_text("GAME OVER", 50, screen_width // 2, 200)

        for i, btn in enumerate(buttons):
            color = (255, 0, 0) if i == selected else (255, 255, 255)
            draw_text(btn, 30, screen_width // 2, 300 + i * 70, color)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(buttons)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(buttons)
                elif event.key == pygame.K_RETURN:
                    if buttons[selected] == "Restart":
                        return "restart"
                    elif buttons[selected] == "Main Menu":
                        return "menu"

        clock.tick(30)

def main_menu():
    pygame.init()
    screen_menu = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Menu")
    font_menu = pygame.font.Font(None, 40)
    clock = pygame.time.Clock()

    menu_items = ["Start game", "Records", "Quit"]
    selected = 0

    pygame.mixer.music.load(SOUND_MENU)
    pygame.mixer.music.set_volume(music_volume)
    pygame.mixer.music.play(-1)

    while True:
        screen_menu.fill((0, 0, 0))

        for index, item in enumerate(menu_items):
            color = (255, 255, 255) if index == selected else (150, 150, 150)
            text = font_menu.render(item, True, color)
            screen_menu.blit(text, (screen_width // 2 - text.get_width() // 2, 200 + index * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if menu_items[selected] == "Start game":
                        return  # Выход из меню для запуска игры
                    elif menu_items[selected] == "Records":
                        print("🔹 Открытие таблицы рекордов (функция пока не реализована)")  
                    elif menu_items[selected] == "Quit":
                        pygame.quit()
                        sys.exit()

        clock.tick(30)

def game_loop():
    print("🔹 Игра началась!")
    player_start_x = screen_width // 2  
    player_start_y = screen_height - 150  

    game_platform.create_starting_platforms(player_start_x, player_start_y)  

    player = Player(player_start_x, player_start_y)  
    clock = pygame.time.Clock()

    scroll_y = 0  

    running = True
    while running:
        screen.fill(white)  

        draw_objects()  

        if player.rect.y > screen_height:  # Если игрок падает вниз, игра окончена
            action = game_over_screen()
            if action == "restart":
                game_loop()  # Начинаем игру заново
            elif action == "menu":
                main_menu()  # Возвращаемся в меню

        if player.rect.y < screen_height // 2:
            scroll_y = screen_height // 2 - player.rect.y
            player.rect.y = screen_height // 2  
            
            for i in range(len(game_platform.platforms)):
                game_platform.platforms[i] = (game_platform.platforms[i][0], game_platform.platforms[i][1] + scroll_y)

        for platform in game_platform.get_platforms():
            game_platform.draw_platform(platform[0], platform[1])

        game_platform.generate_new_platforms(player.rect.y)

        keys = pygame.key.get_pressed()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(keys)  
        player.draw()  

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_menu()
    game_loop()  
