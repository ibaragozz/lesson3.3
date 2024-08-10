import pygame
import random

pygame.init()

# Настройки экрана и цвета
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Инопланетная охота")
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Загружаем изображение цели и устанавливаем размеры
target_image = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

# Устанавливаем начальные координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Подсчет попаданий и промахов
hits = 0
misses = 0
max_misses = 3

# Шрифт для отображения счета и промахов
font = pygame.font.Font(None, 36)

# Время последнего перемещения цели
last_move_time = pygame.time.get_ticks()
move_interval = 1000  # интервал перемещения цели в миллисекундах (1 секунда)

running = True
while running:
    screen.fill(color)
    current_time = pygame.time.get_ticks()

    # Перемещаем цель через каждый move_interval
    if current_time - last_move_time > move_interval:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        last_move_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещаем цель и изменяем цвет фона при попадании
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                hits += 1
            else:
                # Увеличиваем количество промахов
                misses += 1
                if misses >= max_misses:
                    running = False  # Заканчиваем игру, если промахов стало 3

    # Отображаем цель
    screen.blit(target_image, (target_x, target_y))

    # Отображаем счет и количество промахов на экране
    score_text = font.render(f"Счет: {hits}", True, (255, 255, 255))
    misses_text = font.render(f"Промахи: {misses}/{max_misses}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(misses_text, (10, 50))

    pygame.display.update()

# Вывод сообщения об окончании игры с финальным счетом
end_font = pygame.font.Font(None, 72)
end_text = end_font.render("Игре конец!", True, (255, 0, 0))
final_score_text = end_font.render(f"Было сбито {hits} тарелок!", True, (255, 255, 255))

screen.fill((0, 0, 0))
screen.blit(end_text,
            (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT // 2 - end_text.get_height() // 2 - 40))
screen.blit(final_score_text, (
SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - final_score_text.get_height() // 2 + 40))

pygame.display.update()
pygame.time.wait(3000)  # Ожидание перед закрытием

pygame.quit()
