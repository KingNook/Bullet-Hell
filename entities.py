import pyglet
import typing
import extras

from math import atan2

# Stick with absolute image paths for now since i'm using different cwds from session to session
# when actually deploying game, switch to relative paths
# list of places where abs paths are used in 'absolute_paths.txt'

class Entity:

    def __init__(self, image_path: str, x_pos: float = 0, y_pos: float = 0, max_speed: float = 10):

        # loads sprite image from give image path, creates self.sprite w/ image, anchors to centre
        # by default will place sprite at 0, 0 unless a default value of x, y are given 
        sprite_img = pyglet.image.load(image_path)
        sprite_img.anchor_x = sprite_img.width // 2
        sprite_img.anchor_y = sprite_img.height // 2

        self.sprite = pyglet.sprite.Sprite(sprite_img, x_pos, y_pos)

        self._x = x_pos
        self._y = y_pos

        print(max_speed)

        self.max_speed = max_speed

        self.dx = 0
        self.dy = 0 
    
    def draw(self):
        ''' draws sprite '''

        return self.sprite.draw()

    def move(self, x = 0, y = 0):
        ''' updates velocity so that entity moves towards intended target, then updates x and y positions '''
        self.update_velocity(x, y)

        self.x += self.dx
        self.y += self.dy

    def update_velocity(self, x, y):
        ''' update velocity so that entity moves towards a point x, y with maximum speed'''
        
        move_vector = extras.round_down_vector(self.max_speed, self.dir_vector((x, y)))

        self.dx = move_vector[0]
        self.dy = move_vector[1]

        return (self.dx, self.dy)

    def dir_vector(self, point: extras.Vector) -> extras.Vector:
        ''' returns the direction vector to a point '''

        return [point[0] - self.x, point[1] - self.y]

    # direction from self to point
    def dir(self, point: extras.Vector) -> float:
        ''' returns the bearing FROM THE POSITIVE X DIRECTION // gives a value between -pi and pi radians'''
        # should be returning the direction from position to a point
        return atan2(point[1] - self.y, point[0] - self.x)

    # x getter
    @property
    def x(self):
        return self.sprite.x

    @x.setter
    def x(self, val):
        self.sprite.x = val

    # y getter
    @property
    def y(self):
        return self.sprite.y

    @y.setter
    def y(self, val):
        self.sprite.y = val

class Player(Entity):
    
    player_img_path = 'D:/Development/Useful Stuff/applet/pyglet sprite/images/spaceship_64.png'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, image_path=Player.player_img_path, **kwargs)

        # player has a higher max speed than other entities
        self.max_speed = 15

    def update_pos(self):
        pass

    def update_vel(self):
        pass

class Bullet(Entity):

    bullet_img_path = 'D:/Development/Useful Stuff/applet/pyglet sprite/images/bullet_16.png'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, image_path=Bullet.bullet_img_path, **kwargs)