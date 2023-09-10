import pygame
from data.tiles import Tile
from data.settings import tile_size


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile(pos=(x, y), size=tile_size)
                    self.tiles.add(tile)

    def run(self):
        # self.tiles.update(1)
        self.tiles.draw(self.display_surface)
