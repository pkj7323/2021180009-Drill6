from pico2d import *
import random

open_canvas()



class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    x=0
    y=0

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def move():
    global x
    global y
    global dir
    global rx
    global ry
    x1 = x
    y1 = y
    if x > rx:
        dir.x = -1
    elif x < rx:
        dir.x = 1
    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = (1 - t) * x1 + t * rx
        y = (1 - t) * y1 + t * ry
        draw()
    randomXY()
def draw():
    global x
    global y
    global dir
    global frame_run
    global frame_idle
    global rx
    global ry
    clear_canvas()
    background.draw(200, 100)
    hand.draw(rx, ry)
    if dir.x == 1:
        run_character.clip_draw(run[frame_run], 4, 33, 30, x, y, 100, 100)
    elif dir.x == -1:
        run_character.clip_composite_draw(run[frame_run], 4, 33, 30, 0, 'h', x, y, 100, 100)
    frame_idle = (frame_idle + 1) % 14
    frame_run = (frame_run + 1) % len(run)
    update_canvas()
    delay(0.05)
def randomXY():
    global rx
    global ry
    rx = random.randint(0, 800)
    ry = random.randint(0, 600)

running        = True
run_character  = load_image('kirby-run_2.png')
idle_character = load_image('kirby-idle_2.png')
background     = load_image('TUK_GROUND.png')
hand           = load_image('hand_arrow.png')
rx             = random.randint(0,800)
ry             = random.randint(0,600)
dir            = Vec2(0,0)
frame_idle     = 0
frame_run      = 0
run = [3,43,83,123,163,203,243,283,322,360,398,436,474,512,550,588,626,
       664,701,741,781,821,861,901,941,981,1020,1058,1096,1134,1172,1210,1248,1286]
x = 800/2
y = 600/2

while running:
    move()
    handle_events()



close_canvas()
