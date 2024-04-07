from model.world import TILE_SIZE, WorldItem

class Player:
    IMG = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 0.5

    def __init__(self, world):
        self.x = world.player_grid_x * TILE_SIZE
        self.y = world.player_grid_y * TILE_SIZE
        self.world = world

       
    def move_left(self):
        tile_y = int(self.y / TILE_SIZE)
        tile_x = int(self.x / TILE_SIZE)

        new_x = self.x - self.DX
        new_tile_x = tile_x - 1

        next_tile = self.world.world_map[tile_y][new_tile_x]
        if next_tile == WorldItem.WALL:
            if new_tile_x * TILE_SIZE + TILE_SIZE > new_x:
                # collides with the left wall, so we can't move
                return

        self.x = new_x

    def move_right(self):
        tile_y = int(self.y / TILE_SIZE)
        tile_x = int(self.x / TILE_SIZE)

        new_x = self.x + self.DX
        new_tile_x = tile_x + 1

        next_tile = self.world.world_map[tile_y][new_tile_x]
        if next_tile == WorldItem.WALL:
            if new_x + TILE_SIZE > new_tile_x * TILE_SIZE:
                # collides with the right wall, so we can't move
                return
            
        self.x = new_x

    def move_up(self):
        tile_y = int(self.y / TILE_SIZE)
        tile_x = int(self.x / TILE_SIZE)

        new_y = self.y - self.DX
        new_tile_y = tile_y - 1

        next_tile = self.world.world_map[new_tile_y][tile_x]
        if next_tile == WorldItem.WALL:
            if new_tile_y * TILE_SIZE + TILE_SIZE > new_y:
                # collides with the up wall, so we can't move
                return
            
        self.y = new_y

    def move_down(self):
        tile_y = int(self.y / TILE_SIZE)
        tile_x = int(self.x / TILE_SIZE)

        new_y = self.y + self.DX
        new_tile_y = tile_y + 1

        next_tile = self.world.world_map[new_tile_y][tile_x]
        if next_tile == WorldItem.WALL:
            if new_y + TILE_SIZE > new_tile_y * TILE_SIZE:
                # collides with the bottom wall, so we can't move
                return
            
        self.y = new_y



