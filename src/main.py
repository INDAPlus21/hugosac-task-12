import pygame as pg


class StartScreen:
    def __init__(self):
        self.next = 'start-screen'
        self.running = True

    def start(self):
        self.running = True

    def update(self, keys, screens):
        if keys[pg.K_1]:
            self.next = screens['spring']
            self.running = False
    
    def draw(self):
        pass


class Spring:
    def __init__(self):
        self.next = 'start-screen'
        self.running = True

    def start(self):
        self.running = True
    
    def update(self):
        pass

FPS = 60
TITLE = 'Simple Physics'

pg.init()
WIN = pg.display.set_mode((800,600))
pg.display.set_caption(TITLE)

clock = pg.time.Clock()
running = True
keys = pg.key.get_pressed()
screens = {
    'start-screen': StartScreen(),
    'spring': Spring()
}
screen = screens['start-screen']

def run(clock, running, keys, screens, screen):
    '''Runs main loop'''

    while running:
        # Events
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                keys = pg.key.get_pressed()
        

        # Update
        if not screen.running:
            screen = screens[screen.next]
            screen.start() 
            
        screen.update(keys)

        # Draw
        screen.draw(WIN)
        pg.display.update()

        clock.tick(FPS)

