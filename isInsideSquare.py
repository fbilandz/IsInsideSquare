square = []

def pravacY(x1, x2, y1, y2, x):
    y = (y2-y1)*(x-x1)/(x2-x1) + y1
    return y

def pravacX(x1, x2, y1, y2, y):
    x = (x2-x1)*(y-y1)/(y2-y1) + x1
    return x

def is_inside(x, y):
    if y >= pravacY(square[0][0], square[1][0], square[0][1], square[1][1], x):
        if y <= pravacY(square[2][0], square[3][0], square[2][1], square[3][1], x):
            if x >= pravacX(square[0][0], square[3][0], square[0][1], square[3][1], y):
                if x <= pravacX(square[1][0], square[2][0], square[1][1], square[2][1], y):
                    return True
    return False

def unos():
    x = int(input())
    y = int(input())
    square.append((x, y))

def poslozi():
    sortedY = sorted(square, key=lambda tup: tup[1])
    final = []
    if sortedY[0][0] <= sortedY[1][0]:
        final.append(sortedY[0])
        final.append(sortedY[1])
    else: 
        final.append(sortedY[1])
        final.append(sortedY[0])
    if sortedY[2][0] >= sortedY[3][0]:
        final.append(sortedY[2])
        final.append(sortedY[3])
    else: 
        final.append(sortedY[3])
        final.append(sortedY[2])
    return final


i = 0
while i < 4:
    unos()
    i += 1

x = int(input())
y = int(input())
square = poslozi()
print (is_inside(x,y))