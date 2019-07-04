from VisualCliff import *

# 初始化网格用来记录权值
row = 4
column = 8

net = np.zeros(row*column*4).reshape(4, 8, 4)


# 初始化学习率和折扣因素
alpha = 0.1
discount_factor = 0.2
run(net, 0, 0, alpha, discount_factor, 0, column-1, row, column,500)
print(net)
