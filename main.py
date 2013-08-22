
import sys

from graphics.grid_render import grid_render
from game.grid import grid
from game.generated_pattern import pattern
from game.threads_pool import threads_pool
from game import row_processor
from graphics.game_engine import game_engine
from random import randint

if sys.platform.startswith('java'):
    import pyj2d as gameengine
else:
    import pygame as gameengine

FIELD_X = 100
FIELD_Y = 100

def swap(buf1, buf2):
    return buf2, buf1

def foo():
    pass 

def start_life():
    """ init pygame game_engine """
    engine = game_engine(gameengine)
    
    """ init to grids """
    grid_view = grid_render(engine)
    buf, field = grid(FIELD_X, FIELD_Y), grid(FIELD_X, FIELD_Y)
    
    p = [pattern(5, 5, 0.2), pattern(3, 7, 0.3), pattern(30, 30, 0.9), pattern(20, 20, 0.8)] 
    """ create patterns on a grid """ 
    for _ in range (100):
        p[randint(0, 3)].generate(field)

    """ create workers to process a grid """
    trp = threads_pool(4)
    loop = True
    while loop:  
        engine.clear_surface()
        grid_view.draw_grid(field)
        engine.update_surface()
        idx = 0
        for row in field._data:
            trp.add_task(row_processor.process, field, buf, row, idx)
            idx += 1
        trp.wait_completion()
        buf, field = swap ( buf, field )        
        for event in engine.get_event():
            if event.type == gameengine.QUIT:
                loop = False 
        
    return 0
if __name__ == "__main__":
    
    sys.exit(start_life())
