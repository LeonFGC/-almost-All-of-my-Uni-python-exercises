from model import Movies
from view import View
view = View()

class Controller:
    def get_movies(self):
        pelis = []

        with open('pelis.txt', 'r') as f:
            for lines in f:
                title, price, week = lines.strip().split('/')
                peli = Movies(title, price, int(week))
                pelis.append(peli)

        for peli in pelis:
            view.av_movies(peli)
        return pelis


    def buying_process(self, pelis):

        movie = view.asking_movie()
        tickets = view.asking_info4()
        retired = view.asking_info2()
        crippled = view.asking_info3()

        for peli in pelis:
            if peli.title == movie:

                if peli.week == 1:
                    peli.price = int(peli.price) * 0.6

                if tickets > 1:
                    twoxone = view.asking_info()
                    if twoxone == 1:
                        x = int(peli.price)
                        peli.price = int(peli.price) * tickets
                        peli.price = int(peli.price) - x
                        twoxone = 'si'
                    else: 
                        twoxone = 'no'
                        peli.price = int(peli.price) * tickets


                if retired == 1:
                    peli.price = int(peli.price) * 0.5
                    retired = 'si'
                if retired == 0:
                    retired = 'no'

                if crippled == 1:
                    peli.price = 0
                    crippled = 'si'
                if crippled == 0:
                    crippled = 'no'
                
                save = (f'pelicula: {peli.title}, importe: {peli.price}, jubilado: {retired}, cupon: {twoxone}, discapacitado: {crippled}, cantidad de entradas: {tickets}\n')
        return save
        
    
    def save_data(self, save):
        with open('ventas.txt', 'a') as f:
            f.write(save)