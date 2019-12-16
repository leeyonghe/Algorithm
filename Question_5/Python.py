import sys
import array


max_x = 0
max_y = 0

def Full (img, x, y, c, nowc) :
    img[y][x] = c
    position = [[y-1,x-1],[y,x-1],[y+1,x-1],[y-1,x],[y+1,x],[y-1,x+1],[y,x+1],[y+1,x+1]]
    for i in range(0, 8):
        xx = position[i][0]
        yy = position[i][1]
        print(">>>>>>>>>>>>>>> xx : "+str(xx))
        print(">>>>>>>>>>>>>>> yy : "+str(yy))
        if xx >= 0 and xx < max_y and yy >= 0 and yy < max_x:
            print(">>>>>>>>>>>>>>> ? : "+str(img[xx][yy]))
            print(">>>>>>>>>>>>>>> nowc : "+str(nowc))
            if img[xx][yy] == nowc :
                Full(img, yy, xx, c, nowc)


inputArray = []
while (True) :
    i = input(">")
    if i == 'X' : 
        break
    else :
        inputArray.append(i)

for commands in inputArray :
    seperatecommand = commands.split(' ')
    com_0 = seperatecommand[0]
    if com_0 == 'I':
        print('Make Image')
        max_x = int(seperatecommand[1])
        max_y = int(seperatecommand[2])
        image = [[0]*max_x for i in range(max_y)]
    elif com_0 == 'C':
        print('Clear')
        image = [[0]*max_x for i in range(max_y)]
    elif com_0 == 'L':
        print('')
        x = int(seperatecommand[1])-1
        y = int(seperatecommand[2])-1
        print("x "+str(x)+" | y : "+str(y))
        c = seperatecommand[3]
        image[y][x] = c
    elif com_0 == 'V':
        print('')
        x = int(seperatecommand[1])-1
        y1 = int(seperatecommand[2])-1
        y2 = int(seperatecommand[3])
        print("x "+str(x))
        print("y1 "+str(y1))
        print("y2 "+str(y2))
        c = seperatecommand[4]
        for i in range(y1, y2) :
            print(">>>>>>>>>>>>>>> i : "+str(i))
            image[i][x] = c
    elif com_0 == 'H':
        print('')
        x1 = int(seperatecommand[1])-1
        x2 = int(seperatecommand[2])
        y = int(seperatecommand[3])
        print("x1 "+str(x1))
        print("x2 "+str(x2))
        print("y "+str(y))
        c = seperatecommand[4]
        for i in range(x1, x2) :
            print(">>>>>>>>>>>>>>> i : "+str(i))
            image[y][i] = c
    elif com_0 == 'K':
        print('')
        x1 = int(seperatecommand[1])-1
        x2 = int(seperatecommand[2])
        y1 = int(seperatecommand[3])-1
        y2 = int(seperatecommand[4])
        c = seperatecommand[5]
        for i in range(x1, x2) :
            for j in range(y1, y2) :
                image[j][i] = c
    elif com_0 == 'F':
        print('')
        x = int(seperatecommand[1])-1
        y = int(seperatecommand[2])-1
        c = seperatecommand[3]
        nowc = image[y][x]
        Full(image, x, y, c, nowc)
    elif com_0 == 'S':
        print('')
        name = seperatecommand[1]

print(name)
print(image)