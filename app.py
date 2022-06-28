import pyglet
from pyglet.window import key

import entities

import extras

WIDTH = 600
HEIGHT = 800

end_loop = False

window = pyglet.window.Window(width = WIDTH, height = HEIGHT)

mouse_prev_position = [0, 0]

# replacing mouse cursor
window.set_mouse_visible(False)

cursor_image = pyglet.image.load('D:/Development/Useful Stuff/applet/pyglet sprite/images/cursor_8.png')
cursor_image.anchor_x = cursor_image.width // 2
cursor_image.anchor_y = cursor_image.height // 2
cursor = pyglet.sprite.Sprite(cursor_image)

# put working cursor code here if i eventually figure it out
'''
cursor = pyglet.window.ImageMouseCursor(cursor_image, cursor_image.width // 2, cursor_image.height // 2)
window.set_mouse_cursor(cursor)
'''

player = entities.Player()   
bullet = entities.Bullet()

# EXITING THE WINDOW
@window.event
def on_key_press(symbol, modifiers):
    global end_loop

    # close window on alt+f4
    if symbol == key.F4 and modifiers & key.MOD_ALT:
        end_loop = True

@window.event
def on_close():
    global end_loop
    end_loop = True

# GAME LOOP
@window.event
def on_draw():
    window.clear()

    # move player to mouse cursor
    player.move(cursor.x, cursor.y)

    player.draw()

    # draw cursor AFTER player so cursor is overlayed
    cursor.draw()

@window.event
def on_mouse_motion(x, y, d1, d2):

    cursor.x = x
    cursor.y = y

@window.event
def on_mouse_drag(x, y, d1, d2, button, modifiers):

    cursor.x = x
    cursor.y = y

while not end_loop:
    pyglet.clock.tick()

    for w in pyglet.app.windows:
        w.switch_to()
        w.dispatch_events()
        w.dispatch_event('on_draw')
        w.flip()