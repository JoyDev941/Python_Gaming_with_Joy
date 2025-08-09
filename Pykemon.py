import pygame as pg

#start up game
pg.init()

#set window size
h = 1280
v = 720
display = pg.display.set_mode((h,v))
pg.display.set_caption("Pykemon")
pg.display.set_icon(pg.image.load("icon.ico"))

#set music
pg.mixer.music.load("Music\Goblins_Dance_(Battle).ogg")
pg.mixer.music.play(-1)

#set run mode
Running = True


while Running:

    #set up event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False

    display.fill(pg.Color("chartreuse3"))
    pg.display.update()


pg.quit()