red = [255, 0, 0]
orange = [255, 64, 0]
yellow = [255, 255, 0]
light_green = [64, 255, 0]

green = [0, 255, 0]
spring_green = [0, 255, 64]
cyan = [0, 255, 255]
azure = [0, 64, 155]

blue = [0, 0, 255]
violet = [64, 0, 255]
magenta = [255, 0, 255]
rose = [255, 0, 64]

black = [0, 0, 0]
white = [255, 255, 255]

twelve_colors = [
    red,
    orange,
    yellow,
    light_green,

    green,
    spring_green,
    cyan,
    azure,

    blue,
    violet,
    magenta,
    rose,
]

def AlphaBlend(scr_color, dest_color, src_alpha, des_alpha):
    if src_alpha == 255:
        return [scr_color[0], scr_color[1], scr_color[2], src_alpha]

    rgb = Lerp(dest_color, scr_color, src_alpha)
    return [rgb[0], rgb[1], rgb[2], 1-(1-src_alpha)*(1-des_alpha)]

def Blend(color_a, color_b, t):
    if t == 0:
        return color_a
    elif t == 1:
        return color_b
    else:
        one_minus = 1-t

        r = color_a[0] * one_minus + color_b[0] * t
        g = color_a[1] * one_minus + color_b[1] * t
        b = color_a[2] * one_minus + color_b[2] * t
        a_a = 1 if len(color_a) == 3 else color_a[3]
        b_a = 1 if len(color_b) == 3 else color_b[3]
        a = 1 - (1-a_a)* (1-b_a)
        return [r, g, b, a]


def Lerp(color_a, color_b, t):
    return [a*(1-t) + b*t for a, b in zip(color_a, color_b)]

def Multiply(color_a, color_b):
    return [a * b /255.0 for a, b in zip(color_a, color_b)]

def Scale(color_a, scale):
    return [v * scale for v in color_a]

def get_color_from_hsv(h, s, v):
    if s == 0:
        return [v, v, v]

    h /= 60
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1-f))

    if i == 0:
        return [v, t, p]
    elif i == 1:
        return [q, v, p]
    elif i == 2:
        return [p, v, t]
    elif i == 3:
        return [p, q, v]
    elif i == 4:
        return [t, p, v]
    else:
        return [v, p, q]