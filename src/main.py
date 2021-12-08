import pygame as pg
from vectors import Vector, vector_from_points

# Constants
FPS = 60
TITLE = 'Simple Physics'
WIDTH = 800
HEIGHT = 600
RADIUS = 25
TOP_SPEED = 10
BALL_COLOR = (234, 97, 100)
BACKGROUND = (37, 39, 42)

def update(pos, vel, acc):
    '''Update positions'''
    mouse = Vector(*pg.mouse.get_pos())
    acc = vector_from_points(mouse, pos)
    acc.normalize()
    acc.scale(0.5)
    vel.add(acc) 
    pos.add(vel)

def draw(win, pos):
    '''Draw everything'''
    win.fill(BACKGROUND)
    pg.draw.circle(win, BALL_COLOR, pos.pos(), RADIUS)

def main():
    '''Runs main loop'''
    pg.init()
    win = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()
    running = True

    pos = Vector(WIDTH / 2, HEIGHT / 2)
    vel = Vector(0,0)
    vel.set_limit(TOP_SPEED)
    acc = Vector(0,0)

    while running:
        # Main loop
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                running = False

        update(pos, vel, acc)
        draw(win, pos)

        pg.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()