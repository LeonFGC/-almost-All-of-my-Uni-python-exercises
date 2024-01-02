from controller import Controller
if __name__ == '__main__':
    controller = Controller()
    pelis = controller.get_movies()
    save = controller.buying_process(pelis)
    controller.save_data(save)