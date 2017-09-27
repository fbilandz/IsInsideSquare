square = []

def pravacY(x1, x2, y1, y2, x):
    print(x1, x2, y1, y2, x)
    y = (y2-y1)*(x-x1)/(x2-x1) + y1
    print(y)
    return y

def pravacX(x1, x2, y1, y2, y):
    x = (x2-x1)*(y-y1)/(y2-y1) + x1
    print(x)
    return x

def is_inside(x, y):
    if y >= pravacY(float(square[0][0]), float(square[1][0]), float(square[0][1]), float(square[1][1]), float(x)):
        if y <= pravacY(float(square[2][0]), float(square[3][0]), float(square[2][1]), float(square[3][1]), float(x)):
            if x >= pravacX(float(square[0][0]), float(square[3][0]), float(square[0][1]), float(square[3][1]), float(y)):
                if x <= pravacX(float(square[1][0]), float(square[2][0]), float(square[1][1]), float(square[2][1]), float(y)):
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