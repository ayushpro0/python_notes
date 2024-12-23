class City:
    def __init__(self, name, state):
        self.__name = name
        self.__state = state

    def __str__(self):
        return f"{self.__name} is is state {self.__state}"
