from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running, dir, ydir
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here

        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dir=+1
            elif event.key==SDLK_LEFT:
                dir=-1
            elif event.key==SDLK_ESCAPE:
                running=False
            elif event.key == SDLK_UP:
                ydir = +1
            elif event.key == SDLK_DOWN:
                ydir = -1
        elif event.type==SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                dir-=1
            elif event.key==SDLK_LEFT:
                dir+=1
            if event.key ==SDLK_UP:
                ydir-=1
            elif event.key==SDLK_DOWN:
                ydir+=1


running = True
x = 800 // 2
y = 60
frame = 0
dir=0
ydir=0

# fill here

while running:
    clear_canvas()
    ground.draw(400,200)
    character.clip_draw(frame*32, 0, 34, 34, x, y,100,100)
    update_canvas()
    handle_events()
    frame=(frame+1)%5
    x+=dir*10
    y+=ydir*10
    delay(0.1)

close_canvas()
