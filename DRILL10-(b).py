from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(
            self.frame * 100, 0, 100, 100,
            self.x, self.y
        )


class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(
            self.frame * frame_width, 0, frame_width, frame_height,
            self.x, self.y, frame_width // 2, frame_height // 2
            )
        

class Ball:
    def __init__(self):
        self.size = random.choice([21,41])

        if self.size == 21:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x = random.randint(100, 700)
        self.y = 90

        self.speed = random.uniform(3,0 , 8.0)

        self.ground_y = 90 + self.size 


    def draw(self):
        self.image.draw(self.x, self.y)


def reset_world():
    global running, grass, world, team

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    zombie = Zombie()
    world.append(zombie)

    team = [Boy() for _ in range(11)]
    world += team

    balls = [Ball() for _ in range(20)]
    world += balls


def update_world():
    for obj in world:
        obj.update()


def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()