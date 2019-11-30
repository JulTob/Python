import random

def random_walk(n):
    ''' Return coordinates after n steps walk.'''
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
    return (x,y)

def distance(x,y):
    ''' Return distance in n=1 (Manhatan Distance) after coordenates.'''
    return x+y
