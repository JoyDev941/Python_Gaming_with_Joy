import pygame as pg

pg.init()
h = 1280
v = 720

display = pg.display.set_mode((h,v))
pg.mixer.music.load("Assets\Goblins_Dance_(Battle).ogg")
pg.mixer.music.play(-1)
Running = True


while Running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False

    display.fill(pg.Color("chartreuse3"))
    pg.display.update()


pg.quit()