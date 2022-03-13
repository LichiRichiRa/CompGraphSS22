'''
 Программа осуществляет поворот многоугольника на введенный пользователем угол
 относительно введенной пользователем точки. На изображении красная фигура - исходная,
 зеленая - полученная. Построения ведутся в области (-8, 8)(-8, 8)
'''

import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def cond():
    vertexes = []
    print("Введите количество вершин:")
    s = int(input())
    print("Введите вершины многоугольника:")
    for i in range(s):
        vertexes.append(list(map(float, input().split())))
    return vertexes


def turn(vertexes):
    print("Введите точку относительно которой будет совершен поворот (против часовой стрелки):")
    global a
    a = list(map(float, input().split()))
    print("Введите угол (в градусах):")
    alpha = float(input()) / 180 * np.pi
    alpha_mat = [[np.cos(alpha), np.sin(alpha)], [-np.sin(alpha), np.cos(alpha)]]
    new_vertexes = vertexes
    for i in new_vertexes:
        i[0] -= a[0]
        i[1] -= a[1]
    new_vertexes = np.dot(new_vertexes, alpha_mat)
    for i in new_vertexes:
        i[0] += a[0]
        i[1] += a[1]
    return new_vertexes


def drawPolygons(axes, vertexes, color):
    polygon_1 = matplotlib.patches.Polygon(vertexes,
                                           color=color)
    axes.add_patch(polygon_1)


if __name__ == "__main__":
    vertexes = cond()
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)
    plt.grid()
    # Получим текущие оси
    axes = plt.gca()
    axes.set_aspect("equal")

    drawPolygons(axes, vertexes, 'red')
    new_polygon = turn(vertexes)
    drawPolygons(axes, new_polygon, 'green')
    axes.add_patch(matplotlib.patches.Circle(a, 0.1, color= "black"))
    plt.show()
