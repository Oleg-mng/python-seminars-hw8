from datetime import datetime as dt
from time import time


x = 0
y = 0
q = 0


def init(a, b, c):
    global x
    global y
    global q
    x = a
    y = b
    q = c


def write():
    with open('directory.txt', 'a') as data:
        data.write(x+' '+y+' '+q)
        data.write('\n')


def time_logger():
    # time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        csvstr = dt.strftime(dt.now(), '%Y - %m - %d - %H - %m')
        file.writelines(csvstr)
        

# mydate = dt.now()
# csvstr = dt.strftime(dt.now(), '%Y - %m - %d')
# print(csvstr)

# time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};;{}\n'
#                     .format(time))