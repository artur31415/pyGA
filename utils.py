import math
from random import randint

def mag(vec):
    return math.sqrt((vec[0] * vec[0] + vec[1] * vec[1]))

def setMag(vec, newMag):
    mag = math.sqrt((vec[0] * vec[0] + vec[1] * vec[1]))
    if mag == 0:
        return vec

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

def vec_sub(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1])

def vec_scalar_mult(vec, scalar):
    return tuple([z * scalar for z in vec])

def vec_dist(vec1, vec2):
    return math.sqrt(math.pow(vec1[0] - vec2[0], 2) + math.pow(vec1[1] - vec2[1], 2))

def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def lerpColor(color1, color2, value, min_value, max_value):
    if value > max_value:
        value = max_value
    return (map(value, min_value, max_value, color1[0], color2[0]), map(value, min_value, max_value, color1[1], color2[1]), map(value, min_value, max_value, color1[2], color2[2]))