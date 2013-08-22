
class grid_render:
    def __init__(self, game_engine):
        self._gameEngine = game_engine
        self._lineColor = (100,100,100)
        self._cellColor = (255, 255, 0)
    def _drawXLines(self, x, dx):
        for i in range (0, x):
            self._gameEngine.draw_line(self._lineColor, (i*dx,0), (i*dx, self._gameEngine.get_height()) )

    def _drawYLines(self, y, dy):
        for i in range (0, y):
            self._gameEngine.draw_line(self._lineColor, (0,i*dy), (self._gameEngine.get_width(), i*dy)  )
    
    def _drawCell(self, dx, dy, index):
        cell = (dx*index[0], dy*index[1], dx, dy)
        self._gameEngine.draw_rect(self._cellColor, cell)
    
    def draw_grid(self, grid):
        dx = self._gameEngine.get_width() / grid.columns
        dy = self._gameEngine.get_height() / grid.rows 
        # draw game field fist   
        self._drawXLines(grid.columns, dx)
        self._drawYLines(grid.rows, dy)
        # draw cells     
        for y in range(grid.rows) :
            for x in range(grid.columns) :
                if (grid._data[y][x] != 0 ):
                    self._drawCell(dx, dy, (x,y))
                    
            
    
