
def _calcNeighbors(grid, indx, column):
    nc = 0
    dt = grid.get_data(indx,column+1)
    if (dt == 1): nc += 1
    if (grid.get_data(indx,column-1) == 1   ): nc += 1

    if (grid.get_data(indx+1,column) == 1   ): nc += 1
    if (grid.get_data(indx+1,column+1) == 1 ): nc += 1
    if (grid.get_data(indx+1,column-1) == 1 ): nc += 1
   
    if (grid.get_data(indx-1,column) == 1  ): nc += 1
    if (grid.get_data(indx-1,column-1) == 1 ): nc += 1
    if (grid.get_data(indx-1,column+1) == 1 ): nc += 1
    return nc;

def process(grid, buf, row, row_indx):
    for i in range(len(row)):
        cnt = _calcNeighbors (grid, row_indx, i )
        buf.set_data(row_indx, i, (row[i]) and (cnt == 2) or (cnt == 3) )
    return    
            
