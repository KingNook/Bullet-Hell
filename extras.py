import typing
import math

Vector = typing.NewType('Vector', typing.List[float])

def round_down(max_speed: int, change: int) -> int:
    max_v = abs(max_speed)
    if change < -1 * max_v:
        return -1 * max_v
    elif change > max_v:
        return max_v
    else:
        return change


def dot_prod(a: Vector, b: Vector) -> float:
    ''' returns a.b (vector calculation) '''
    if len(a) != len(b):
        raise IndexError

    return sum( [ a[i] * b[i] for i in range(len(a)) ] )

def scale(scalar: float, v: Vector):
    return [scalar*i for i in v]

def mag(a: Vector) -> float:
    ''' return magnitude of a given vector'''
    return dot_prod(a, a)**0.5

def tan(angle: float) -> float:
    return math.sin(angle)/math.cos(angle)


def round_down_vector(max_speed: float, dir_vector: Vector) -> Vector:
    ''' if the magnitude of the direction vector is greater than the max speed, the vector will be scaled down to the max speed '''
    vector_magnitude = mag(dir_vector)

    if vector_magnitude <= max_speed:
        return dir_vector
    else:
        scale_factor = max_speed / vector_magnitude
        return scale(scale_factor, dir_vector)

def unit_vector_ang(angle: float) -> Vector:

    y = tan(angle)

    print(f'angle // y : {angle} // {y}')

    magnitude = mag((1,y))

    return scale(1/magnitude, [1,y])