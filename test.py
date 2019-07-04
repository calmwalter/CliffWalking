from Visual import GAME
from CliffWalking import *



random.seed(time.time())
# 初始化网格用来记录权值
row = 20
column = 20
net = np.zeros(row*column*4).reshape(row, column, 4)
# 初始化学习率和折扣因素
alpha = 0.1
discount_factor = 0.3
run(net, 0, 0, alpha, discount_factor, 0, column-1, row, column,5000)
print(net)
route = get_route(net)
print(route)

display = GAME(row,column,route)

display.run()