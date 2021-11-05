import numpy as np
import random


def near_point(x, y, points, colors, r):
    points.append([x, y])
    k = random.randint(1, 4)
    d = list(range(-5 * r, -2 * r)) + list(range(2 * r, 5 * r))
    for i in range(k):
        x_new = x + random.choice(d)
        y_new = y + random.choice(d)
        points.append([x_new, y_new])
        i = i - 1
    for i in range(k + 1):
        colors.append((0, 0, 0))


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def flags(points, colors, minPts, eps):
    for i in range(len(points)):
        neighb = 0
        for j in range(len(points)):
            if dist(points[i][0], points[i][1],
                    points[j][0], points[j][1]) < eps:
                neighb += 1
        if neighb > minPts:
            colors[i] = (0, 255, 0)
    for i in range(len(points)):
        if colors[i] != (0, 255, 0):
            for j in range(len(points)):
                if colors[j] == (0, 255, 0):
                    if dist(points[i][0], points[i][1],
                            points[j][0], points[j][1]) < eps:
                        colors[i] = (255, 165, 0)
    for i in range(len(points)):
        if colors[i] != (0, 255, 0) and colors[i] != (255, 165, 0):
            colors[i] = (255, 0, 0)



