import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((16, 32))
        self.image.fill('orange')
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 0.2
        self.gravity = 0.05
        self.jump_speed = -2

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x += 0.5
        elif keys[pygame.K_LEFT]:
            self.direction.x -= 0.5
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def insert_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self) -> None:
        self.get_input()
        self.insert_gravity()
