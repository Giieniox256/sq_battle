import pygame
from data.tiles import Tile
from data.settings import tile_size
from data.player import Player


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile(pos=(x, y), size=tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player_sprite = Player(pos=(x, y))
                    self.player.add(player_sprite)

    def horizontal_mov_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_mov_collision(self):
        player = self.player.sprite
        player.insert_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.horizontal_mov_collision()
        self.vertical_mov_collision()
        self.player.draw(self.display_surface)
