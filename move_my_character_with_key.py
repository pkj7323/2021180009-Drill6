
from pico2d import *


open_canvas()

running = True
run_character = load_image('kirby-run_2.png')
idle_character = load_image('kirby-idle_2.png')
background = load_image('TUK_GROUND.png')
# fill here
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
    # fill here
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dir.x -= 1
            elif event.key == SDLK_RIGHT:
                dir.x += 1
            elif event.key == SDLK_UP:
                dir.y += 1
            elif event.key == SDLK_DOWN:
                dir.y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir.x += 1
            elif event.key == SDLK_RIGHT:
                dir.x -= 1
            elif event.key == SDLK_UP:
                dir.y -= 1
            elif event.key == SDLK_DOWN:
                dir.y += 1

def move():
    global x
    global y
    if x > 790 and dir.x == 1:
        pass
    elif x < 10 and dir.x == -1:
        pass
    else:
        x = x + 10 * dir.x

    if y > 790 and dir.y == 1:
        pass
    elif y < 10 and dir.y == -1:
        pass
    else:
        y = y + 10 * dir.y


dir = Vec2(0,0)
frame_idle = 0
frame_run = 0
run=[3,43,83,123,163,203,243,283,322,360,398,436,474,512,550,588,626,664,701,741,781,821,861,901,941,981,1020,1058,1096,1134,
     1172,1210,1248,1286]
x = 800/2
y = 600/2
while running:

    clear_canvas()
    background.draw(200,100)
    if(dir.x == 0 and dir.y == 0):
        idle_character.clip_draw(3 + 38 * frame_idle,3,33,32,x,y,100,100)
    else:
        if dir.x ==0 or dir.x == 1:
            run_character.clip_draw(run[frame_run], 4, 33, 30, x, y, 100, 100)
        elif dir.x ==-1:
            run_character.clip_composite_draw(run[frame_run], 4, 33, 30, 0, 'h', x, y, 100, 100)
    update_canvas()

    handle_events()
    move()


    frame_idle = (frame_idle + 1) % 14
    frame_run = (frame_run + 1) % len(run)
    delay(0.05)


close_canvas()
