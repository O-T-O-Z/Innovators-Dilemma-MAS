import random

### COLOR SAMPLING

def get_random_color():
    r = lambda: random.randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())

def sample_color(x=0.5, a=(115, 140, 255), b=(69, 101, 247)):
    assert x >= 0 and x <= 1
    c = [0, 0, 0]
    for i in range(3):
        
        c[i] = int(x*float(a[i]) + (1.0-x)*float(b[i]))
    return "#%02X%02X%02X" % (c[0], c[1], c[2])

def sample_color_rgb_gradient(x, color):
    if color == "red":
        return sample_color(x, a=(255, 163, 163), b=(184, 44, 58))
    if color == "green":
        return sample_color(x, a=(166, 255, 175), b=(51, 145, 73))
    if color == "blue":
        return sample_color(x, a=(162, 171, 252), b=(69, 101, 247))

sample_color_rgb_gradient_random = lambda color: sample_color_rgb_gradient(random.random(), color)

###