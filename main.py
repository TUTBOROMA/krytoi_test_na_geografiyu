import pygame
import sys
arg = sys.argv
rec = 0
print(pygame.font.get_fonts())
print("Start")
whif = False
def main():
    pygame.display.init()
    screen = pygame.display.set_mode((1200, 800))
    image = pygame.image.load("data/image.jpg").convert_alpha()
    FPS = 60
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("С днём рождения!")
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_SPACE:
                    n = event.key - 48
                    running = False
        screen.blit(image, image.get_rect())
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__':
    main()
pygame.display.init()
sc = screen = pygame.display.set_mode((1200, 800))
image = pygame.image.load("data/image.jpg").convert_alpha()
FPS = 60
pygame.init()
pygame.mixer.init()
for i in range(100):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        sc.fill((184, 115, 51))
        f6 = pygame.font.SysFont("Serif", 278)
        text6 = f6.render('3', True, (184, 51, 35))
        sc.blit(text6, (377, 375))
    pygame.display.update()
    pygame.time.delay(15)
sc.fill((184, 115, 51))
for i in range(70):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f7 = pygame.font.SysFont("Serif", 278)
    text7 = f7.render('2', True, (184, 51, 35))
    sc.blit(text7, (377, 375))
    pygame.display.update()
    pygame.time.delay(15)
sc.fill((184, 115, 51))
for i in range(70):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f8 = pygame.font.SysFont("Serif", 278)
    text8 = f8.render('1', True, (184, 51, 35))
    sc.blit(text8, (377, 375))
    pygame.display.update()
    pygame.time.delay(15)
sc.fill((184, 155, 51))
for i in range(75):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    f9 = pygame.font.SysFont("Serif", 278)
    text9 = f9.render('СТАРТ!', True, (45, 95, 255))
    sc.blit(text9, (177, 375))
    pygame.display.update()
    pygame.time.delay(15)
sc = screen = pygame.display.set_mode((1431, 775))
image, running, clock = pygame.image.load("data/m1.jpg").convert_alpha(), True, pygame.time.Clock()
pygame.display.set_caption("С днём рождения!")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                n, running = event.key - 48, False
                print(n)
                if n == 4:
                    rec = rec + 10
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4:
                n, running = event.key - (1073741864 + 48), False
                print(n)
                if n == 4:
                    rec = rec + 10
    screen.blit(image, image.get_rect())
    pygame.display.flip()
pygame.quit()
def main3():
    a = 1
    pygame.display.init()
    sc = screen = pygame.display.set_mode((1200, 800))
    FPS = 60
    pygame.init()
    pygame.mixer.init()
    for i in range(30):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            sc.fill((137, 155, 255))
            f6 = pygame.font.SysFont("Serif", 58)
            text6 = f6.render('Ответ засчитан! Ожидайте:' + str(a) + 'сек', True, (184, 51, 35))
            sc.blit(text6, (240, 375))
        pygame.display.update()
        pygame.time.delay(15)
        a = a - 0.03
main3()
sc = screen = pygame.display.set_mode((1152, 767))
image, running, clock = pygame.image.load("data/m2.jpg").convert_alpha(), True, pygame.time.Clock()
pygame.display.set_caption("С днём рождения!")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                n, running = event.key - 48, False
                print(n)
                if n == 2:
                    rec = rec + 10
                    whif = True
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4:
                n, running = event.key - 1073741864 - 48, False
                print(n)
                if n == 2:
                    rec = rec + 10
                    whif = True
    screen.blit(image, image.get_rect())
    pygame.display.flip()
sc = screen = pygame.display.set_mode((1000, 751))
image, running, clock = pygame.image.load("data/m3.png").convert_alpha(), True, pygame.time.Clock()
pygame.display.set_caption("С днём рождения!")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                n, running = event.key - 48, False
                print(n)
                if n == 1:
                    rec = rec + 10
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4:
                n, running = event.key - 1073741864 - 48, False
                print(n)
                if n == 1:
                    rec = rec + 10
    screen.blit(image, image.get_rect())
    pygame.display.flip()
sc = screen = pygame.display.set_mode((724, 724))
image, running, clock = pygame.image.load("data/m4.png").convert_alpha(), True, pygame.time.Clock()
pygame.display.set_caption("аоцлцоэыдацуэдуэацо")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                n, running = event.key - 48, False
                print(n)
                if n == 4:
                    rec = rec + 10
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4:
                n, running = event.key - 1073741864 - 48, False
                print(n)
                if n == 4:
                    rec = rec + 10
    screen.blit(image, image.get_rect())
    pygame.display.flip()
sc = screen = pygame.display.set_mode((870, 583))
image, running, clock = pygame.image.load("data/m5.jpg").convert_alpha(), True, pygame.time.Clock()
pygame.display.set_caption("аоцлцоэыдацуэдуэацо")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                n, running = event.key - 48, False
                print(n)
                if n == 1:
                    rec = rec + 10
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4:
                n, running = event.key - 1073741864 - 48, False
                print(n)
                if n == 1:
                    rec = rec + 10
    screen.blit(image, image.get_rect())
    pygame.display.flip()
pygame.quit()
if whif == True:
    print("Привет! Это рубрика - ДОПОЛНИТЕЛЬНЫЙ ВОПРОС")
    print("Помнишь, какой город был правильным ответом на 2 вопрос? Я знаю, что ты правильно ответил там")
    print("Напиши цифру с городом, который был на втором вопросе правильным ответом и нажми Enter")
    ar = int(input("1 - Москва, 2 - Лас-Вегас, 3 - Нью-Йорк, 4 - Стамбул, 5 - Санкт-Петербург, 6 - Дубай ------- "))
    if ar == 1:
        print("Вы ответили правильно на дополнительный вопрос! +5 баллов")
        rec = rec + 5
pygame.init()
pygame.display.init()
sc = screen = pygame.display.set_mode((870, 583))
image, running, clock = pygame.image.load("data/m6.png").convert_alpha(), True, pygame.time.Clock()
pygame.font.init()
FPS = 60
pygame.mixer.init()
pygame.display.set_caption("анхуцанчанщанбебра")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                n, running = event.key - 48, False
                print(n)
                if n == 1:
                    rec = rec + 10
    screen.blit(image, image.get_rect())
    pygame.display.flip()
#===========================================
sc = screen = pygame.display.set_mode((922, 615))
image, running, clock = pygame.image.load("data/m7.jpg").convert_alpha(), True, pygame.time.Clock()
pygame.display.set_caption("аоцлцоэыдацуэдуэацо")
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                n, running = event.key - 48, False
                print(n)
                if n == 2:
                    rec = rec + 10
            if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4:
                n, running = event.key - 1073741864 - 48, False
                print(n)
                if n == 2:
                    rec = rec + 10
    screen.blit(image, image.get_rect())
    pygame.display.flip()
print("-----------------------------------------------------")
print("Итак, конец!")
if rec % 10 == 0:
    bebra = 'Вы набрали, ' + str(rec) + 'очков. А ответили вы на ' + str(round(round(rec) / 10)) + ' вопросов! '
else:
    bebra = 'Вы набрали, ' + str(rec) + 'очков. А ответили вы на ' + str(round((round(rec - 5)) / 10)) + ' вопросов !'
FPS = 60
print("Спасибо за прохождение! Если вы хотите переместить этот .exe файл в другую папку, то в этой же директории должна лежать папка data !")
print("Сделал Turbo Roma 17.07.2022. Discord: КТО НАСРАЛ ТОТ УБРАЛ #2509")
pygame.quit()
#-----------------------------
import pygame
pygame.init()
sc = screen = pygame.display.set_mode((1200, 800))
running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        sc.fill((0, 153, 255))
        f6 = pygame.font.SysFont('corbel', 48)
        text6 = f6.render("Тест окончен! Результаты внизу", True, (184, 51, 35))
        sc.blit(text6, (150, 50))
        f6 = pygame.font.SysFont('Serif', 28)
        text6 = f6.render(bebra, True, (184, 51, 35))
        sc.blit(text6, (200, 250))
        f6 = pygame.font.SysFont('corbel', 15)
        text6 = f6.render("спасибо за прохождение! если вы хотите переместить этот .EXE файл в другое место, в этой же директории должна лежать папка data !", True, (153, 0, 153))
        sc.blit(text6, (110, 375))
        f6 = pygame.font.SysFont('corbel', 18)
        text6 = f6.render(
            "Написал Turbo Roma, июль 2022 г. | Discord: КТО НАСРАЛ ТОТ УБРАЛ #2509",
            True, (153, 0, 153))
        sc.blit(text6, (250, 450))
    pygame.time.delay(15)
    pygame.display.flip()
