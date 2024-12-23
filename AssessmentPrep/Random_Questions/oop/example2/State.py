class State:
    def __init__(self, name, city_list):
        self.__name = name
        self.__city_list = city_list


    @property
    def name(self):
        return self.__name

    @property
    def city_list(self):
        return self.__city_list

    @city_list.setter
    def city_list(self, value):
        self.__city_list = value

    def __str__(self):
        return f"{self.__name} has {len(self.__city_list)} cites"