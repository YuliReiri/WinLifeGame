from random import randint, random

class pattern:
    def __init__(self, rows, columns, probability):
        self._rows = rows
        self._columns = columns
        self._probability = probability
   
# generate random pattern here to a grid        
    def generate(self, grid):
        y = randint(0, grid.rows - self._rows )
        x = randint(0, grid.columns - self._columns )
        for i in range(0, self._rows):
            for j in range(0, self._columns):
                if (random() > self._probability ):
                    grid.set_data(y+i,x+j, 1); 
            