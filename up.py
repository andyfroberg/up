from model import Model
from controller import Controller
from view import View

class Up:
    def __init__(self):
        model = Model()
        view = View()
        controller = Controller(model, view)
        # self.view = View(self.model)
        # controller.register_view(self.view)
        controller.start()


if __name__ == "__main__":
    game = Up()