from collections import deque
import functions
import numpy as np

def dbscan(points, colors, minPts, eps):
    queue = deque()
    passed_list = []
    lone_list = []
    while(len(passed_list) + len(lone_list) < len(points)):
        index = append_queue(points, passed_list, lone_list)
        if(index == -1):
            break
        queue.append(index)
        if count_neighbors(points, index, eps) >= minPts:
            color = create_color()
            while(len(queue) > 0):
                ind = queue.popleft()
                if (ind in lone_list):
                    colors[ind] = (255, 255, 0)
                    passed_list.append(ind)
                    lone_list.remove(ind)
                else:
                    neigh = get_neighbors(points, ind, eps)
                    if len(neigh) >= minPts:
                        colors[ind] = (color[0], color[1], color[2])
                        passed_list.append(ind)
                        for n in neigh:
                            if (n not in passed_list) and (n not in queue):
                                queue.append(n)
                    else:
                        colors[ind] = (255, 255, 0)
                        passed_list.append(ind)
        else:
            queue.popleft()
            lone_list.append(index)
    for id in lone_list:
        colors[id] = (255, 0, 0)



def append_queue(points, pased, lone):
    for i in range(len(points)):
        if (i not in pased) and (i not in lone):
            return i
    return -1

def count_neighbors(points, index, eps):
    neighbors = 0
    for i in range(len(points)):
        if (i != index) and (functions.dist(points[i][0], points[i][1], points[index][0], points[index][1]) < eps):
            neighbors += 1
    return neighbors

def get_neighbors(points, index, eps):
    neighbors = []
    for i in range(len(points)):
        if (i != index) and (functions.dist(points[i][0], points[i][1], points[index][0], points[index][1]) < eps):
            neighbors.append(i)
    return neighbors

def create_color():
    color = np.random.randint(0, 255, 3)
    return color