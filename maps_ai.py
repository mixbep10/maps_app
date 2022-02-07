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

def import_map():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(NAME_OF_FILE), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

if __name__ == '__main__':
    params_save_1 = Map_params(longitude, lattitude)
    my_dict = params_save_1.make_dict()
    maps_ai_1(my_dict)
    import_map()







