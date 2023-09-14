import pygame.sprite


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((16, 32))
        self.image.fill('orange')
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 2
        self.gravity = 1
        self.jump_speed = -2
        self.jump_height = 5
        self.jump_f = False

        # tiles
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] == 0:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] == 0:
            self.rect.x -= self.speed

        if keys[pygame.K_UP] and keys[pygame.K_DOWN] == 0:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and keys[pygame.K_UP] == 0:
            self.rect.y += self.speed

        if keys[pygame.K_SPACE]:
            self.jump()

    def insert_gravity(self):
        self.rect.y += self.gravity

    def jump(self):
        actual_s_pos_y = self.rect.y
        for i in range(self.jump_height):
            self.rect.y -= 1

    def update(self) -> None:
        self.get_input()
        self.insert_gravity()
