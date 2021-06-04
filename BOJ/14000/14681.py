x = int(input())
y = int(input())

if (-1000<=x<=1000 and x!=0) and (-1000<=y<=1000 and y!=0):
    if 0<x and 0<y:
        print("1")
    elif 0>x and 0<y:
        print("2")
    elif 0>x and 0>y:
        print("3")
    else:
        print("4")
else:
    x = int(input())
    y = int(input())