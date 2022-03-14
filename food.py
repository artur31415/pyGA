class Food:
    position = (0, 0)
    nutrition = 0

    def __init__(self, _position, _nutrition) -> None:
        self.position = _position
        self.nutrition = _nutrition

    def draw(self, DISPLAY):
        if self.nutrition > 0:
            