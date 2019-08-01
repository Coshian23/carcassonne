class tile_class:
    def __init__(self):
        name = ""
        image = ""
        array = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
        pennant = False
        cloister = False

tile = [None for _ in range(72)]

# a 2
for i in [0,1]:
    tile[i] = tile_class()
    tile[i].name = "a-tile"
    tile[i].image = "a-tile.png"
    tile[i].array = [["F0","F0","F0"],
                     ["F0","CL","F0"],
                     ["F0","R0","F0"]]
    tile[i].pennant = False
    tile[i].cloister = True

# b 4
for i in [3,4,5,6]:
    tile[i] = tile_class()
    tile[i].name = "b-tile"
    tile[i].image = "b-tile.png"
    tile[i].array = [["F0","F0","F0"],
                     ["F0","CL","F0"],
                     ["F0","F0","F0"]]
    tile[i].pennant = False
    tile[i].cloister = True

# c 1
for i in [7]:
    tile[i] = tile_class()
    tile[i].name = "c-tile"
    tile[i].image = "c-tile.png"
    tile[i].array = [[0,"C0",0],
                     ["C0","C0","C0"],
                     [0,"C0",0]]
    tile[i].pennant = True
    tile[i].cloister = False

# d 4
for i in [8,9,10,11]:
    tile[i] = tile_class()
    tile[i].name = "d-tile"
    tile[i].image = "d-tile.png"
    tile[i].array = [["F0","R0","F1"],
                     ["F0","R0","C0"],
                     ["F0","R0","F1"]]
    tile[i].pennant = False
    tile[i].cloister = False
