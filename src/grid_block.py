
class GridBlock():
    x_min = None
    x_max = None
    y_min = None
    y_max = None
    distance = None    
    block_value = None
    
    def __init__(self, x_min, x_max, y_min, y_max, distance) -> None:
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.distance = distance
        
    def set_block_valule(self, block_value):
        self.block_value = block_value