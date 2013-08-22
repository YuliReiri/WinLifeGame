
class game_engine():

    def __init__(self, library):
        self.library = library
        self._surface = library.display.set_mode((600,600))
        
    def clear_surface(self):
        self._surface.fill((0,0,0))
    
    def update_surface(self):
        self.library.display.update()
    
    def initialize(self):
        self.library.init()
        self.library.display.set_caption('Game of life')
        
    def get_event(self):
        return self.library.event.get()
    
    def draw_line(self, color, point1, point2):
        self.library.draw.line(self._surface, color, point1, point2 )
    
    def draw_rect(self, color, rect):
        self.library.draw.rect(self._surface, color, rect)
        
    def get_width(self):
        return self._surface.get_width()
    
    def get_height(self):
        return self._surface.get_height()
