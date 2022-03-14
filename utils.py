import math
from random import randint


def setMag(vec, newMag):
    mag = math.sqrt((vec[0] * vec[0] + vec[1] * vec[1]))
    f = newMag / mag
    return (vec[0] * f, vec[1] * f)

def clamp(vec, limit):
    norm = math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
    f = 1
    if norm >= limit:
        f = limit / norm

    return (vec[0] * f, vec[1] * f)

def randFloat(init, end):
    f = 10
    return randint(init * 10, end * 10) / float(f)

def vec_add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def vec_scalar_mult(vec, scalar):
    return tuple([z * scalar for z in vec])