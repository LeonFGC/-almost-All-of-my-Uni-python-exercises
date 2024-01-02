class View:
    def av_movies(self, peli):
        print('titulo: ' + peli.title + '   precio: ' + peli.price)
    
    def asking_movie(self):
        print('movie?')
        return input()

    def asking_info(self):
        print('2x1?')
        return int(input())
    
    def asking_info2(self):
        print('jubilado?')
        return int(input())
    
    def asking_info3(self):
        print('invalido?')
        return int(input())
    
    def asking_info4(self):
        print('entradas?')
        return int(input())