import pygame

money = pygame.transform.scale(pygame.image.load("game_assets/coin.png"), (50, 50))


class Button:
    def __init__(self, img, x, y, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        """
        Returns if the position has collided with menu
        :param X:
        :param Y:
        :return:
        """
        if X <= self.x + self.height.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return True

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class Menu:
    """
    Menu for holding items
    """

    def __init__(self, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.items_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img

    def click(self, X, Y):
        """
        Returns if the position has collided with the menu
        :param X:
        :param Y:
        :return:
        """
        if X <= self.x + self.height.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return True

    def add_btn(self, img, name):
        """
        adds button to the menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        inc_x = self.width
        btn_x = self.items * inc_x - img.get_width()/2
        btn_y = self.y + self.height/2
        self.buttons.append(Button(img, btn_x, btn_y, name))

    def draw(self, win):
        """
        draws btns and menu
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - (self.bg.get_width()/2), self.y + 30))
        for item in self.buttons:
            item.draw(win)

    def get_clicked(self, X, Y):
        """
        return the clicked item from the menu
        :param X: int
        :param Y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name
