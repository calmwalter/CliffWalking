import numpy as np
import random
import time
from Visual2 import GAME
'''
网格4*8
状态4*8*2
初始化全为零
到达cliff区域-100，重新开始
到达终点为100
碰到墙就是-1,但是没死，继续走
每次找最优的走法
学习率0.1

'''
# 选择最佳的行为方向
# x,y为当前的坐标，将要选择下一个坐标,并返回

# direction 1,2,3,4-------->top,bottom,left,right


def pi(net, x, y, row, column):
    #print(x,y)
    if random.randint(1, 10) <= 8:
        # select the most significant direction
        maxq = net[x][y][0]
        direction = 0
        for i in range(1,4):
               if maxq<=net[x][y][i]:
                   direction = i
                   maxq = net[x][y][i]
        #print("selection:")
        #print(net[x][y])
        return direction+1
    else:
        # random choice a direction
        #print("random")
        return random.randint(1, 4)


def QFunc(Q, Qmax, alpha, discount_factor, reward):
    return Q+alpha*(reward+discount_factor*Qmax-Q)


def run(net, x, y, alpha, discount_factor, ex, ey, row, column,episode):
    vi = GAME(row,column,[0,0])
    ox = x
    oy = y
    while episode >0:
        #print(episode)
        notEnd = True
        while notEnd:
            vi.updates([[x,y]])
            time.sleep(0.04)
            reward = -1
            # strategy,get the direction
            direction = pi(net, x, y, row, column)
            # get the new position
            Qmax = -10000
            nx = x
            ny = y
            if direction == 1:
                # top
                if x-1 < 0:
                    reward = -5
                    Qmax = np.max(net[x][y])
                else:
                    if x-1 == 0:
                        if y == ey:
                            reward = 100
                            notEnd = False
                        elif y != 0:
                            reward = -100
                            notEnd = False
                    Qmax = np.max(net[x-1][y])
                    nx = x-1
                    ny = y

            if direction == 2:
                # bottom
                if x+1 > row-1:
                    reward = -5
                    Qmax = np.max(net[x][y])
                else:

                    Qmax = np.max(net[x+1][y])
                    nx = x+1
                    ny = y
            if direction == 3:
                # left
                if y-1 < 0:
                    reward = -5
                    Qmax = np.max(net[x][y])
                else:

                    Qmax = np.max(net[x][y-1])
                    nx = x
                    ny = y-1
            if direction == 4:
                # right
                if x==0 and y==0:
                    reward = -100
                    notEnd = False
                    Qmax = np.max(net[x][y+1])
                    nx = x
                    ny = y+1
                elif y+1 > column-1:
                    reward = -5
                    Qmax = np.max(net[x][y])
                else:
                    Qmax = np.max(net[x][y+1])
                    nx = x
                    ny = y+1

            net[x][y][direction-1] = QFunc(net[x][y][direction-1], Qmax,
                              alpha, discount_factor, reward)
            x = nx 
            y = ny 
        episode -= 1
        x = ox
        y = oy



def get_route(net):
    route = [[0,0]]
    step = 0
    while not(route[step][0]==0 and route[step][1]>0):
        maxq = net[route[step][0]][route[step][1]][0]
        x = route[step][0]-1
        y = route[step][1]
        if maxq < net[route[step][0]][route[step][1]][1]:
            maxq = net[route[step][0]][route[step][1]][1]
            x = route[step][0]+1
            y = route[step][1]
        if maxq < net[route[step][0]][route[step][1]][2]:
            maxq = net[route[step][0]][route[step][1]][2]
            x = route[step][0]
            y = route[step][1]-1
        if maxq < net[route[step][0]][route[step][1]][3]:
            maxq = net[route[step][0]][route[step][1]][3]
            x = route[step][0]
            y = route[step][1]+1
        route.append([x,y])
        step+=1

    return route

if __name__ == "__main__":
    # 初始化网格用来记录权值
    row = 4
    column = 8

    net = np.zeros(row*column*4).reshape(4, 8, 4)


    # 初始化学习率和折扣因素
    alpha = 0.1
    discount_factor = 0.2
    run(net, 0, 0, alpha, discount_factor, 0, column-1, row, column,500)
    print(net)
