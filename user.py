users = dict()

class User:
    
    def __init__(self, name, id):
        self.name = name
        self.__id = id
        self.game_keyboard = list()
        
    