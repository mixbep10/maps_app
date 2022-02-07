import sys
import pygame
import requests

NAME_OF_FILE = 'map.png'
longitude = 56.244284
lattitude = 58.006502

class Map_params:
    def __init__(self, longitude, lattitude, spn=0.01, format='map'):
        self.longitude = longitude
        self.lattitude = lattitude
        self.spn = spn
        self.format = format

    def make_dict(self):
        self.dictionary = {}
        self.dictionary['ll'] = ",".join([str(self.longitude), str(self.lattitude)])
        self.dictionary['l'] = self.format
        self.dictionary['spn'] = ",".join([str(self.spn), str(self.spn)])
        return self.dictionary

    def spn_up(self):
        if 0.01 >= self.spn > 0.001:
            self.spn -= 0.001
        elif 0.1 >= self.spn > 0.01:
            self.spn -= 0.01
        elif 1 >= self.spn > 0.1:
            self.spn -= 0.1
        elif 10 >= self.spn > 1:
            self.spn -= 1
        elif 90 >= self.spn > -80:
            self.spn -= 10

    def spn_down(self):
        if 0.01 >= self.spn > 0.001:
            self.spn += 0.001
        elif 0.1 >= self.spn > 0.01:
            self.spn += 0.01
        elif 1 >= self.spn > 0.1:
            self.spn += 0.1
        elif 10 >= self.spn > 1:
            self.spn += 1
        elif 80 >= self.spn > -90:
            self.spn += 10

    def update(self, key):
        if key == pygame.K_PAGEUP:
            self.spn_up()
        if key == pygame.K_PAGEDOWN:
            self.spn_down()


def maps_ai_1(dictionary):
    api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(api_server, params=dictionary)
    # Запишем полученное изображение в файл.
    if not response:
        print('Запрос к серверу был неудачный')
        print(response.url)
        sys.exit()
    else:
        with open(NAME_OF_FILE, "wb") as file:
            file.write(response.content)

def import_map(param_for_req):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                param_for_req.update(event.key)
                maps_ai_1(param_for_req.make_dict())
        screen.blit(pygame.image.load(NAME_OF_FILE), (0, 0))
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    params_save_1 = Map_params(longitude, lattitude)
    import_map(params_save_1)


