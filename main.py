import pygame

pygame.init()

# Create the screen
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jerry opens the noor")
tile_size = 50
wall_img = pygame.image.load("Wall.png")
air_img = pygame.image.load("NOTHING.png")
clicked = False
world_map1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class World:
    def __init__(self, world_map):
        self.map = world_map
        self.tile_list = []
        row_count = 0
        for row in self.map:
            col_count = 0
            for col in row:
                if col == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 1, col_count, row_count)
                    self.tile_list.append(tile)
                if col == 0:
                    img = pygame.transform.scale(air_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0, col_count, row_count)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
            
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

    def clicked(self):
        global clicked
        global world_map1
        global world1
        for tile in self.tile_list:
            x_point = tile[3]
            y_point = tile[4]
            key = pygame.mouse.get_pressed()
            if key[0]:
                mouse_position = pygame.mouse.get_pos()
                if tile[1].collidepoint(mouse_position[1], mouse_position[0]) and not clicked:
                    if world_map1[x_point][y_point] == 0:
                        world_map1[x_point][y_point] = 1
                    elif world_map1[x_point][y_point] == 1:
                        world_map1[x_point][y_point] = 0
                    clicked = True
                    world1 = World(world_map1)
                if clicked:
                    pygame.time.delay(500)
                    clicked = False


world1 = World(world_map1)
run = True
while run:
    world1.clicked()
    world1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(world_map1)
            run = False
    pygame.display.update()
pygame.quit()

