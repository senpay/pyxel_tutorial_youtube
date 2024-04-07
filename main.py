import pyxel

from model.player import Player
from model.world import World, WorldItem, world_item_draw, TILE_SIZE


class App:
    def __init__(self):
        pyxel.init( World.WIDTH * TILE_SIZE, World.HEIGHT * TILE_SIZE, title="Hello World")
        pyxel.load("mygame.pyxres")

        self.world = World(pyxel.tilemap(0))

        self.player = Player(self.world)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.move_left()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right()    
        elif pyxel.btn(pyxel.KEY_UP):
            self.player.move_up()
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.player.move_down()        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        for y in range(self.world.HEIGHT):
            for x in range(self.world.WIDTH):
                world_item = self.world.world_map[y][x]
                world_item_draw(pyxel, x, y, world_item)

        pyxel.blt(
            self.player.x,
            self.player.y,
            self.player.IMG,
            WorldItem.PLAYER[0] * TILE_SIZE,
            WorldItem.PLAYER[1] * TILE_SIZE,
            self.player.WIDTH,
            self.player.HEIGHT,
        )


App()
