from model.pyxel_utlis import PyxelSounds
from model.utils import round_float_if_close
from model.world import TILE_SIZE, WorldItem, sprites_collide


class Player:
    IMG = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 0.5
    ROUNDING_ERROR_DELTA = 0.1

    def __init__(self, world):
        self.__x = world.player_grid_x * TILE_SIZE
        self.__y = world.player_grid_y * TILE_SIZE
        self.world = world
        self.pyxel_sounds = PyxelSounds()

    def stop_moving(self):
        self.__x = round_float_if_close(self.__x, self.ROUNDING_ERROR_DELTA)
        self.__y = round_float_if_close(self.__y, self.ROUNDING_ERROR_DELTA)

    # dx should be 1 or -1 (for right or left)
    def move_horizontally(self, dx):
        tile_y = int(self.__y / TILE_SIZE)
        tile_x = int(self.__x / TILE_SIZE)

        new_x = self.__x + dx * self.DX

        new_tile_x = tile_x + dx

        if new_tile_x < 0 or new_tile_x >= self.world.WIDTH:
            return

        # We always round "Down", so we can consider possible "up" and "bottom" tiles
        next_tile_up = self.world.world_map[tile_y][new_tile_x]
        next_tile_bottom = self.world.world_map[tile_y + 1][new_tile_x]

        if (
            next_tile_up == WorldItem.WALL
            and sprites_collide(
                new_x, self.__y, new_tile_x * TILE_SIZE, tile_y * TILE_SIZE
            )
        ) or (
            next_tile_bottom == WorldItem.WALL
            and sprites_collide(
                new_x, self.__y, new_tile_x * TILE_SIZE, (tile_y + 1) * TILE_SIZE
            )
        ):
            self.pyxel_sounds.play_hit_wall_sound()
            return

        self.__x = new_x       

    def move_left(self):
        self.move_horizontally(-1)

    def move_right(self):
        self.move_horizontally(1)

    # dy should be 1 or -1 (for down or up)
    def move_vertically(self, dy):
        tile_y = int(self.__y / TILE_SIZE)
        tile_x = int(self.__x / TILE_SIZE)

        new_y = self.__y + dy * self.DX
        new_tile_y = tile_y + dy

        # We always round "Down", so we can consider possible "left" and "right" tiles
        next_tile_left = self.world.world_map[new_tile_y][tile_x]
        next_tile_right = self.world.world_map[new_tile_y][tile_x + 1]

        if (
            next_tile_left == WorldItem.WALL
            and sprites_collide(
                self.__x, new_y, tile_x * TILE_SIZE, new_tile_y * TILE_SIZE
            )
        ) or (
            next_tile_right == WorldItem.WALL
            and sprites_collide(
                self.__x, new_y, (tile_x + 1) * TILE_SIZE, new_tile_y * TILE_SIZE
            )
        ):
            self.pyxel_sounds.play_hit_wall_sound()
            return

        self.__y = new_y

    def move_up(self):
        self.move_vertically(-1)

    def move_down(self):
        self.move_vertically(1)

    @property
    def x(self):
        return int(self.__x)
    
    @property
    def y(self):
        return int(self.__y)
