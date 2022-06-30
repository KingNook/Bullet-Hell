import pyglet
import entities, extras
import typing

def dist(a: extras.Vector, b: extras.Vector) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx**2 + dy**2)**0.5

def pp_to_line(point1: extras.Vector, point2: extras.Vector) -> float:
    ''' returns (a, b, c) where ax + by = c'''

    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]

    grad = dy / dx

    return (-1 * grad, 1, point[1] - grad * point[0])

window = pyglet.window.Window()
pyglet.gl.glClearColor(1, 1, 1, 1)

point = pyglet.shapes.Line(
    x = 0, y = window.height,
    x2 = 0, y2 = window.height,
    width = 10,
    color = (63, 63, 63)
)

collider = pyglet.shapes.Line(
    x = window.width // 2, y = window.height // 2,
    x2 = 0, y2 = 0,
    width = 10,
    color = (127, 15, 15)
)

intersection = pyglet.shapes.Circle(
    x = 0, y = 0,
    radius = 15,
    color = (15, 15, 127)
)

intersection.visible = False

@window.event
def on_draw():
    window.clear()

    if line_line(point, collider):
        collider.color = (15, 127, 15)
    else:
        collider.color = (127, 15, 15)

    collider.draw()

    point.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):

    point.x2 = x
    point.y2 = y


def line_line(line1: pyglet.shapes.Line, line2: pyglet.shapes.Line) -> tuple:
    line1_vector = pp_to_line((line1.x, line1.y), (line1.x2, line1.y2))
    line2_vector = pp_to_line((line2.x, line2.y), (line2.x2, line2.y2))

    # return point of intersection?

def circle_circle(circle1, circle2):
    ''' circle circle collision'''

    circle1_centre = (circle1.x, circle1.y)
    circle2_centre = (circle2.x, circle2.y)

    if dist(circle1_centre, circle2_centre) < circle1.radius + circle2.radius:
        return True
    
    else:
        return False

def point_circle(point, circle):
    ''' point circle collision '''
    
    point_centre = (point.x, point.y)
    circle_centre = (circle.x, circle.y)

    if dist(point_centre, circle_centre) < circle.radius:
        return True
    
    else:
        return False

pyglet.app.run()