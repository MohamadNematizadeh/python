from class_media import Media

class Documentary(Media):
    def __init__(self,id,name,director):
        Media.__init__(self,id,name,director)
        self.parts=parts

class Series(Media):
    def __init__(self,N_o_e):
        super().__init__()
        self.N_o_e = N_o_episodes
        
class Film(Media):
    def __init__(self,id=None,name=None,director=None):
        Media.__init__(self,id,name,director)     

class Clip(Media):
    def __init__(self,id=None,name=None,director=None):
        Media.__init__(self,id,name,director)     