class Atmosphere:
    __state = {}

    def __init__(self):
        self.__dict__ = self.__state

        if not self.__state:
            self.__set_defaults()

    def __set_defaults(self):
        self.carbon_dioxide_level = 200
