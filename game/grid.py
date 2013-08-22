
class grid:
    def __init__(self, row, column):
# init 2d array here with zero values      
        self._data = [[0]*column for _ in range(row)]
        self.rows = row
        self.columns = column

    def set_data(self, row, column, value):
        self._data[row][column] = int(value)
        
    def get_data(self, row, column):
        return self._data[row % self.rows][column % self.columns]
        
