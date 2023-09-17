import pygame

from data.player import Player
from data.settings import tile_size
from data.tiles import Tile


class Level:

    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.jump_flag = False

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

        # for sprite in self.tiles.sprites():
        #     print(sprite.rect.colliderect(player.rect))

        hit_wall = pygame.sprite.spritecollideany(player, self.tiles)
        print()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # print(sprite.rect.colliderect(player.rect))
                if player.rect.right == sprite.rect.left:
                    player.move_left = False
                    # player.rect.right = sprite.rect.left
                elif player.rect.left == sprite.rect.right:
                    player.move_right = False
                    # player.rect.left = sprite.rect.right
            else:
                player.move_left = True
                player.move_right = True

        # for sprite in self.tiles.sprites():
        #     if sprite.rect.colliderect(player.rect):
        #         if player.rect.x > sprite.rect.x:
        #             player.rect.left = sprite.rect.right
        #         elif player.rect.x < sprite.rect.x:
        #             player.rect.right = sprite.rect.left

    def vertical_mov_collision(self):
        player = self.player.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.collidedict(player.rect):
                print(sprite.rect)

        onground = pygame.sprite.spritecollideany(player, self.tiles)
        # print(onground)
        if onground:
            player.move_down = False
        else:
            player.move_down = True

    def collision(self):
        player = self.player.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                print('sprite', sprite.rect)
                print('player', player.rect)

        onground = pygame.sprite.spritecollideany(player, self.tiles)
        if onground:
            print(onground)
            player.move_down = False
        else:
            player.move_down = True

    def run(self):
        self.tiles.draw(self.display_surface)
        # self.horizontal_mov_collision()
        # self.vertical_mov_collision()
        self.collision()
        self.player.update()
        self.player.draw(self.display_surface)
