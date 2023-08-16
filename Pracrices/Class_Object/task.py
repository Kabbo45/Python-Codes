class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self._speed = speed
        self._radius = radius
        self._color = color
        self._on = on

